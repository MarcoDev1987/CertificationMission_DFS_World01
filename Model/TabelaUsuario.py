import psycopg2



class TabelaUsuario:
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
            cursor.execute(''' CREATE TABLE public."Usuario"
                                (
                                CPF VARCHAR(11) PRYMARY KEY,                                     
                                Nome VARCHAR(40) NOT NULL
                                  
                                ); ''')  #Codigo INT PRIMARY KEY,  Preco NUMERIC CHECK(preco > 0) NOT NULL
            print('Tabela criada com sucesso!')
            self.conexao.commit()
            self.conexao.close()
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela USUARIO")


    def selecionarDados(self):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Selecionando todos os USUARIOS")
            sql_select_query = '''select * from public."Usuario" '''

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
            return registros
            print(registros)
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Error in select operation", error)

        finally:  
            #closing database connection.
            cursor.close()
            self.conexao.close()
            print("A conexão com Banco de Dados foi fechada")
        return registros
    
    def inserirDados(self, cpf, nome):  #Create
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."Usuario"
                                    (CPF, Nome) VALUES (%s, %s) '''
            record_to_insert = (cpf, nome)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela Usuario')
            return True
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Usuario", error)
                return False
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    def atualizarDados(self, cpf, nome): #Update
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Registro antes da atualização:")
            sql_select_query = ''' select * from public."Usuario"
                                    where CPF = %s'''
            cursor.execute(sql_select_query, (cpf,) )
            record = cursor.fetchone()
            print(record)

            #Atualizar registro:
            sql_update_query = ''' Update public."Usuario" SET
                                    Nome=%s where CPF = %s;'''
            cursor.execute(sql_update_query, (nome, cpf))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."Usuario"
                                    where CPF = %s'''
            cursor.execute(sql_select_query, (cpf,) )
            record = cursor.fetchone()
            print(record)   
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Usuario", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')


    
    def excluirDados (self, cpf):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."Usuario"
                                where CPF = %s '''
            
            cursor.execute(sql_delete_query, (cpf,))
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











