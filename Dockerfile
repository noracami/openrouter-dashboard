FROM python:3.12-slim

WORKDIR /code

# 安裝 uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# 建立非 root 使用者
RUN useradd --create-home appuser

COPY pyproject.toml .
COPY app ./app

# 安裝依賴
RUN uv sync --no-dev

# 切換到非 root 使用者
USER appuser

ENV RELOAD=false

EXPOSE 80

CMD ["uv", "run", "python", "-m", "app"]
