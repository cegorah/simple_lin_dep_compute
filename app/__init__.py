import os
from flask import Flask
from flask_caching import Cache
from app.settings import BaseConfig
from typing import Callable

from app.repository.object_storage import AwsStorage
from app.repository.file_storage import FileRepo
from app.engine.compute_engine import LDComputation

path = os.path.dirname(__file__)

cache = Cache()
aws_storage = AwsStorage()
file_storage = FileRepo()
compute_engine = LDComputation()


def create_app(config=None):
    if not config:
        config = BaseConfig()
    app = Flask(__name__)
    app.config.from_object(config)
    app.config["STATIC_DIR"] = os.path.join(path, "static")
    if not app.config.get("AWS_ACCESS_KEY_ID"):
        file_storage.init_app(app)
    else:
        aws_storage.init_app(app)
    compute_engine.init_app(app)
    cache.init_app(app, config={"CACHE_TYPE": "simple"})
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp, url_prefix="/")
    return app
