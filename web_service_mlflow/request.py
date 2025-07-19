import requests

ride = {
    'PULocationID' : 110,
    'DOLocationID' : 131,
    'trip_distance' : 39
}

url = 'http://localhost:5005/predict'
response = requests.post(url, json=ride)
try:
    print(response.json())
except requests.exceptions.JSONDecodeError:
    print(response)
    print("Raw Response Text:", response.text)
    print("Response is not valid JSON.")
#print(response.json())