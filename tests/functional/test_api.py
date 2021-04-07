import time


def test_compute_ldc_independ(client):
    res = client.post("/process/data")
    location = res.headers.get("Location")
    timeout = time.time() + 15
    resp = None
    while time.time() < timeout:
        resp = client.get(location)
        if resp.status_code != 404:
            break
        time.sleep(5)
    assert not resp.json.get("result")


def test_compute_ldc_depend(client):
    res = client.post("/process/data1")
    location = res.headers.get("Location")
    timeout = time.time() + 15
    resp = None
    while time.time() < timeout:
        resp = client.get(location)
        if resp.status_code != 404:
            break
        time.sleep(5)
    assert resp.json.get("result") == [2]
