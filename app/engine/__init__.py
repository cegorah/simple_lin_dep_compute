from typing import Any
from abc import ABC, abstractmethod


class IEngine(ABC):
    @abstractmethod
    def add_task(self, data: Any, **kwargs) -> str: ...

    @abstractmethod
    def task_result(self, task_id: str, **kwargs) -> Any: ...
