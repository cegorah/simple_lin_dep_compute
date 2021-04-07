import logging

from flask import current_app, request, Response
from botocore.exceptions import ClientError

from app.errors import *
from app.routes import bp as main_bp
from app.responses.errors import *
from app.responses.responses import *

from app.repository import IRepo
from app.engine import IEngine

logger = logging.getLogger(__name__)


@main_bp.route("/task/<string:task_id>", methods=["GET"])
def get_task_result(task_id):
    try:
        compute_engine: IEngine = current_app.compute_engine
        res = compute_engine.task_result(task_id)
        return TaskDone(res)
    except KeyError:
        return NotFoundResponse("TaskNotFound")
    except Exception as e:
        logger.error(e)
        return InternalServerError()
main_bp.route("/process/<string:name>", methods=["POST"])
def process_file(name):
    try:
        file_repo: IRepo = current_app.file_repo
        timeout = current_app.config.get("TASK_RESULT_EXPIRED_SEC")
        compute_engine: IEngine = current_app.compute_engine
        filename = f"{name}.csv"
        df = file_repo.read_file(filename=filename)
        task_id = compute_engine.add_task(df, timeout=timeout)
        return Response(headers={"Location": f"{request.url_root}task/{task_id}"}, status=202)
    except FileReadError as e:
        logger.error(e)
        return BadFile()
    except ClientError as e:
        logger.error(e)
        error_code = e.response['Error']['Code']
        if error_code == '404':
            return NotFoundResponse("File not found")
    except FileNotFoundError as e:
        logger.error(e)
        return NotFoundResponse("File not found")
    except Exception as e:
        logger.error(e)
        return InternalServerError()
