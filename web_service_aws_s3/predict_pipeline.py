import pickle
from flask import Flask, request, jsonify
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient

MLFLOW_TRACKING_URI = 'http://localhost:5004'
RUN_ID = '79d08684e9e441dfbc066847af4de142'

mlflow.set_tracking_uri(f'{MLFLOW_TRACKING_URI}')


#logged_model = f'runs:/{RUN_ID}/model_pipeline' # uncomment if you want the run via mlflow tracking server
logged_model = f's3://mlflow-ride-duration21-prediction-artifact-store/1/{RUN_ID}/artifacts/model_pipeline' #connected directly to model pipeline logged to aws s3 bucket
model = mlflow.sklearn.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s %s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    pred = model.predict(features)
    return float(pred[0])

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