import yaml
import os
from pathlib import Path

CONFIG_PATH = Path(__file__).resolve().parents[1] / "configs" / "config.yaml"

def load_config(path: str = None):
    p = Path(path) if path else CONFIG_PATH
    if not p.exists():
        return {}
    with open(p, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)
