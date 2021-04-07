from flask.testing import Client


def test_process_correct_file(client: Client):
    res = client.post("/process/data")
    assert res.status_code == 202
    assert "Location" in res.headers.keys()


def test_process_not_found(client: Client):
    res = client.post("/process/data3")
    assert res.status_code == 404
    assert "File not found" in res.json.values()


def test_process_incorrect_file(client: Client):
    res = client.post("/process/incorrect_data")
    assert res.status_code == 400
    assert "BadFile" in res.json.values()


def test_not_found_task(client: Client):
    res = client.get("/task/123")
    assert res.status_code == 404
