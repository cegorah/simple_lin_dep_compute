from pandas import DataFrame
from typing import Union, TextIO, BinaryIO
from abc import ABC, abstractmethod


class IRepo(ABC):
    @abstractmethod
    def upload_file(self, *, filename: str, **kwargs): ...

    @abstractmethod
    def read_file(self, *, filename: str, **kwargs) -> DataFrame: ...

    @abstractmethod
    def download_file(self, *, filename: str, **kwargs) -> Union[BinaryIO, TextIO]: ...
