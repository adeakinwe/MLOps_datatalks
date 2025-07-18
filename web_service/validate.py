import predict

ride = {
    'PULocationID' : 20,
    'DOLocationID' : 31,
    'trip_distance' : 23
}

features = predict.prepare_features(ride)

predict_ = predict.predict(features)
print(predict_)