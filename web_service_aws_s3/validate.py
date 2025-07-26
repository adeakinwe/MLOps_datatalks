import predict

ride = {
    'PULocationID' : 59,
    'DOLocationID' : 34,
    'trip_distance' : 45
}

features = predict.prepare_features(ride)

predict_ = predict.predict(features)
print(predict_)