from flask import Flask, render_template


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index() -> str:
        return render_template('index.html')

    @app.route('/health')
    def health() -> tuple[dict[str, str], int]:
        return {'status': 'ok'}, 200

    return app
