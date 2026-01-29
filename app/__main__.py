import os
import tomllib
from pathlib import Path

import uvicorn


def get_port() -> int:
    """取得 port，優先順序：環境變數 > config.toml > 預設值"""
    # 環境變數
    if port := os.getenv("PORT"):
        return int(port)

    # config.toml
    config_path = Path("config.toml")
    if config_path.exists():
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
            if port := config.get("server", {}).get("port"):
                return int(port)

    return 8000


if __name__ == "__main__":
    port = get_port()
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
