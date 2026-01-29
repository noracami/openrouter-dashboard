# OpenRouter Dashboard 設計文件

## 概述

一個簡單的儀表板，用於監控 OpenRouter API 使用量。供內網使用，API Key 藏於後端。

## 技術棧

- **後端**：Python FastAPI + requests
- **前端**：HTML + Tailwind CSS（CDN）
- **部署**：Docker

## 功能需求

顯示以下資訊：
- API Key 標籤（label）
- 剩餘額度（limit_remaining）
- 今日消耗（usage_daily）
- 累積總消耗（usage）

## API 端點

| 端點 | 方法 | 說明 |
|------|------|------|
| `/` | GET | 前端頁面 |
| `/api/usage` | GET | 取得使用量資料 |
| `/health` | GET | 健康檢查 |

## 專案結構

```
openrouter-dashboard/
├── app/
│   ├── main.py          # FastAPI 後端
│   └── index.html       # 前端介面
├── docs/
│   └── plans/
│       └── 2026-01-29-openrouter-dashboard-design.md
├── Dockerfile
├── .dockerignore
└── requirements.txt
```

## 原規格修正項目

| 問題 | 修正 |
|------|------|
| `bootstrap.min.min.css` typo | 改用 Tailwind CSS |
| `return {...}, 500` 語法錯誤 | 使用 `HTTPException` |
| 無環境變數檢查 | 啟動時驗證 |
| 前端無錯誤處理 | 加入 `.catch()` |
| Dockerfile 用 root | 使用非 root 使用者 |
| 無 .dockerignore | 新增 |

## 執行方式

```bash
# 建立映像檔
docker build -t openrouter-dashboard .

# 啟動容器
docker run -d -p 8080:80 -e OPENROUTER_API_KEY="your_key" openrouter-dashboard
```

瀏覽器開啟 `http://localhost:8080` 即可使用。
