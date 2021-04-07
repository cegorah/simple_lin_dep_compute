from app.responses import BasicResponse


class TaskDone(BasicResponse):
    def __init__(self, message=None):
        payload = {
            "result": message or []
        }
        super().__init__(payload)


class TaskAccepted(BasicResponse):
    default_status = 202

    def __init__(self, message=None, headers=None):
        payload = {
            "message": message or "TaskAccepted"
        }
        super().__init__(payload, headers=headers)


__all__ = ["TaskAccepted", "TaskDone"]
