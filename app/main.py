import os
import sys
import tomllib
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import requests


def load_config() -> dict:
    """載入設定，優先順序：環境變數 > config.toml"""
    api_key = os.getenv("OPENROUTER_API_KEY")
    name = os.getenv("OPENROUTER_NAME")

    config_path = Path("config.toml")
    if config_path.exists():
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
            openrouter = config.get("openrouter", {})
            if not api_key:
                api_key = openrouter.get("api_key")
            if not name:
                name = openrouter.get("name")

    return {"api_key": api_key, "name": name}


config = load_config()
OPENROUTER_API_KEY = config["api_key"]
OPENROUTER_NAME = config["name"]

if not OPENROUTER_API_KEY:
    print("錯誤：請設定 config.toml 或 OPENROUTER_API_KEY 環境變數", file=sys.stderr)
    sys.exit(1)

app = FastAPI()


@app.get("/")
async def read_index():
    return FileResponse("app/index.html")


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/api/usage")
def get_usage():
    url = "https://openrouter.ai/api/v1/auth/key"
    headers = {"Authorization": f"Bearer {OPENROUTER_API_KEY}"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        raise HTTPException(status_code=502, detail=f"無法連線至 OpenRouter: {e}")

    data = response.json().get("data", {})
    return {
        "name": OPENROUTER_NAME or data.get("label"),
        "limit_remaining": data.get("limit_remaining"),
        "usage": data.get("usage"),
        "usage_daily": data.get("usage_daily"),
    }
