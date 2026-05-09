"""
storage.py — Persistent storage layer using local JSON files.
Data survives page reloads and session restarts.
"""
import json
import os
from datetime import datetime

STORAGE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
os.makedirs(STORAGE_DIR, exist_ok=True)

def _path(key: str) -> str:
    return os.path.join(STORAGE_DIR, f"{key}.json")

def save(key: str, data) -> None:
    try:
        with open(_path(key), "w", encoding="utf-8") as f:
            json.dump(data, f, default=str, indent=2)
    except Exception as e:
        print(f"[Storage] Save error for {key}: {e}")

def load(key: str, default=None):
    try:
        p = _path(key)
        if not os.path.exists(p):
            return default
        with open(p, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[Storage] Load error for {key}: {e}")
        return default

def append_record(key: str, record: dict) -> None:
    """Append a record to a list stored under key."""
    existing = load(key, default=[])
    if not isinstance(existing, list):
        existing = []
    record["_saved_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    existing.append(record)
    save(key, existing)

def delete(key: str) -> None:
    try:
        p = _path(key)
        if os.path.exists(p):
            os.remove(p)
    except Exception as e:
        print(f"[Storage] Delete error for {key}: {e}")

def list_keys() -> list:
    try:
        return [f.replace(".json", "") for f in os.listdir(STORAGE_DIR) if f.endswith(".json")]
    except Exception:
        return []
