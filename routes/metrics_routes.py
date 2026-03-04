from flask import Blueprint, jsonify, render_template

metrics_bp = Blueprint("metrics", __name__)


@metrics_bp.get("/")
def home():
    return render_template("index.html")


@metrics_bp.get("/health")
def health():
    return jsonify({"status": "ok"})
