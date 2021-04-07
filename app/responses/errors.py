from app.responses import BasicResponse


class NotFoundResponse(BasicResponse):
    default_status = 404

    def __init__(self, message=None):
        payload = {
            "error": message or "FileNotFound"
        }
        super().__init__(payload)


class BadFile(BasicResponse):
    default_status = 400

    def __init__(self, message=None):
        payload = {
            "error": message or "BadFile"
        }
        super().__init__(payload)


class InternalServerError(BasicResponse):
    default_status = 500

    def __init__(self, message=None):
        payload = {
            "error": message or "InternalServerError"
        }
        super().__init__(payload)


__all__ = ["InternalServerError", "BadFile", "NotFoundResponse"]
