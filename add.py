from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os

class Adicionar:
    def __init__(self) -> None:
        pass

    
    def adicionar():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        conexao = ConexaoMongoDB(host=db_url)
        
        conexao.conectar()
        print('Digite o nome a ser inserido:')
        nome = str(input())
        print(f'Digite a ocupacao que {nome} possui:')
        ocupacao = str(input())
        documento = {"name":nome, "ocupation":ocupacao}

        conexao.inserir_documento('test',documento)
        print(f'{nome} foi adicionado ao banco de dados com sucesso!')
        conexao.desconectar()
