import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "models")

REGRESSION_MODEL_PATH = os.path.join(MODEL_DIR, "regression_pipeline.pkl")
CLASSIFICATION_MODEL_PATH = os.path.join(MODEL_DIR, "classification_pipeline.pkl")

CSV_SEPARATOR = ";"
DEFAULT_SUBJECT = "math"
TARGET_COLUMN = "G3"
