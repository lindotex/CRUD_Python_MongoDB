from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os


class Atualizar:
    def __init__(self) -> None:
        pass

    def atualizar():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        conexao = ConexaoMongoDB(host=db_url)
        conexao.conectar()


        print('Digite o nome a ser Atualizado:')
        nome = str(input())
        print(f'Deseja realmente atualizar os dados de {nome} no banco de dados? Y/N')
        res = str(input())
        print(f'Insira a nova Ocupacao para {nome}:')
        valor = str(input())
        novos_dados = {"ocupation": valor}

        if (res == 'y' or res == 'Y'):
            try:
                conexao.atualizar_documento('test',{"name":nome}, novos_dados)
                print(f'{nome} foi atualizado no banco de dados com sucesso!')
            except Exception as e:
                print('Nao foi possivel atualizar o usuario', e)
        else:
            print(f'O usuario {nome} nao foi atualizado no banco de dados')

        conexao.desconectar()