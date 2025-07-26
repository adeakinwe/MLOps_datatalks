# virtual env
python3 -m venv mlflow-env
source mlflow-env/bin/activate
pip install --upgrade pip
pip install mlflow

# virtual env 
source mlflow-env/bin/activate
pip install ipykernel
python -m ipykernel install --user --name=mlflow-env --display-name "Experiment-tracking (mlflow-env)"

#backend url
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5001
#aws# mlflow server --backend-store-uri sqlite:///mlflow4.db --default-artifact-root s3://mlflow-ride-duration21-prediction-artifact-store --host 127.0.0.1 --port 5004

# virtual env (access to global packages)
python3 -m venv --system-site-packages mlflow-env
source mlflow-env/bin/activate
pip install --upgrade pip
pip install mlflow

# python 3.11 virtual environment
# Navigate to your project directory
cd ~/Projects/MLops_pipeline/

# Create a new virtual environment using Python 3.11
/usr/local/bin/python3.11 -m venv mlflow-311venv
source mlflow-311venv/bin/activate
pip install --upgrade pip
pip install ipykernel
python -m ipykernel install --user --name=mlflow-env --display-name "Experiment-tracking (mlflow311-venv)"
pip install mlflow
python -m mlflow ui --backend-store-uri sqlite:///mlflow.db --host 127.0.0.1 --port 5001
#aws mlflow server --backend-store-uri sqlite:///mlflow4.db --default-artifact-root s3://mlflow-ride-duration21-prediction-artifact-store --host 127.0.0.1 --port 5003

# serve gunicorn
gunicorn --bind=0.0.0.0:5005 predict_pipeline:app

# download dataset
curl -O "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2023-01.parquet"
