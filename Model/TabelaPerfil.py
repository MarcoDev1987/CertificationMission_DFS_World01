import psycopg2



class TabelaPerfil:
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
            cursor.execute(''' CREATE TABLE public."PERFIS"
                                (
                                Codigo INT NOT NULL,                                     
                                Nome VARCHAR(30) NOT NULL,
                                Descricao VARCHAR(200) NOT NULL,
                                UNIQUE (Nome),                                
                                FOREIGN KEY (Codigo) REFERENCES public."SISTEMAS"(Codigo) ON DELETE CASCADE ON UPDATE CASCADE  
                                ); ''')  #Codigo INT PRIMARY KEY,  Preco NUMERIC CHECK(preco > 0) NOT NULL
            print('Tabela criada com sucesso!')
            self.conexao.commit()
            self.conexao.close()
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela PERFIS")

   

    def selecionarDados(self):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Selecionando todos os PERFIS")
            sql_select_query = '''select * from public."PERFIS" '''

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
    
    def inserirDados(self, codigo, nome, decricao):  #Create
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."PERFIS"
                                    (Codigo, Nome, Descricao) VALUES (%s, %s, %s) '''
            record_to_insert = (codigo, nome, decricao)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela Perfis')
            return True, ''
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Perfis", error)
                return (False, error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    def atualizarDados(self, codigo, nome, descricao): #Update
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Registro antes da atualização:")
            sql_select_query = ''' select * from public."PERFIS"
                                    where Nome = %s AND Codigo = %s'''
            cursor.execute(sql_select_query, (nome, codigo) )
            record = cursor.fetchone()
            print(record)

            #Atualizar registro:
            sql_update_query = ''' Update public."PERFIS" set
                                    Codigo=%s, Descricao = %s where
                                    Nome = %s AND Codigo = %s'''
            cursor.execute(sql_update_query, (codigo, descricao, nome, codigo) )
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."PERFIS"
                                    where Nome = %s'''
            cursor.execute(sql_select_query, (nome,) )
            record = cursor.fetchone()
            print(record)   
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela PERFIS", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')


    
    def excluirDados (self, nome, codigo):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."PERFIS"
                                where Nome = %s AND Codigo = %s '''
            
            cursor.execute(sql_delete_query, (nome, codigo ))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro excluido com sucesso!')
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Erro de exclusão da tabela PERFIS", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')    











