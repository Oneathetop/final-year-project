import requests
import pandas as pd

# Load one real row from your dataset to avoid missing columns
df = pd.read_csv("student-mat.csv", sep=";")
df["subject"] = "math"

# IMPORTANT: use the exact feature columns your model expects.
# If your model was trained on combined df, it expects the same columns minus targets.
# We'll drop G3 (target) and keep everything else (including G1,G2).
sample = df.drop(columns=["G3"]).iloc[0].to_dict()

r = requests.post("http://127.0.0.1:5000/predict", json=sample)
print(r.status_code)
print(r.json())
