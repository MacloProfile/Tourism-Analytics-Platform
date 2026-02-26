from flask import Flask
from app.config import Config
from app.db import db
from app.routers import register_routers

import threading

from app.utils.db_utils import wait_for_database
from scripts.auto_pipeline import start_watcher
from flask_swagger_ui import get_swaggerui_blueprint

from app.middleware.logger import request_logger


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    with app.app_context():
        wait_for_database(app)

    register_routers(app)

    # Swagger
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={"app_name": "Tourism Analytics API"}
    )

    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    # logger
    request_logger(app)

    # folder's watcher
    threading.Thread(
        target=start_watcher,
        args=(app,),
        daemon=True
    ).start()

    return app
