from flask import Flask, render_template

from routes.metrics_routes import metrics_bp
from routes.predict_routes import predict_bp
from routes.insight_routes import insights_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(predict_bp)
    app.register_blueprint(insights_bp)

    @app.get("/")
    def home():
        return render_template("index.html")

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)
