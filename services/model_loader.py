import joblib

from config import REGRESSION_MODEL_PATH, CLASSIFICATION_MODEL_PATH

regression_model = joblib.load(REGRESSION_MODEL_PATH)
classification_model = joblib.load(CLASSIFICATION_MODEL_PATH)
