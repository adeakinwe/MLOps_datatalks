import requests

ride = {
    'PULocationID' : 20,
    'DOLocationID' : 31,
    'trip_distance' : 23
}

url = 'http://localhost:5005/predict'
response = requests.post(url, json=ride)
print(response.json())