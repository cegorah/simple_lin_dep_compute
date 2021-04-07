import os
from app import path
from app.repository.file_storage import FileRepo
from app.errors.file_store_error import FileReadError


def test_read_existing_file():
    file_dir = os.path.join(path, 'static')
    fr = FileRepo(file_dir)
    fr.read_file(filename="data.csv")


def test_read_not_found():
    file_dir = os.path.join(path, 'static')
    fr = FileRepo(file_dir)
    try:
        fr.read_file(filename="data-NOT_FOUND.csv")
    except FileNotFoundError:
        pass


def test_read_error():
    file_dir = os.path.join(path, 'static')
    fr = FileRepo(file_dir)
    try:
        fr.read_file(filename="incorrect_data.csv")
    except FileReadError:
        pass
