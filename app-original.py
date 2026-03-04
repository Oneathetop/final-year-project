from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd

app = Flask(__name__)

rf_reg = joblib.load("models/regression_pipeline.pkl")
logreg_cls = joblib.load("models/classification_pipeline.pkl")

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict():
    data = request.get_json()
    X = pd.DataFrame([data])

    pred_g3 = float(rf_reg.predict(X)[0])
    pred_risk = str(logreg_cls.predict(X)[0])

    probs = logreg_cls.predict_proba(X)[0]
    classes = logreg_cls.classes_
    prob_map = {str(c): float(p) for c, p in zip(classes, probs)}

    return jsonify({
        "predicted_g3": round(pred_g3, 2),
        "predicted_risk": pred_risk,
        "risk_probabilities": prob_map
    })

@app.post("/predict_csv")
def predict_csv():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    df = pd.read_csv(file, sep=";")  # UCI uses ; separator

    # Add subject if missing (for math file)
    if "subject" not in df.columns:
        df["subject"] = "math"

    # Take first row only for demo (simple)
    row = df.drop(columns=["G3"], errors="ignore").iloc[0].to_dict()

    X = pd.DataFrame([row])

    pred_g3 = float(rf_reg.predict(X)[0])
    pred_risk = str(logreg_cls.predict(X)[0])

    probs = logreg_cls.predict_proba(X)[0]
    classes = logreg_cls.classes_
    prob_map = {str(c): float(p) for c, p in zip(classes, probs)}

    return jsonify({
        "used_row_index": 0,
        "predicted_g3": round(pred_g3, 2),
        "predicted_risk": pred_risk,
        "risk_probabilities": prob_map
    })

if __name__ == "__main__":
    app.run(debug=False)
