FROM python:3.13.2-slim-bullseye

WORKDIR /app

# Upgrade pip and install virtualenv
RUN pip install --upgrade pip

# Copy requirements first for cache efficiency
COPY requirements.txt .

# Create virtualenv
RUN python -m venv /opt/mlflow-env

# Install dependencies inside venv
RUN . /opt/mlflow-env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Make venv's binaries available system-wide
ENV PATH="/opt/mlflow-env/bin:$PATH"

# Copy app files
COPY predict.py lin_reg_green_tripdata.bin ./

# Expose port
EXPOSE 5005

# Run the app
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:5005", "predict:app"]