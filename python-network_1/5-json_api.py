import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <letter>")
    sys.exit(1)

url = "http://0.0.0.0:5000/search_user"
letter = sys.argv[1]

data = {'q': letter}
response = requests.post(url, data=data)

try:
    response_data = response.json()
    if response_data:
        print("[{}] {}".format(response_data.get('id'), response_data.get('name')))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
    