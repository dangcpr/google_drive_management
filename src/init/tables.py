from models.tables import models
from init.db import engine


def create_tables():
    models.Base.metadata.create_all(bind=engine)

def drop_tables():
    models.Base.metadata.drop_all(bind=engine)