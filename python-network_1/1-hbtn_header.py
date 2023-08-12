import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python script_name.py <url>")
    sys.exit(1)

url = sys.argv[1]
response = requests.get(url)

if response.status_code == 200:
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
    else:
        print("X-Request-Id header not found in the response.")
else:
    print(f"Failed to fetch URL. Status code: {response.status_code}")
