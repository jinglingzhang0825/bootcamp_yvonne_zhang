# Stage 13 Homework - Prediction API

This project serves a linear regression model trained on a synthetic two-feature regression dataset generated with scikit-learn.

The API predicts a continuous numeric target from two numeric input features.

## Running the API

From the homework13 folder, run:

    python app.py

The server starts at:

    http://127.0.0.1:5000

The model is loaded once from `model/model.pkl` when the application starts.

## POST /predict

Send two numeric features in a JSON body:

    curl -X POST http://127.0.0.1:5000/predict \
         -H "Content-Type: application/json" \
         -d '{"features": [0.1, 0.2]}'

Example response:

    {"prediction":23.58961171297328}

## GET /predict/<f1>/<f2>

The same prediction can be requested using URL path parameters:

    curl http://127.0.0.1:5000/predict/0.1/0.2

Example response:

    {"prediction":23.58961171297328}

## Bad Input

The API returns HTTP 400 with a JSON error message when input is invalid.

For example:

    curl http://127.0.0.1:5000/predict/abc/0.2

Response:

    HTTP 400

    {"error":"f1 and f2 must be numeric"}

For POST requests, the API also returns HTTP 400 if the `features` key is missing, contains the wrong number of values, or contains non-numeric values.
