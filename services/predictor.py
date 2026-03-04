import pandas as pd

from services.model_loader import regression_model, classification_model


def predict_single(input_dict):
    df = pd.DataFrame([input_dict])

    pred_g3 = float(regression_model.predict(df)[0])
    pred_risk = str(classification_model.predict(df)[0])

    probs = classification_model.predict_proba(df)[0]
    classes = classification_model.classes_
    prob_map = {str(c): float(p) for c, p in zip(classes, probs)}

    return {
        "predicted_g3": round(pred_g3, 2),
        "predicted_risk": pred_risk,
        "risk_probabilities": prob_map,
    }


def predict_batch(df):
    grade_preds = regression_model.predict(df)
    risk_preds = classification_model.predict(df)

    result = df.copy()
    result["predicted_g3"] = grade_preds
    result["predicted_risk"] = risk_preds

    return result
