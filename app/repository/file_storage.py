import os
from pandas import DataFrame, read_csv
from typing import Union, BinaryIO, TextIO
from app.errors.file_store_error import FileReadError

from app.repository import IRepo


class FileRepo(IRepo):
    def __init__(self, file_dir: str = None):
        self.file_dir = file_dir

    def init_app(self, app):
        if not self.file_dir:
            self.file_dir = app.config.get("STATIC_DIR")
        app.file_repo = self

    def read_file(self, *, filename: str, **kwargs) -> DataFrame:
        try:
            return read_csv(os.path.join(self.file_dir, filename), header=kwargs.get("header", 0))
        except FileNotFoundError as e:
            raise e
        except Exception as e:
            raise FileReadError(e.__str__())

    def upload_file(self, *, filename: str, **kwargs):
        NotImplementedError()

    def download_file(self, *, filename: str, **kwargs) -> Union[BinaryIO, TextIO]:
        NotImplementedError()
