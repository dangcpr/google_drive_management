import io
from fastapi import APIRouter, Response, logger
from googleapiclient.http import MediaIoBaseDownload, HttpError
from src.helpers.convert_type import checkAppTypeIsSupport, checkGoogleTypeIsSupport, convertAppToExtension, convertExtensionToApp, convertTypeGoogleToApp, convertTypeGoogleToExtension
from src.constants.drive import service

router = APIRouter(
    prefix="/google/drive",
    tags=["files"],
    responses={404: {"description": "Not found"}},
)


@router.get("/list", summary="Get list file from Google Drive")
async def getFile(response: Response):
    try:
        drive = service.files().list().execute()
        # folders = drive.get('files').get('mimeType') == 'application/vnd.google-apps.folder'
        # return {"folders": list(filter(lambda x: x['mimeType'] == 'application/vnd.google-apps.folder', drive.get('files')))}
        return {"files": drive.get('files')}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}


@router.get("/list/{folder_id}", summary="Get list file in a folder")
async def getFilesInFolder(folder_id: str, response: Response):
    try:
        drive = service.files().list(q=f"'{folder_id}' in parents").execute()
        return {"files": drive}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}


@router.get("/download/file/{file_id}", summary="Download a file")
async def downloadFile(file_id: str, response: Response, type: str | None = None):
    try:
        # get info file
        drive = service.files().get(fileId=file_id).execute()

        # type must include ".", ex: ".pdf". "None" means download as pdf and get file name
        type_end = f".{type}" if type else ".pdf"
        file_name = drive["name"] + type_end

        # download file
        request = service.files().export_media(
            fileId=file_id, mimeType=convertExtensionToApp(type_end))
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()

        # save file
        file.seek(0)
        with open(f"download/{file_name}", "wb") as f:
            f.write(file.read())
            f.close()

        return {"downloaded": drive}
    except HttpError as e:
        response.status_code = e.status_code
        return {"error": str(e)}
    except Exception as e:
        response.status_code = 500
        return {"error": str(e)}


@router.get("/download/folder/{folder_id}", summary="Download a folder")
async def downloadFolder(folder_id: str, response: Response, type: str | None = None):
    try:
        drive = service.files().list(q=f"'{folder_id}' in parents").execute()
        folder_info = service.files().get(fileId=folder_id).execute()

        files_folder = drive.get('files')
        if (files_folder == None or len(files_folder) == 0):
            response.status_code = 404
            return {"error": "Folder not found"}

        download_success = 0
        download_fail = 0

        # create folder
        import os
        if(not os.path.exists('./download/' + folder_info["name"])):
            os.mkdir('./download/' + folder_info["name"])

        # download files
        for file in files_folder:
            try:
                # check type
                if (checkGoogleTypeIsSupport(file["mimeType"])):
                    request = service.files().export_media(
                        fileId=file["id"], mimeType=convertTypeGoogleToApp(file["mimeType"]) if type == None else convertExtensionToApp(f".{type}"))
                elif (checkAppTypeIsSupport(file["mimeType"])):
                    request = service.files().get_media(fileId=file["id"])
                else:
                    download_fail += 1
                    continue

                f_io = io.BytesIO()
                downloader = MediaIoBaseDownload(f_io, request)
                done = False
                while done is False:
                    status, done = downloader.next_chunk()

                f_io.seek(0)

                with open(f"download/{folder_info["name"]}/{file["name"]}{convertTypeGoogleToExtension(file["mimeType"]) if type == None else (f".{type}")}", "wb") as f:
                    f.write(f_io.read())
                    f.close()
                download_success += 1
            except HttpError as e:
                download_fail += 1
            except:
                download_fail += 1

        return {"downloaded": drive, "download_success": download_success, "download_fail": download_fail, "download_unknown": len(files_folder) - download_success - download_fail}
    except HttpError as e:
        response.status_code = e.status_code
        return {"error": str(e)}
    except:
        response.status_code = 500
        return {"error": "Internal server error"}
