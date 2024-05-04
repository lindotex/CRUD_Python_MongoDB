import pymongo
from pymongo import MongoClient

class ConexaoMongoDB:
    pymongo = pymongo
    MongoClient = MongoClient
    
    def __init__(self, host):
        self.host = host
        self.cliente = None
        self.db = None

    def conectar(self):
    
        try:
            # Estabelece a conexão com o servidor MongoDB
            self.cliente = pymongo.MongoClient(host=self.host)
            # Seleciona o banco de dados especificado
            self.db = self.cliente.get_database('Test')
            print("Conexão com MongoDB estabelecida com sucesso.")
        except pymongo.errors.ConnectionFailure as e:
            print("Erro ao conectar ao MongoDB:", e)

    def desconectar(self):
        if self.cliente:
            self.cliente.close()
            print("Conexão com MongoDB encerrada.")

    def executar_query(self, colecao, query):
        if not self.cliente:
            print("Erro: Não conectado ao MongoDB.")
            return None

        try:
            # Executa a query na coleção especificada
            resultado = self.db[colecao].find(query)
            return list(resultado)  # Retorna os resultados como uma lista de dicionários
        except Exception as e:
            print("Erro ao executar a query:", e)
            return None
        
    def inserir_documento(self, colecao, documento):
        if not self.cliente:
            print("Erro: Não conectado ao MongoDB.")
            return

        try:
            # Insere o documento na coleção especificada
            self.db[colecao].insert_one(documento)
            print("Documento inserido com sucesso.")
        except Exception as e:
            print("Erro ao inserir documento:", e)
    
    def obter_todos_elementos_como_tabela(self, colecao):
        if not self.cliente:
            print("Erro: Não conectado ao MongoDB.")
            return None

        try:
            # Obtém todos os elementos da coleção especificada
            resultado = self.db[colecao].find({})
            
            # Converte os resultados em um DataFrame do pandas
            df = pd.DataFrame(list(resultado))
            return df
        except Exception as e:
            print("Erro ao obter todos os elementos como tabela:", e)
            return None
    
    def atualizar_documento(self, colecao, filtro, novos_valores):
        if not self.cliente:
            print("Erro: Não conectado ao MongoDB.")
            return

        try:
            # Atualiza o documento na coleção com base no filtro especificado
            resultado = self.db[colecao].update_many(filtro, {"$set": novos_valores})
            
            # Verifica se os documentos foram atualizados com sucesso
            if resultado.modified_count > 0:
                print(f"{resultado.modified_count} documentos atualizados com sucesso.")
            else:
                print("Nenhum documento encontrado para atualizar.")
        except Exception as e:
            print("Erro ao atualizar documentos:", e)    

    def remover_por_nome(self, colecao, nome):
        if not self.cliente:
            print("Erro: Não conectado ao MongoDB.")
            return

        try:
            # Remove o documento da coleção com base no nome especificado
            resultado = self.db[colecao].delete_one({"name": nome})
            
            # Verifica se o documento foi removido com sucesso
            if resultado.deleted_count > 0:
                print(f"Documento com nome '{nome}' removido com sucesso.")
            else:
                print(f"Documento com nome '{nome}' não encontrado.")
        except Exception as e:
            print("Erro ao remover documento:", e)
    
    def quantidade_na_collection(self, colecao):
        if not self.cliente:
            print("Erro: Nao conectado ao MongoDB")
            return
        
        try:
            number = self.db[colecao].count_documents({})
            print(f'Quantidade de itens na colecao: {number} itens.')
        
        except Exception as e:
            print("Erro ao consultar o documento:", e)
            
        