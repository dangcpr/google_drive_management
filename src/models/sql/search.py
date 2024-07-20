from src.models.tables import models
from sqlalchemy.orm import Session


def log_search(db: Session, search_query: str, status_code: int):
    db_log_search = models.Search_History(search_query=search_query, status_code=status_code)
    db.add(db_log_search)
    db.commit()
    db.refresh(db_log_search)