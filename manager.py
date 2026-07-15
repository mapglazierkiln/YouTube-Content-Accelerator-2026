# Configuration module: manager

SETTINGS = {
    "nzywf": 13,
    "unqfxus": 943,
    "nxsea": 773,
    "qkmpsno": 280,
    "buarqf": 44,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
