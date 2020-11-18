# import settings
from src.user import Usuario


def main():
    usuario = Usuario()
    usuario.get_all()
    # usuario.idUsuario = 2
    # usuario.nome = 'Bianca Lazzaris'
    # usuario.senha = 'abacateAgoraEModinha'
    # usuario.login = 'bianca.la'
    print('')
    usuario.get_user(3)
    print(usuario.nome)
    # usuario.inserir()
    # usuario.excluir(1)
    # usuario.atualizar()
    # usuario.get_all()
    # usuario.get_user(1)
    # print(usuario.nome)
    # print(settings.SECRET_KEY)


if __name__ == "__main__":
    main()
