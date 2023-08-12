import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <username> <personal_access_token>")
    sys.exit(1)

username = sys.argv[1]
personal_access_token = sys.argv[2]

url = "https://api.github.com/user"
headers = {
    "Authorization": f"Basic {username}:{personal_access_token}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    user_data = response.json()
    print("Your GitHub ID:", user_data.get('id'))
else:
    print(f"Failed to fetch user data. Status code: {response.status_code}")
