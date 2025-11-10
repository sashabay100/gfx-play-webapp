from src.config import load_config


def test_load_config():
    cfg = load_config()
    assert isinstance(cfg, dict)
    assert 'app' in cfg
