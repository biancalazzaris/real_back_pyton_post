import settings
from src.user import Usuario
from src.post import Post
from src.comentario import Comments
import os


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    return 0


def menu():
    print("\n \n  SEJA BEM VINDO \n \n")
    print("ESCOLHA UMA DAS OPÇÕES \n \n")
    print("1- USUÁRIOS\n") 
    print("2- POST\n")
    print("3- COMENTÁRIOS\n \n")
    print("DIGITE QUALQUER OUTRO NÚMERO PARA SAIR\n \n")
    return 0

def menuUsuario():
    print("\n \n  MENU USUÁRIO\n \n")
    print("ESCOLHA UMA DAS OPÇÕES \n \n")
    print("1- Incluir \n") 
    print("2- Excluir \n")
    print("3- Alterar \n")
    print("4- Buscar usuário\n")
    print("5- Buscar todos os usuários \n")
    print("6- Atualizar a senha \n")
    print("DIGITE QUALQUER OUTRO NÚMERO PARA SAIR")
    return 0


def menuPost():
    print("\n \n MENU POST\n \n")
    print("ESCOLHA UMA DAS OPÇÕES \n \n")
    print("1- Incluir \n") 
    print("2- Excluir \n")
    print("3- Alterar \n")
    print("4- Buscar post \n")
    print("5- Buscar todos os posts \n")
    print("6- Buscar comentários do post \n")
    print("DIGITE QUALQUER OUTRO NÚMERO PARA SAIR")
    return 0


def menuComentario():
    print("\n \n MENU COMENTARIO\n \n")
    print("ESCOLHA UMA DAS OPÇÕES \n \n")
    print("1- Incluir \n") 
    print("2- Excluir \n")
    print("3- Alterar\n")
    print("4- Buscar comentario \n")
    print("5- Buscar todos os comentarios \n")
    print("6- Buscar comentários de um post\n")
    print("7- Buscar comentários de um usuario \n")
    print("DIGITE QUALQUER OUTRO NÚMERO PARA SAIR")
    return 0

def entrada_dados():
    continuar = True
    while(continuar):
        menu()
        opcao = int(input())
        if (opcao > 6 or opcao <= 0):
            continuar = False
            continue
        if ( opcao == 1):
            menuUsuario()
            opcaoUsuario()
            continue
        if (opcao == 2):
            menuPost()
            opcaoPost()
            continue
        if (opcao == 3):
            menuComentario()
            opcaoComentario()
            continue


def opcaoUsuario():
    opcao = int(input())

    if (opcao == 1):
        usuario = Usuario()
        usuario.nome = input('Digite o nome \n')
        usuario.senha = input('Digite a senha \n')
        usuario.login = input('Digite o login \n')
        usuario.email = input('Digite o e-mail \n')
        usuario.inserir()    
    if (opcao == 2):
        usuario=Usuario()
        id= int(input('Digite o ID do usuário para excluir \n'))
        usuario.excluir(id)
    if (opcao == 3):
        usuario = Usuario()
        usuario.idUsuario = int(input('Digite o ID do usuário que quer alterar\n'))
        usuario.nome = input('Digite o nome \n')
        usuario.senha = input('Digite a senha \n')
        usuario.login = input('Digite o login \n')
        usuario.email = input('Digite o e-mail \n')
        usuario.atualizar()    
    if (opcao == 4):
        usuario = Usuario()
        user = int(input('Digite o ID do usuário para buscar\n'))
        usuario.get_user(user)
    if (opcao == 5):
        usuario = Usuario()
        usuario.get_all()
    if (opcao == 6):
        usuario = Usuario()
        usuario.idUsuario = int(input('Digite o ID do usuário para alterar a senha\n'))
        usuario.senha = input('Digite a senha NOVA\n')
        usuario.atualizarSenha()  


def opcaoPost():
    opcao = int(input())

    if (opcao == 1):
        post= Post()
        post.idUsuario = int(input('Digite seu ID \n'))
        post.titulo = input('Digite o titulo do seu post\n')
        post.descricao = input('Descreva seu post \n')
        post.inserir()
        
    if (opcao == 2):
        post= Post()
        id= int(input('Digite o ID do post para excluir \n'))
        post.excluir(id)
        
    if (opcao == 3):
        post= Post()
        post.idPost = int(input('Digite o ID do Post que deseja alterar\n'))
        post.titulo = input('Digite o titulo do seu post\n')
        post.descricao = input('Descreva seu post \n')
        post.atualizar()    
    if (opcao == 4):
        post= Post()
        postagem = int(input('Digite o ID do usuário para buscar\n'))
        post.get_post(postagem)
    if (opcao == 5):
        post= Post()
        post.get_all()
    if (opcao == 6):
        coment = Comments()
        idPost = int(input('Informe o ID do post para ver os comentários \n'))
        coment.get_commentByPost(idPost)


def opcaoComentario():
    opcao = int(input())
    if (opcao == 1):
        coment = Comments()
        coment.idUsuario = int(input('Digite seu ID \n'))
        coment.idPost = int(input('Digite o ID do post para comentar\n'))
        coment.ds_comment = input('Escreva seu comentário \n')
        coment.incluir()
           
    if (opcao == 2):
        coment = Comments()
        id= int(input('Digite o ID do comentario para excluir \n'))
        coment.excluir(id)
        
    if (opcao == 3):
        coment = Comments()
        id= int(input('Digite o ID do Post que deseja alterar\n'))
        coment.idPost = int(input('Digite o ID do post para comentar\n'))
        coment.ds_comment = input('Escreva seu comentário \n')
        coment.atualizar()    
    if (opcao == 4):
        coment = Comments()
        id= int(input('Digite o ID do comentario para buscar\n'))
        coment.get_comment(id)
    if (opcao == 5):
        coment = Comments()
        coment.get_all()
    if (opcao == 6):
        coment = Comments()
        idPost = int(input('Informe o ID do post para ver os comentários \n'))
        coment.get_commentByPost(idPost)
    if (opcao == 7):
        coment = Comments()
        idusuario = int(input('Digite o ID do usuário para ver os comentários \n'))
        coment.get_commentByUsuario(idusuario)



entrada_dados()