# OpenRouter Dashboard

OpenRouter API 使用量監控儀表板。

## 功能

- 顯示 API Key 標籤
- 剩餘額度
- 今日消耗
- 累積總消耗

## 需求

- Python 3.11+
- [uv](https://github.com/astral-sh/uv)（推薦）或 pip

## 設定

複製設定檔範本並填入 API Key：

```bash
cp config.toml.example config.toml
```

編輯 `config.toml`：

```toml
[openrouter]
api_key = "sk-or-v1-your-api-key"
name = "My API Key"  # 選填，自訂顯示名稱

[server]
port = 8000
```

API Key 從 https://openrouter.ai/keys 取得。

## 本地執行

```bash
uv run python -m app
```

開啟 http://localhost:8000

## Docker

```bash
docker build -t openrouter-dashboard .
```

**使用案例：**

```bash
# 預設 port 8000
docker run -p 8080:8000 -e OPENROUTER_API_KEY="sk-..." openrouter-dashboard

# 掛載 config.toml（port 從設定檔讀取）
docker run -p 8080:8000 -v $(pwd)/config.toml:/code/config.toml openrouter-dashboard

# 自訂 port（環境變數覆蓋 config.toml）
docker run -p 8080:3000 -e PORT=3000 -e OPENROUTER_API_KEY="sk-..." openrouter-dashboard
```

## 設定優先順序

| 設定項 | 優先順序 |
|--------|----------|
| API Key | `OPENROUTER_API_KEY` > `config.toml` |
| Name | `OPENROUTER_NAME` > `config.toml` > API 回傳值 |
| Port | `PORT` > `config.toml` > 8000 |
