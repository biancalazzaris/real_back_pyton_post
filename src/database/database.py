import mysql.connector  # python -m pip install mysql-connector-python
import settings


class SQL:
    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(
                host=settings.DATABASE_MYSQ_HOST,
                user=settings.DATABASE_MYSQL_USER,
                password=settings.DATABASE_MYSQL_PASSWORD,
                database=settings.DATABASE_MYSQL_DB
            )
            self.mycursor = self.mydb.cursor()
            # self.mycursor = self.mydb.cursor(dictionary=True)
        except:
            print('erro ao conectar ao banco de dados')

    def insert(self, sql, values):
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registros inseridos")

    def get_all(self, sql):
        self.mycursor.execute(sql)
        result = self.mycursor.fetchall()
        # print(type(result))
        return result

    def get_object(self, sql, value):
        self.mycursor.execute(sql, value)
        return self.mycursor.fetchall()

    def excluir(self, sql):
        self.mycursor.execute(sql)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registro excluido")

    def atualizar(self, sql, values):
        self.mycursor.execute(sql, values)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registros atualizados")

    def __del__(self):
        self.mycursor.close()
        self.mydb.close()
