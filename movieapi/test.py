import requests
import json

url = "http://127.0.0.1:8000/apimovies/"
headers = {'Content-Type': 'application/json'}

data = {
    "title": "The Shawshank Redemption",
    "release_date": "1994-09-23",
    "Description": "Frank Darabont's prison drama based on Stephen King's novella",
    "Certifications": "R"
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.status_code)
print(response.json())
