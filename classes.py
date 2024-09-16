from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os
from prettytable import PrettyTable

class crud_python:
    def __init__(self) -> None:
        pass

    # CRUD - CREATE
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

      # CRUD - READ
    def exibir():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        conexao = ConexaoMongoDB(host=db_url)
        conexao.conectar()
        print("")
        conexao.quantidade_na_collection('test')
        print("")
        resultados = conexao.executar_query("test", {})
        
        
        if resultados:
                
            t = PrettyTable(['ID','Nome', 'Ocupacao'])
            for documento in resultados:
                
                _id = documento.get("_id","ID Nao encontrado")
                nome = documento.get("name", "Nome não encontrado")
                ocupacao = documento.get("ocupation", "Ocupação não encontrada")
                
                t.add_row([f"{_id}",f"{nome}", f"{ocupacao}"])
            
            print(t)
        else:
            print("Nenhum documento encontrado na coleção 'test'.")
        conexao.desconectar()

    # CRUD - UPDATE
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
 
    # CRUD - DELETE
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
