import random
from src.config import load_config

CONFIG = load_config()

def sample_from_weights(items):
    # items: list of dicts with 'weight' key
    total = sum(i.get('weight', 1) for i in items)
    r = random.uniform(0, total)
    upto = 0
    for it in items:
        w = it.get('weight', 1)
        if upto + w >= r:
            return it
        upto += w
    return items[-1]

def open_case(case_key: str):
    cases = CONFIG.get('cases', {})
    case = cases.get(case_key)
    if not case:
        raise KeyError('Case not found')
    item = sample_from_weights(case.get('items', []))
    return item
