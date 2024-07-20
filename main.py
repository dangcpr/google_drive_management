from fastapi import FastAPI
import src.controllers.drive as drive
import src.controllers.search as search
from src.init.tables import create_tables, drop_tables

app = FastAPI()

app.include_router(search.router)
app.include_router(drive.router)

if __name__ == '__main__':
    try:
        # drop_tables()
        create_tables()
        print("Tables created successfully.")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)