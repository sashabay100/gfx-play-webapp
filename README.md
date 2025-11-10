# GFX Play Bot

Telegram bot for case opening (GFX Play Bot) — scaffolded project.

Features included in this scaffold:
- Bot core using aiogram
- Config loader (YAML)
- Locale files (en/ru/de/fr)
- SQLite DB skeleton
- Case opening skeleton with configurable drop rates
- Admin command stubs

Quick start (Windows PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
copy .env.example .env
# Edit .env to set your BOT_TOKEN
python -m src.bot
```

See `configs/config.yaml` for configuration examples. Locales are in `locales/`.
