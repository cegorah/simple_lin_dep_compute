from botocore.exceptions import ConnectTimeoutError, EndpointConnectionError
from app.engine.compute_engine import LDComputation
from app.repository.file_storage import FileRepo
from app.repository.object_storage import AwsStorage


def test_init_apps_filestor(app):
    comp = LDComputation()
    f_repo = FileRepo()
    comp.init_app(app)
    f_repo.init_app(app)
    assert isinstance(app.compute_engine, LDComputation)
    assert isinstance(app.file_repo, FileRepo)


def test_init_apps_aws(app):
    aws_repo = AwsStorage(bucket_name="my_bucket")
    try:
        aws_repo.init_app(app)
    except (ConnectTimeoutError, EndpointConnectionError):
        pass
    assert isinstance(app.file_repo, AwsStorage)
