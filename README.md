# api-mock

ESP32などの組み込み機器から利用することを想定した、検証用APIモックサーバーです。

実APIでは再現しづらい正常系・異常系を、ESP32側の接続先を固定したままモックサーバー側の設定変更だけで試せる環境を目指します。

## Requirements

- Python 3.11+

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

Windows PowerShellの場合は、仮想環境の有効化を以下のように行います。

```powershell
.venv\Scripts\Activate.ps1
```

## Run

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

`0.0.0.0` にbindするため、同一LAN上のESP32や別端末からアクセスできます。

## Health check

サーバーを起動した端末から確認する場合:

```bash
curl http://127.0.0.1:8000/health
```

レスポンス:

```json
{
  "status": "ok"
}
```

同一LAN上の別端末から確認する場合は、サーバーを起動している端末のLAN内IPアドレスを指定します。

```text
http://<server-ip>:8000/health
```

例:

```text
http://192.168.1.100:8000/health
```

OSのファイアウォールを有効にしている場合は、TCP 8000番ポートへのLAN内アクセスを許可してください。

## Test

```bash
python -m pytest
```

## Project structure

```text
api-mock/
├── app/
│   ├── __init__.py
│   └── main.py
├── mocks/
│   └── .gitkeep
├── tests/
│   └── test_health.py
├── pyproject.toml
└── README.md
```

`mocks/` は後続実装でJSON形式のモック定義を配置するために使用します。
