import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://palashdhote.atlassian.net/rest/api/3/project"
api_token = "ATATT3xFfGF01jEFjanpmGgCAQU0b0mVgG5_CUAqnuY3AEpcmMZ3DFskyYgzWEQrfjVJ5k9oKCswt6Pai1HLfLrdACX2UhSfABYxJPoGBfbSuoPFya2HDDR5KbFNgutlYsPSQo0_QQTeGGzQso4AHCKG2smxlRZWmympOrPDb7KP_a7coSkDzJc=6153EF26"
auth = HTTPBasicAuth("palashdhote@gmail.com", api_token)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))