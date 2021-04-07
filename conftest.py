import os
from pandas import read_csv
import pytest
from app import create_app
from app.settings.dev_config import DevConfig


@pytest.fixture
def client(app):
    with app.app_context():
        yield app.test_client()


@pytest.fixture
def app():
    app = create_app(config=DevConfig())
    yield app


@pytest.fixture
def mocked_data(app):
    def wrapper(name="data", correct=True):
        file_path = app.config.get("STATIC_DIR")
        fn = f"{name}.csv" if correct else "incorrect_data.csv"
        return read_csv(os.path.join(file_path, fn))

    return wrapper
