import pandas as pd

from services.model_loader import regression_model, classification_model

# Default values for features not provided by the user
DEFAULT_FEATURES = {
    "school": "GP",
    "sex": "M",
    "age": 17,
    "address": "U",
    "famsize": "GT3",
    "Pstatus": "T",
    "Medu": 2,
    "Fedu": 2,
    "Mjob": "other",
    "Fjob": "other",
    "reason": "course",
    "guardian": "mother",
    "traveltime": 2,
    "studytime": 2,
    "failures": 0,
    "schoolsup": "no",
    "famsup": "yes",
    "paid": "no",
    "activities": "no",
    "nursery": "yes",
    "higher": "yes",
    "internet": "yes",
    "romantic": "no",
    "famrel": 4,
    "freetime": 3,
    "goout": 3,
    "Dalc": 1,
    "Walc": 1,
    "health": 3,
    "absences": 0,
    "G1": 10,
    "G2": 10,
    "subject": "math",
}

def predict_single(input_dict):

    data = DEFAULT_FEATURES.copy()
    data.update(input_dict)

    df = pd.DataFrame([data])

    # Ensure column order matches training
    df = df[regression_model.feature_names_in_]

    grade_prediction = regression_model.predict(df)[0]
    risk_prediction = classification_model.predict(df)[0]

    return {
        "predicted_g3": round(float(grade_prediction), 2),
        "predicted_risk": risk_prediction
    }


def predict_batch(df):
    grade_preds = regression_model.predict(df)
    risk_preds = classification_model.predict(df)

    result = df.copy()
    result["predicted_g3"] = grade_preds
    result["predicted_risk"] = risk_preds

    return result
