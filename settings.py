import os
from dotenv import load_dotenv, find_dotenv  # pip install -U python-dotenv

try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
    SECRET_KEY = os.environ.get("SECRET_KEY")
    DATABASE_MYSQ_HOST = os.environ.get("DATABASE_MYSQ_HOST")
    DATABASE_MYSQL_USER = os.environ.get("DATABASE_MYSQL_USER")
    DATABASE_MYSQL_PASSWORD = os.environ.get("DATABASE_MYSQL_PASSWORD")
    DATABASE_MYSQL_DB = os.environ.get("DATABASE_MYSQL_DB")

except Exception as e:
    print('É necessário criar o arquivo .env para continuar')

if __name__ == "__main__":
    # print('settings.py file')
    # raise Exception("O arquivo .env não existe"))
    print('database password: ' + DATABASE_MYSQL_PASSWORD)
