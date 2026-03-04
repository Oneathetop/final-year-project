from flask import Blueprint, jsonify, request

from services.predictor import predict_single
from utils.preprocessing_helpers import extract_feature_row, load_student_csv

predict_bp = Blueprint("predict", __name__)


@predict_bp.post("/predict")
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON payload"}), 400

    result = predict_single(data)
    return jsonify(result)


@predict_bp.post("/predict_csv")
def predict_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    if not file.filename:
        return jsonify({"error": "Empty filename"}), 400

    df = load_student_csv(file)
    row = extract_feature_row(df, row_index=0)
    if row is None:
        return jsonify({"error": "Empty CSV"}), 400

    result = predict_single(row)
    return jsonify({
        "used_row_index": 0,
        **result,
    })
