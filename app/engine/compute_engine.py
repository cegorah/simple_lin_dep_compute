import uuid
import sympy

from pandas import DataFrame
from multiprocessing.pool import ThreadPool

from app.engine import IEngine

import logging
logger = logging.getLogger(__name__)


class LDComputation(IEngine):
    def __init__(self):
        self.__workers = ThreadPool(processes=4)
        from app import cache
        self.cache = cache

    def init_app(self, app):
        app.compute_engine = self

    def add_task(self, data: DataFrame, **kwargs) -> str:
        task_id = uuid.uuid4().hex
        cleaned_data = data.loc[:, (data.dtypes == "float64")]
        self.__workers.apply_async(self.compute, args=(cleaned_data, task_id, kwargs.get("timeout")))
        return task_id

    def compute(self, data: DataFrame, task_id: str, timeout=None):
        _, inds = sympy.Matrix(data.values).rref()
        cl_cnt = data.columns.shape[0]
        self.cache.set(task_id, [x for x in range(cl_cnt) if x not in inds], timeout=timeout)

    def task_result(self, task_id: str, **kwargs):
        res = self.cache.get(task_id)
        if not isinstance(res, list):
            raise KeyError
        return res

    @property
    def tasks_cnt(self):
        return self.__workers._taskqueue.qsize()
