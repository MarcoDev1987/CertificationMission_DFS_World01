import psycopg2

class BD:
    def __init__(self):
        print('Método Construtor')

    def AbrirConexao(self):
        try:
            self.conexao = psycopg2.connect (database='CRUD', user = 'postgres',
                    password='admin3003', host = '127.0.0.1', port = '5432')
            print('Conexão bem sucedida com Banco de Dados!')
        except (Exception, psycopg2.Error) as error :
            if(self.conexao):
                print("Falha ao se conectar ao Banco de Dados", error)
    
    def CriarTabelas(self):
        try:
            self.AbrirConexao()
            cursor = self.conexao.cursor()                 #Codigo SERIAL PRIMARY KEY,
            cursor.execute(''' CREATE TABLE public."Produto"
                                (
                                Codigo INT PRIMARY KEY,     
                                Nome VARCHAR(30) NOT NULL,
                                Preco NUMERIC CHECK(preco > 0) NOT NULL  
                                ); ''')
            print('Tabela criada com sucesso!')
            self.conexao.commit()
            self.conexao.close()
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela preço")

    def geracaodeDadosFake(self):  #Create
        from faker import Faker
        #BD.AbrirConexao()
        self.AbrirConexao()
        cursor = self.conexao.cursor()
        fake = Faker('pt_BR')
        n = 10
        for i in range(n):
            Codigo = i+10
            Nome = 'produto_'+str(i+1)
            Preco = fake.pyfloat(left_digits =4, right_digits=2, positive=True,
                                 min_value = 5, max_value= 1000 )
            print(Preco)
            print(Nome)

            comandoSQL = ''' INSERT INTO public."Produto" (Codigo, Nome, Preco) 
            VALUES (%s, %s, %s)'''
            registro = (Codigo, Nome, Preco)
            cursor.execute(comandoSQL, registro)
        
        self.conexao.commit()
        self.conexao.close()

    def selecionarDados(self):
        try:
            self.AbrirConexao()
            cursor = self.conexao.cursor()

            print("Selecionando todos os produtos")
            sql_select_query = '''select * from public."Produto" '''

            cursor.execute(sql_select_query)
            registros = cursor.fetchall()
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
    
    def inserirDados(self, codigo, nome, preco):  #Create
        try:
            self.AbrirConexao()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."Produto"
                                    (Codigo, Nome, Preco) VALUES (%s, %s, %s) '''
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela Produto')
            return True
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Produto", error)
                return False
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')

    
    def atualizarDados(self, codigo, nome, preco): #Update
        try:
            self.AbrirConexao()
            cursor = self.conexao.cursor()

            print("Registro antes da atualização:")
            sql_select_query = ''' select * from public."Produto"
                                    where Codigo = %s'''
            cursor.execute(sql_select_query, (codigo,) )
            record = cursor.fetchone()
            print(record)

            #Atualizar registro:
            sql_update_query = ''' Update public."Produto" set
                                    Nome=%s, Preco = %s where
                                    Codigo = %s'''
            cursor.execute(sql_update_query, (nome, preco, codigo) )
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."Produto"
                                    where Codigo = %s'''
            cursor.execute(sql_select_query, (codigo,) )
            record = cursor.fetchone()
            print(record)   
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Produto", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')


    
    def excluirDados (self, codigo):
        try:
            self.AbrirConexao()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."Produto"
                                where Codigo = %s '''
            
            cursor.execute(sql_delete_query, (codigo, ))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro excluido com sucesso!')
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Erro de exclusão da tabela Produto", error)
        
        finally:
            if(self.conexao):
                cursor.close()
                self.conexao.close()
                print('A conexão foi encerrada com sucesso!')    



if __name__ == '__main__':
    Obj = BD()
    Obj.CriarTabelas()
    Obj.geracaodeDadosFake()







