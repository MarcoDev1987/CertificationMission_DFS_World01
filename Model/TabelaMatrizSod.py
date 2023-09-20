import psycopg2



class TabelaMatrizSod:
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
            cursor = self.conexao.cursor()                    #Codigo SERIAL PRIMARY KEY,
            cursor.execute(''' CREATE TABLE public."Matrizsod"
                                (
                                CodigoA INT CHECK( CodigoA >= 100 AND CodigoA <= 999),                                     
                                FuncaoA VARCHAR(30),
                                CodigoB INT CHECK( CodigoB >= 100 AND CodigoB <= 999),
                                FuncaoB VARCHAR(30),
                                FOREIGN KEY (CodigoA) REFERENCES public."SISTEMAS" (Codigo) ON DELETE CASCADE ON UPDATE CASCADE,
                                FOREIGN KEY (CodigoB) REFERENCES public."SISTEMAS" (Codigo) ON DELETE CASCADE ON UPDATE CASCADE,
                                CONSTRAINT CColuna1 CHECK ((FuncaoA IS NULL AND FuncaoB IS NULL) OR (FuncaoA IS NOT NULL AND FuncaoB IS NOT NULL)),
                                PRIMARY KEY (FuncaoA, FuncaoB, CodigoA, CodigoB)
                                ); ''')  #Codigo INT PRIMARY KEY,  Preco NUMERIC CHECK(preco > 0) NOT NULL
            self.conexao.commit()
            self.conexao.close()
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela MATRIZsod")


    def selecionarDados(self):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Selecionando todos os MATRIZsod")
            sql_select_query = '''select * from public."Matrizsod" '''

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
    
    def inserirDados(self, codA, nomeA, codB, nomeB):  #Create
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."Matrizsod"
                                    (CodigoA, FuncaoA, CodigoB, FuncaoB ) VALUES (%s, %s, %s, %s) '''
            record_to_insert = ( codA, nomeA, codB, nomeB)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela Matrizsod')
            return True, ''
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Matrizsod", error)
                return False, error
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    
    def atualizarDados(self,codA, nomeA, codB, nomeB): #Update
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Registro antes da atualização:")
            sql_select_query = ''' select * from public."Matrizsod"
                                    where CodigoA = %s AND FuncaoA = %s AND CodigoB = %s '''
            cursor.execute(sql_select_query, (codA, nomeA, codB) )
            record = cursor.fetchone()
            print(record)

            #Atualizar registro:
            sql_update_query = ''' Update public."Matrizsod" SET
                                    FuncaoB = %s where CodigoA = %s AND FuncaoA = %s AND CodigoB = %s '''
            cursor.execute(sql_update_query, (nomeB, codA, nomeA, codB))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."Matrizsod"
                                    where CodigoA = %s AND FuncaoA = %s AND CodigoB = %s '''
            cursor.execute(sql_select_query, (codA, nomeA, codB))
            record = cursor.fetchone()
            print(record)   
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Matrizsod", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    
    def excluirDados (self, codA, nomeA, codB, nomeB):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."Matrizsod"
                                where CodigoA = %s AND FuncaoA = %s AND CodigoB = %s AND FuncaoB = %s'''
            
            cursor.execute(sql_delete_query, (codA, nomeA, codB, nomeB))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro excluido com sucesso!')
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Erro de exclusão da tabela Usuario", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')    




