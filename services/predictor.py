from jaraco import classes
import pandas as pd

from services.model_loader import regression_model, classification_model

# Default values for features not provided by the user
DEFAULT_FEATURES = {
"G1":10,
"G2":10,
"absences":0,
"studytime":2,
"age":17,
"famrel":4,
"freetime":3,
"health":3,
"goout":3,
"failures":0
}

def predict_single(input_dict):

    data = DEFAULT_FEATURES.copy()
    data.update(input_dict)

    df = pd.DataFrame([data])

    # Ensure column order matches training
    df = df[regression_model.feature_names_in_]

    grade_prediction = regression_model.predict(df)[0]
    risk_prediction = classification_model.predict(df)[0]

    risk_probs = classification_model.predict_proba(df)[0]

    classes = classification_model.classes_

    probabilities = dict(zip(classes, risk_probs))

    return {
        "predicted_g3": round(float(grade_prediction), 2),
        "predicted_risk": risk_prediction,
        "risk_probabilities": probabilities
    }


def predict_batch(df):
    grade_preds = regression_model.predict(df)
    risk_preds = classification_model.predict(df)

    result = df.copy()
    result["predicted_g3"] = grade_preds
    result["predicted_risk"] = risk_preds

    return result
