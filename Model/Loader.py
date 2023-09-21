
import psycopg2

class Loader:

    def __init__(self):
        pass

    
    def AbrirConexaoBD(self):
        try:
            self.conexao = psycopg2.connect (database='CRUD', user = 'postgres',
                    password='admin3003', host = '127.0.0.1', port = '5432')
            print('Conexão bem sucedida com Banco de Dados!')
        except (Exception, psycopg2.Error) as error :
            if(self.conexao):
                print("Falha ao se conectar ao Banco de Dados", error)

    