import requests
import sys

if len(sys.argv) != 3:
    print("Usage: python script_name.py <url> <email>")
    sys.exit(1)

url = sys.argv[1]
email = sys.argv[2]

data = {'email': email}
response = requests.post(url, data=data)

if response.status_code == 200:
    print(response.text)
else:
    print(f"Failed to fetch URL. Status code: {response.status_code}")
