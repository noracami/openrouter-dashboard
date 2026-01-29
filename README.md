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
# 建立映像檔
docker build -t openrouter-dashboard .

# 執行（二擇一）

# 方式一：環境變數
docker run -p 8080:80 -e OPENROUTER_API_KEY="sk-..." openrouter-dashboard

# 方式二：掛載設定檔
docker run -p 8080:80 -v $(pwd)/config.toml:/code/config.toml openrouter-dashboard
```

開啟 http://localhost:8080

## 設定優先順序

| 設定項 | 優先順序 |
|--------|----------|
| API Key | `OPENROUTER_API_KEY` > `config.toml` |
| Name | `OPENROUTER_NAME` > `config.toml` > API 回傳值 |
| Port | `PORT` > `config.toml` > 預設 8000 |
