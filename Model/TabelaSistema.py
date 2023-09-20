import psycopg2



class TabelaSistema:
    def __init__(self):
        print('Método Construtor')

    def AbrirConexaoBD(self):
        try:
            self.conexao = psycopg2.connect (database='CRUD', user = 'postgres',
                    password='admin3003', host = '127.0.0.1', port = '5432')
            print('Conexão bem sucedida com Banco de Dados!')
        except (Exception, psycopg2.Error) as error :
            if(self.conexao):
                print("Falha ao se conectar ao Banco de Dados", error)
    
    def CriarTabelas(self):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()                 #Codigo SERIAL PRIMARY KEY,
            cursor.execute(''' CREATE TABLE public."SISTEMAS"
                                (
                                Codigo INT CHECK (Codigo >= 100 AND Codigo <= 999),                                     
                                Nome_Sistema VARCHAR(30) NOT NULL,
                                PRIMARY KEY (Codigo)  
                                ); ''')  #Codigo INT PRIMARY KEY,  Preco NUMERIC CHECK(preco > 0) NOT NULL
            print('Tabela SISTEMAS criada com sucesso!')
            self.conexao.commit()
            self.conexao.close()
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela PERFIS")

   

    def selecionarDados(self):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Selecionando todos os SISTEMAS")
            sql_select_query = '''select * from public."SISTEMAS" '''

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            return registros
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Error in select operation", error)

        finally:  
            #closing database connection.
            cursor.close()
            self.conexao.close()
            print("A conexão com Banco de Dados foi fechada")
        return registros
    
    def inserirDados(self, codigo, nome):  #Create
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."SISTEMAS"
                                    (Codigo, Nome_Sistema ) VALUES (%s, %s) '''
            record_to_insert = (codigo, nome)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela SISTEMAS')
            return True, ''
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela SISTEMAS", error)
                return False, error
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    def atualizarDados(self, codigo, nome): #Update
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Registro antes da atualização:")
            sql_select_query = ''' select * from public."SISTEMAS"
                                    where Codigo = %s'''
            cursor.execute(sql_select_query, (codigo,) )
            record = cursor.fetchone()
            print(record)

            #Atualizar registro:
            sql_update_query = ''' Update public."SISTEMAS" set
                                    Nome_Sistema=%s where
                                    Codigo = %s'''
            cursor.execute(sql_update_query, (nome, codigo) )
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."SISTEMAS"
                                    where Nome_Sistema = %s'''
            cursor.execute(sql_select_query, (nome,) )
            record = cursor.fetchone()
            print(record)   
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela SISTEMAS", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')


    
    def excluirDados (self, nome, codigo):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."SISTEMAS"
                                where Nome_Sistema = %s AND Codigo = %s '''
            
            cursor.execute(sql_delete_query, (nome, codigo ))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro excluido com sucesso!')
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Erro de exclusão da tabela SISTEMAS", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')    
