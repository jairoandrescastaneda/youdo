import json
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

class YoutubeHttpClient:
    def __init__(self) -> None:
        self._api_service_name = "youtube"
        self._api_version = "v3"
        self._client_secrets_file = "client_secret.json"

    def connection(self) -> object:
        pass

def test():


    if os.path.isfile("credentials.json"):
        with open("credentials.json", 'r') as f:
            credentials_data = json.load(f)
        credentials = Credentials(credentials_data['token'])
    else:
        flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
        credentials = flow.run_console()
        credentials_data = {
            'token': credentials.token,
            'refresh_token': credentials.refresh_token,
            'token_uri': credentials.token_uri,
            'client_id': credentials.client_id,
            'client_secret': credentials.client_secret,
            'scopes': credentials.scopes
        }
        print(credentials_data)
        with open("credentials.json", 'w') as outfile:
            json.dump(credentials_data, outfile)

    youtube = build(api_service_name, api_version, credentials=credentials)