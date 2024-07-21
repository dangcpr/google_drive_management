from fastapi import Depends, APIRouter, Response, logger
import requests
import constants.search as const
from sqlalchemy.orm import Session
from models.sql import search as sql
from init.db import get_db

router = APIRouter(
    prefix="/google/search",
    tags=["searchs"],
    responses={404: {"description": "Not found"}},
)

@router.get("")
async def search(query: str, response: Response, db: Session = Depends(get_db)):
    try:
        paramsGoogle = {
            'key': 'AIzaSyDew7qNRh7nx6E3YtiORIXbG8r9YUgmjaI',
            'cx': '9705f4d17ba1748d7',
            'q':query,
        }

        resGoogleSearch = requests.get(const.urlGoogleSearch, params=paramsGoogle).json()

        if (resGoogleSearch.get('error')):
            response.status_code = resGoogleSearch['error']['code']
            return {'error': resGoogleSearch['error']}
        else:
            # urlHtml = resGoogleSearch['items'][0]['link']
            # text = get_text_web.get_text_web(urlHtml)
            response.status_code = 200
            return resGoogleSearch
    except Exception as e:
        response.status_code = 500
        return {'error': str(e)}
    finally:
        sql.log_search(db, query, response.status_code)
