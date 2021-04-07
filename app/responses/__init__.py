import json
from flask import Response


class BasicResponse(Response):
    default_mimetype = "application/json"
    charset = "utf-8"
    default_status = 200

    def __init__(self, payload=None):
        super().__init__()
        self.set_data(json.dumps(payload))
