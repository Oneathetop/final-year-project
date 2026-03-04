from flask import Flask

from routes.metrics_routes import metrics_bp
from routes.predict_routes import predict_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(metrics_bp)
    app.register_blueprint(predict_bp)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=False)
