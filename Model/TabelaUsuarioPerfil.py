import psycopg2



class TabelaUsuarioPerfil:
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
            cursor.execute(''' CREATE TABLE public."UsuarioPerfil"
                                (
                                CPF char(11) CHECK(LENGTH(CPF) >= 11),                                     
                                Codigo_Sistema INT NOT NULL,
                                Funcao  VARCHAR(30) NOT NULL,
                                PRIMARY KEY (CPF, Codigo_Sistema, Funcao),
                                FOREIGN KEY (CPF) REFERENCES public."Usuario"(CPF) ON DELETE CASCADE ON UPDATE CASCADE,
                                ); ''')
            print('Tabela UsuarioPerfil criada com sucesso!')
            self.conexao.commit()
            self.conexao.close()
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("falha ao criar a tabela USUARIOPerfil")


    def Obter_registros_CPF(self, cpf):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()

            print("Selecionando todos os perfis daquele usuário")
            sql_select_query = '''select Codigo_Sistema, Funcao FROM public."UsuarioPerfil"
                                    WHERE CPF = %s '''
            cpf = f"{cpf}".zfill(11)
            print(cpf)
            cursor.execute(sql_select_query, (cpf,) )
            #record = cursor.fetchone()
            
            registros = cursor.fetchall()
            print("Registros de Perfil Usuário:", registros)
            return registros
            
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Error in select operation", error)

        finally:  
            #closing database connection.
            cursor.close()
            self.conexao.close()
            print("A conexão com Banco de Dados foi fechada da MatrizSoD")
        return registros
    
    def inserirDados(self,cpf, codigo2, perfil):  #Create
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            postgres_insert_query = ''' INSERT INTO public."UsuarioPerfil"
                                    (CPF, Codigo_Sistema, Funcao) VALUES (%s, %s, %s) '''
            record_to_insert = (cpf, codigo2, perfil)
            cursor.execute(postgres_insert_query, record_to_insert)
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro inserido com sucesso na tabela Usuario Perfil')
            return True
        except (Exception, psycopg2.Error) as error:
            if(self.conexao):
                print("Falha ao inserir registro na tabela Usuario Perfil", error)
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
                                    Nome=%s where CPF = %s'''
            cursor.execute(sql_update_query, (nome, cpf))
            self.conexao.commit()
            count = cursor.rowcount
            print(count,'Registro atualizado com sucesso')
            print('Registro depois da Atualização')
            sql_select_query = ''' select * from public."UsuarioPerfil"
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


    
    def excluirDados (self, cpf, codigo2, perfil):
        try:
            self.AbrirConexaoBD()
            cursor = self.conexao.cursor()
            sql_delete_query = ''' DELETE from public."UsuarioPerfil"
                                where CPF= %s AND Codigo_Sistema = %s AND Funcao = %s '''
            
            cursor.execute(sql_delete_query, (cpf, codigo2, perfil))
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











