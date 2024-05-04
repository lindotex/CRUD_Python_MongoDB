from dotenv import load_dotenv, find_dotenv
from conn import ConexaoMongoDB
import os
load_dotenv(find_dotenv())
db_url = os.environ.get('MONGO_URL')




conexao = ConexaoMongoDB(host=db_url)
conexao.conectar()
conexao.quantidade_na_collection('test')
