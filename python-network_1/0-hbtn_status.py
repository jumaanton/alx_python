#!/usr/bin/python3
import requests

url = 'https://alu-intranet.hbtn.io/status'
response = requests.get(url)

if response.status_code == 200:
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
else:
    print("Error: Failed to fetch the URL. Status code:", response.status_code)
