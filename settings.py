from dotenv import load_dotenv, find_dotenv  
import os 


try:
    load_dotenv(find_dotenv(raise_error_if_not_found=True))
    SECRET_KEY = os.environ.get("")
    DATABASE_MYSQ_HOST = os.environ.get("HOSTNAME")
    DATABASE_MYSQL_USER = os.environ.get("NOME_USUARIO")
    DATABASE_MYSQL_PASSWORD = os.environ.get("SENHA_DO_BANCO")
    DATABASE_MYSQL_DB = os.environ.get("NOME_DO_BANCO")

except Exception as e:
    print('É necessário criar o arquivo .env para continuar')

if __name__ == "__main__":
    print('settings.py file')
    # raise Exception("O arquivo .env não existe")
    print('database password: ' + DATABASE_MYSQL_PASSWORD)
