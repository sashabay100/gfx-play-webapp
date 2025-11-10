import json
from pathlib import Path

class I18n:
    def __init__(self, locales_dir: str, default_lang: str = "en"):
        self.locales_dir = Path(locales_dir)
        self.default = default_lang
        self.cache = {}

    def load(self, lang: str):
        if lang in self.cache:
            return self.cache[lang]
        p = self.locales_dir / f"{lang}.json"
        if not p.exists():
            p = self.locales_dir / f"{self.default}.json"
        try:
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = {}
        self.cache[lang] = data
        return data

    def t(self, lang: str):
        return self.load(lang)
