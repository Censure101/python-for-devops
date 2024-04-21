# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://palashdhote.atlassian.net//rest/api/3/project"

API_TOKEN="ATATT3xFfGF01jEFjanpmGgCAQU0b0mVgG5_CUAqnuY3AEpcmMZ3DFskyYgzWEQrfjVJ5k9oKCswt6Pai1HLfLrdACX2UhSfABYxJPoGBfbSuoPFya2HDDR5KbFNgutlYsPSQo0_QQTeGGzQso4AHCKG2smxlRZWmympOrPDb7KP_a7coSkDzJc=6153EF26"

auth = HTTPBasicAuth("palashdhote@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)