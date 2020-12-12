import hashlib
from src.database.database import SQL


class Usuario:
    def __init__(self):
        self.idUsuario = 0
        self.nome = ''
        self.login = ''
        self.senha = ''
        self.email = ''
        self.sql = SQL()

    def inserir(self):
        sql = "INSERT INTO usuario (nome, login, senha, email) VALUES (%s, %s, %s, %s)"
        self.senha = hashlib.md5(self.senha.encode('utf-8')).hexdigest()
        val = (self.nome, self.login, self.senha, self.email)
        self.sql.insert(sql, val)

        

    def get_all(self):
        sql = "SELECT * FROM usuario"
        result = self.sql.get_all(sql)
        for item in result:
            print(item)

    def get_user(self, id):
        sql = "SELECT * FROM usuario WHERE idUsuario = (%s)"
        value = (id,)
        result = self.sql.get_object(sql, value)
        for item in result:
            self.idUsuario = item[0]
            self.nome = item[1]
            self.login = item[2]
            self.senha = item[3]
            self.email = item[4]
        print(item)
        

    def excluir(self, id):
        sql = "DELETE FROM usuario WHERE idUsuario = " + str(id)
        self.sql.excluir(sql)

    def atualizar(self):
        sql = ''
        values = ()
        if self.senha != '':
            sql = "UPDATE usuario SET nome = %s, login = %s, senha = %s, email = %s where idusuario = %s"
            self.senha = hashlib.md5(self.senha.encode('utf-8')).hexdigest()
            values = (self.nome, self.login, self.senha, self.email, self.idUsuario)
            self.sql.atualizar(sql, values)
        else:
            sql = "UPDATE usuario SET nome = %s, login = %s, email = %s, where idusuario = %s"
            values = (self.nome, self.login, self.email, self.idUsuario)
            self.sql.atualizar(sql, values)

    def atualizarSenha(self):
        sql = ''
        values = ()
        sql = "UPDATE usuario SET senha = %s where idusuario = %s"
        self.senha = hashlib.md5(self.senha.encode('utf-8')).hexdigest()
        values = ( self.senha, self.idUsuario) 
        self.sql.atualizar(sql, values)



if __name__ == "__main__":
    print('class Usuario')
