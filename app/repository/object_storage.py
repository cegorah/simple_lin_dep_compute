import boto3
import logging
from pandas import DataFrame, read_csv
from typing import Union, BinaryIO, TextIO, Any

from app.repository import IRepo

logger = logging.getLogger(__name__)


class AwsStorage(IRepo):
    def __init__(self, **kwargs):
        self.s3_client = None
        if "bucket_name" in kwargs.keys():
            self.bucket_name = kwargs.pop("bucket_name")
        if kwargs:
            self.s3_client = boto3.resource(**kwargs)

    def init_app(self, app):
        if not self.bucket_name:
            self.bucket_name = app.config.get("AWS_BUCKET_NAME")
        if not self.s3_client:
            self.s3_client = boto3.resource('s3')
        assert self.bucket_name, "AWS_BUCKET_NAME has to be provided"
        app.file_repo = self

    def read_file(self, *, file_name: str, **kwargs) -> Any:
        data = DataFrame(self.s3_client.Object(self.bucket_name, file_name).get()['Body'].read())
        return data

    def download_file(self, *, file_name: str, **kwargs):
        NotImplementedError()

    def upload_file(self, *, file_name: str, **kwargs) -> Union[BinaryIO, TextIO]:
        NotImplementedError()
