import os
import requests
import pytest

BASE_URL = os.getenv("E2E_BASE_URL", "http://localhost:8080")

def test_app_is_up():
    """Vérifie que l'application répond sur /health."""
    resp = requests.get(f"{BASE_URL}/health", timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "healthy"

def test_index_endpoint():
    """Vérifie l'endpoint / et une fonctionnalité simple."""
    resp = requests.get(BASE_URL, timeout=5)
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "ok"
    assert "service" in data
    assert "version" in data
