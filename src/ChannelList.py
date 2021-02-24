# -*- coding: utf-8 -*-
import json
import os
import sqlite3
import time
import psycopg2

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

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

    subscriptionsRequest = youtube.subscriptions().list(
        part="snippet,contentDetails",
        maxResults=2000,
        prettyPrint=True,
        mine=True
    )

    subscriptionsList = subscriptionsRequest.execute()

    for subscriptionItem in subscriptionsList["items"]:
        channelId = subscriptionItem['snippet']['resourceId']['channelId']

        channelRequest = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            prettyPrint=True,
            id=channelId
        )

        responseChannelInfo = channelRequest.execute()

        for item in responseChannelInfo['items']:

            name = item['snippet']['title']
            description = item['snippet']['description']
            publishedAt = item['snippet']['publishedAt']
            country = item['snippet']['country'] if 'country' in item['snippet'] else "NONE"
            videoUploads = item['statistics']['videoCount']
            subscribers = item['statistics']['subscriberCount']
            viewers = item['statistics']['viewCount']
            thumbnail = item['snippet']['thumbnails']['high']['url']

            timestamp = int(time.time() * 1000.0)

            print(">> Channel Name: {}\n".format(name))
            sqliteChannelCreate(conn, channelId, name, description,
                                country, videoUploads, subscribers, viewers, thumbnail,
                                publishedAt, timestamp, timestamp)
            print(">> -----------------------\n")


if __name__ == "__main__":
    main()
