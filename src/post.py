
from datetime import datetime
from src.database.database import SQL


class Post:
    def __init__(self):
        self.idPost= 0
        self.titulo = ''
        self.descricao = ''
        self.date = ''
        self.idUsuario= 0
        self.sql = SQL()

    def inserir(self):
        sql = "INSERT INTO post (titulo, descricao, data, idUsuario) VALUES (%s, %s, %s,%s)"
        agora = datetime.now()
        self.date= agora.strftime('%Y-%m-%d %H:%M')
        post = (self.titulo, self.descricao, self.date, self.idUsuario)
        self.sql.insert(sql, post)

    def get_post(self, id):
        sql = "SELECT * FROM post WHERE idPost = (%s)"
        value = (id,)
        result = self.sql.get_object(sql, value)
        for item in result:
            self.idPost = item[0]
            self.titulo = item[1]
            self.descricao = item[2]
            print(item)

    def get_all(self):  # talvez precise estar antes de getpost
        sql = "SELECT * FROM post"
        result = self.sql.get_all(sql)
        for item in result:
            print(item)

    def excluir(self, id):
        sql = "DELETE FROM post WHERE idPost = " + str(id)
        self.sql.excluir(sql)    
    
    def atualizar(self):
        sql = "UPDATE post SET titulo = %s, descricao = %s where idpost = %s"
        values = (self.titulo, self.descricao, self.idPost)
        self.sql.atualizar(sql, values)
        
