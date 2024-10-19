import requests
from dotenv import load_dotenv
import os

# Replace with your actual Steam Web API key
# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('API_KEY')
app_id = os.getenv('APP_ID')

url = f'http://api.steampowered.com/ISteamUserStats/GetNumberOfCurrentPlayers/v1/?appid={app_id}&key={api_key}'

response = requests.get(url)
data = response.json()

if response.status_code == 200:
    print(f"Current players: {data['response']['player_count']}")
else:
    print(f"Failed to fetch data: {response.status_code}")
