import pytest
from fastapi.testclient import TestClient

from event_ingest.main import app


@pytest.fixture
def client():
    return TestClient(app)


def test_healthz(client):
    r = client.get("/healthz")
    assert r.json()["status"] == "ok"
    assert r.status_code == 200
