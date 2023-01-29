import os.path
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

USER_DB = os.getenv('USER_DB')
PASSWORD_DB = os.getenv('PASSWORD_DB')
HOST_DB = os.getenv('HOST_DB')
PORT_DB = os.getenv('PORT_DB')
DIALECT_DB = os.getenv('DIALECT_DB')
NAME_DB = os.getenv('NAME_DB')

databases_url = (
    f'{DIALECT_DB}+pymysql://{USER_DB}:{PASSWORD_DB}@{HOST_DB}:{PORT_DB}/'
    f'{NAME_DB}?charset=utf8'
)


def _config():
    return {
        'host': HOST,
        'port': PORT,
        'databases': {
            'databases_url': databases_url,
            'user_db': USER_DB,
            'password_db': PASSWORD_DB,
            'host_db': HOST_DB,
            'port_db': PORT_DB,
            'dialect_db': DIALECT_DB,
            'name_db': NAME_DB,
        }
    }


CONFIG = _config()
