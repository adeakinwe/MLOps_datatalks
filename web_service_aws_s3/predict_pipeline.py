import pickle
from flask import Flask, request, jsonify
import mlflow
from mlflow.tracking import MlflowClient

MLFLOW_TRACKING_URI = 'http://localhost:5004'
RUN_ID = '16b9d6323465410db3f39d3e3b849a60'

mlflow.set_tracking_uri(f'{MLFLOW_TRACKING_URI}')


logged_model = f'runs:/{RUN_ID}/models_xgboost_mlflow'

model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s %s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    pred = model.predict(features)
    return pred[0]

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride = request.get_json()

    features = prepare_features(ride)
    pred = predict(features)

    result = {
        'duration' : float(pred),
        'model_version' : RUN_ID
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5005)