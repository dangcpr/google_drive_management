gg_type_support = ["application/vnd.google-apps.audio", "application/vnd.google-apps.document", "application/vnd.google-apps.spreadsheet",
                   "application/vnd.google-apps.presentation", "application/vnd.google-apps.video", "application/vnd.google-apps.file"]
app_type_support = ["audio/mpeg", "application/pdf", "text/csv", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "video/mp4", "application/octet-stream", "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-powerpoint", "image/png", "image/jpeg", "image/gif", "text/plain", "text/html", "application/xml", "application/json", "application/octet-stream", "application/zip", "application/vnd.ms-excel", "application/msword", "application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]


def convertTypeGoogleToApp(gg_drive_mine_type: str) -> str:
    match gg_drive_mine_type:
        case "application/vnd.google-apps.folder":
            return "application/zip"
        case "application/vnd.google-apps.audio":
            return "audio/mpeg"
        case "application/vnd.google-apps.document":
            return "application/pdf"
        case "application/vnd.google-apps.spreadsheet":
            return "text/csv"
        case "application/vnd.google-apps.presentation":
            return "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        case "application/vnd.google-apps.video":
            return "video/mp4"
        case _:
            return gg_drive_mine_type


def convertTypeGoogleToExtension(gg_drive_mine_type: str) -> str:
    match gg_drive_mine_type:
        case "application/vnd.google-apps.folder":
            return ".zip"
        case "application/vnd.google-apps.audio":
            return ".mp3"
        case "application/vnd.google-apps.document":
            return ".docx"
        case "application/vnd.google-apps.spreadsheet":
            return ".xlsx"
        case "application/vnd.google-apps.presentation":
            return ".pptx"
        case "application/vnd.google-apps.video":
            return ".mp4"
        case _:
            return ""


def checkGoogleTypeIsSupport(gg_drive_mine_type: str) -> bool:
    if (gg_drive_mine_type in gg_type_support):
        return True
    return False

def checkAppTypeIsSupport(app_type: str) -> bool:
    if (app_type in app_type_support):
        return True
    return False

def convertAppToExtension(app: str):
    match app:
        case "application/zip":
            return ".zip"
        case "audio/mpeg":
            return ".mp3"
        case "application/pdf":
            return ".pdf"
        case "text/csv":
            return ".csv"
        case "application/vnd.ms-powerpoint":
            return ".ppt"
        case "application/vnd.openxmlformats-officedocument.presentationml.presentation":
            return ".pptx"
        case "video/mp4":
            return ".mp4"
        case "application/msword":
            return ".doc"
        case "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            return ".docx"
        case "application/vnd.ms-excel":
            return ".xls"
        case "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            return ".xlsx"
        case "image/png":
            return ".png"
        case "image/jpeg":
            return ".jpg"
        case "image/gif":
            return ".gif"
        case "text/plain":
            return ".txt"
        case "text/html":
            return ".html"
        case "application/xml":
            return ".xml"
        case "application/json":
            return ".json"
        case "application/octet-stream":
            return ".bin"
        case _:
            return ".bin"

def convertExtensionToApp(extension: str) -> str:
    match extension:
        case ".zip":
            return "application/zip"
        case ".mp3":
            return "audio/mpeg"
        case ".pdf":
            return "application/pdf"
        case ".csv":
            return "text/csv"
        case ".ppt":
            return "application/vnd.ms-powerpoint"
        case ".pptx":
            return "application/vnd.openxmlformats-officedocument.presentationml.presentation"
        case ".mp4":
            return "video/mp4"
        case ".doc":
            return "application/msword"
        case ".docx":
            return "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        case ".xls":
            return "application/vnd.ms-excel"
        case ".xlsx":
            return "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        case ".png":
            return "image/png"
        case ".jpg":
            return "image/jpeg"
        case ".jpeg":
            return "image/jpeg"
        case ".gif":
            return "image/gif"
        case ".txt":
            return "text/plain"
        case ".html":
            return "text/html"
        case ".xml":
            return "application/xml"
        case ".json":
            return "application/json"
        case _:
            return "application/octet-stream"
