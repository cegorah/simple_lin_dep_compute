class BaseStorageException(BaseException):
    def __init__(self):
        super().__init__()


class FileReadError(BaseStorageException):
    def __init__(self, message=None):
        self.message = message
        super().__init__()

    def __repr__(self):
        return self.message

    def __str__(self):
        return self.message


__all__ = ["FileReadError"]
