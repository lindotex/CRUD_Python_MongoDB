from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os

class Remover:
    def __init__(self) -> None:
        pass
    
    def remover():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        conexao = ConexaoMongoDB(host=db_url)
        conexao.conectar()
        print('Digite o nome a ser removido:')
        nome = str(input())
        print(f'Deseja realmente remover {nome} do banco de dados? Y/N')
        res = str(input())

        if (res == 'y' or res == 'Y'):
            try:
                conexao.remover_por_nome('test',nome)
                print(f'{nome} foi removido do banco de dados com sucesso!')
            except Exception as e:
                print('Nao foi possivel remover o usuario', e)
        else:
            print(f'O usuario {nome} nao foi removido do banco de dados')
        conexao.desconectar()
