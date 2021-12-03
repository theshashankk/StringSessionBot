import os

ENVIRONMENT = os.environ.get('ENVIRONMENT', False)

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 2615662))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', 'f4ab3405e1518e49c3c6f19163981c60')
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5070352553:AAGjcg_NcckSvtoq3r3cAZnKQCM7ijzkfB0')
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', '@black_lightning_channel')
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 0
    API_HASH = ""
    BOT_TOKEN = ""
    DATABASE_URL = ""
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
    MUST_JOIN = ""
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN[1:]
