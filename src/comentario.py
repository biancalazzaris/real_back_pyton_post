
from datetime import datetime
from src.database.database import SQL

class Comments:
    def __init__(self):
        self.idcomment = 0
        self.ds_comment = ''
        self.dateComment = ''
        self.sql = SQL()
        self.idPost= 0
        self.idUsuario = 0

    def incluir(self):
        sql = "INSERT INTO comments (idcomment, ds_comment, data, idusuario, idpost) VALUES (%s, %s, %s, %s, %s)"
        hr = datetime.now()
        self.dateComment = hr.strftime('%Y-%m-%d %H:%M')
        valores = ( self.idcomment, self.ds_comment, self.dateComment, self.idUsuario, self.idPost) 
        self.sql.insert(sql, valores)
        

    def excluir(self, id):
        sql = "DELETE FROM comments WHERE idComment = " + str(id)
        self.sql.excluir(sql)

    def atualizar(self):
        sql = "UPDATE post SET  descricao = %s where idcomment = %s"
        values = ( self.ds_comment, self.idcomment)
        self.sql.atualizar(sql, values)


    def get_all(self):
        sql = "SELECT * FROM comments"
        result = self.sql.get_all(sql)
        for item in result:
            print(item) 

    def get_comment(self, id):
        sql = "SELECT * FROM comments WHERE idcomment = (%s)"
        value = (id,)
        getcomment = self.sql.get_object(sql, value)
        for item in getcomment:
            print(item)

    def get_commentByPost(self, id):
        sql = "SELECT * FROM comments WHERE idPost = (%s)"
        value = (id,)
        getCom_post = self.sql.get_object(sql, value) 
        for item in getCom_post:
            print(item)


    def get_commentByUsuario(self, id):
        sql = "SELECT * FROM comments WHERE idusuario = (%s)"
        value = (id,)
        getCom_usuario = self.sql.get_object(sql, value) 
        for item in getCom_usuario:
            print(item)