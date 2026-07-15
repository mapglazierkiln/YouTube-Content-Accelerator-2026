# Configuration module: client

SETTINGS = {
    "kdfh": 887,
    "mwdiw": 157,
    "ivltze": 788,
}


def get(key, default=None):
    return SETTINGS.get(key, default)
