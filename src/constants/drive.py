from pathlib import Path
from dotenv import load_dotenv
from googleapiclient.discovery import build
from google.oauth2 import service_account, credentials as google_credentials

dotenv_path = Path('./src/env')
load_dotenv(dotenv_path=dotenv_path)

# ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
# REFRESH_TOKEN_SECRET = os.getenv("REFRESH_TOKEN_SECRET")

credentials = service_account.Credentials.from_service_account_file(
    '../src/credentials.json', scopes=['https://www.googleapis.com/auth/drive']
)
# gg_credentials = google_credentials.Credentials(ACCESS_TOKEN_SECRET, refresh_token=REFRESH_TOKEN_SECRET)
service = build("drive", "v3", credentials=credentials)
