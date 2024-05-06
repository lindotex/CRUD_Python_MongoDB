from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os
from prettytable import PrettyTable

class Exibir:
    def __init__(self) -> None:
        pass
    

    def exibir():
        load_dotenv(find_dotenv())
        db_url = os.environ.get('MONGO_URL')
        conexao = ConexaoMongoDB(host=db_url)
        conexao.conectar()
        print("")
        conexao.quantidade_na_collection('test')
        print("")
        resultados = conexao.executar_query("test", {})
        t = PrettyTable(['ID','Nome','Ocupacao'])
        if resultados:
            for documento in resultados:
                _id = documento.get("_id", "_Id não encontrado")
                nome = documento.get("name", "Nome não encontrado")
                ocupacao = documento.get("ocupation", "Ocupação não encontrada")
                t.add_row([_id,nome,ocupacao])
                # print(f"ID: {_id} | Nome:  {nome} | Ocupação: {ocupacao}")
            print(t)    
        else:
            print("Nenhum documento encontrado na coleção 'test'.")
        conexao.desconectar()   
    