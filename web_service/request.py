import requests

ride = {
    'PULocationID' : 110,
    'DOLocationID' : 131,
    'trip_distance' : 39
}

url = 'http://localhost:5005/predict'
response = requests.post(url, json=ride)
print(response.json())