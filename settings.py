import os

from dotenv import load_dotenv

dot_env = os.path.join('.env')
load_dotenv(dotenv_path=dot_env)

PSQL_USER = os.getenv('PSQL_USER')
PSQL_PASSWORD = os.getenv('PSQL_PASSWORD')
