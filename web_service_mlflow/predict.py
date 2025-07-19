import pickle
from flask import Flask, request, jsonify
import mlflow
from mlflow.tracking import MlflowClient

with open('lin_reg_green_tripdata.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)

RUN_ID = 'ca613be92280409287899eaab84e698f'

from mlflow.tracking import MlflowClient

client = MlflowClient(tracking_uri="http://localhost:5001")
run = client.get_run("ca613be92280409287899eaab84e698f")
print(run.info)

MLFLOW_TRACKING_URI = 'http://localhost:5001'
mlflow.set_tracking_uri(f'{MLFLOW_TRACKING_URI}')
client = MlflowClient(tracking_uri=MLFLOW_TRACKING_URI)
path = client.download_artifacts(run_id=RUN_ID, path='preprocessor/models.preprocessor.b')

print(f'downloading dict_vectorizer to path {path}')

with open(path, 'rb') as f_in:
    dv = pickle.load(f_in)

logged_model = f'runs:/{RUN_ID}/models_xgboost_mlflow'

model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s %s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features

def predict(features):
    X = dv.transform(features)
    pred = model.predict(X)
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