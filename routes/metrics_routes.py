from flask import Blueprint, render_template
import json
import os

metrics_bp = Blueprint("metrics", __name__)

@metrics_bp.route("/metrics")
def metrics_page():

    metrics_path = os.path.join("models", "model_metrics.json")

    with open(metrics_path) as f:
        metrics = json.load(f)

    return render_template("metrics.html", metrics=metrics)