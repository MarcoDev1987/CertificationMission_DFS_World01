from Model.TabelaSistema import TabelaSistema as TbS
from Model.TabelaPerfil import TabelaPerfil as TbP
from Model.TabelaUsuario import TabelaUsuario as TbU
from Model.TabelaUsuarioPerfil import TabelaUsuarioPerfil as TbUP
from Model.TabelaMatrizSod import TabelaMatrizSod as TbM
from Model.Loader import Loader
      #Package.Module        #Class
import View.Sistema as Sistema
       #Package.Module   #Call as Sistema
import View.Perfil as Perfil
import View.Usuario as Usuario
import View.MatrizSod as MatrizSod
from View.TkInterSistema import TkSistema
from View.TkInterPerfil import TkPerfil
from View.TkInterUsuario import TkUsuario
from View.TkMatrizsod import TkMatrizsod




class Controlador:

    def __init__(self) -> None:
        self.lista_sistemas = []
        self.lista_perfis = []
        self.lista_usuarios = []
        self.lista_matrizsod = []
        self.BdM = TbM()
        self.BdS = TbS()        
        self.BdP = TbP()        
        self.BdU = TbU()        
        self.BdUP = TbUP()
        
    # def comparar_matrizsod(self, cpf, codigo2, perfil):
        
    #         self.registros_usr = self.BdUP.Obter_registros_CPF(cpf)
    #         self.registros_usr = list(self.registros_usr)
    #         self.registros_matriz = self.BdM.selecionarDados()
    #         self.registros_matriz = list(self.registros_matriz)
    #         print(self.registros_matriz)
    #         print(self.registros_usr)
    #         condicao = 0
    #         for registro in self.registros_usr:
    #             for linha_matriz in self.registros_matriz:
    #                 if (linha_matriz[1] == 0 and registro[1] in linha_matriz and codigo2 in linha_matriz) :  #Comparação entre Sistemas
    #                     print("não é possível fazer o cadastro")
    #                     condicao = 1
    #                     #return False
                        
    #                 if (registro[1] in linha_matriz and registro[2] in linha_matriz and 
    #                     codigo2 in linha_matriz and perfil in linha_matriz):
    #                     print("não é possível fazer o cadastro")
    #                     condicao = 1
    #                     #return False
                        
    #         if condicao == 0:
    #             #return True
        


    def run(self):
        #Carregar todos os arquivos csv
        loader = Loader()
        self.loader = loader.AbrirConexaoBD()

# -------------------------- Carregamento de Sistemas  -----------------------------#
        self.Df_Sistemas = loader.load('./Model/Sistemas.csv') 
        for n in range(self.Df_Sistemas.shape[0]) :
            self.codigo = self.Df_Sistemas['Código'][n]
            self.nome = self.Df_Sistemas['Nome'][n]
            sistema = Sistema.Sistema()
            sistema.setCodigo(self.codigo)
            sistema.setNome(self.nome)
            self.lista_sistemas.append(sistema) # A lista sistemas irá adicionar a lista o objeto sistema
        
       

# -------------------------- Carregamento de Perfis  -----------------------------#
        self.Df_Perfis = loader.load('./Model/Perfis.csv') 
        for n in range(self.Df_Perfis.shape[0]) :
            self.codigo = self.Df_Perfis['Código'][n]
            self.nome = self.Df_Perfis['Nome'][n]
            self.descricao = self.Df_Perfis['Descrição'][n]
            perfil = Perfil.Perfil()
            perfil.setCodigo(self.codigo)
            perfil.setNome(self.nome)
            perfil.setDescricao(self.descricao)
            self.lista_perfis.append(perfil) # A lista sistemas irá adicionar a lista o objeto sistema
        
        


# -------------------------- Carregamento de Usuários  -----------------------------#
        self.Df_Usuarios = loader.load('./Model/Usuarios.csv') 
        for n in range(self.Df_Usuarios.shape[0]) :
            self.cpf = self.Df_Usuarios['CPF'][n]
            self.nome = self.Df_Usuarios['Nome'][n]
            self.codigo = self.Df_Usuarios['Código'][n]
            self.perfil = self.Df_Usuarios['Nome do Perfil'][n]
            usuario = Usuario.Usuario()
            usuario.setCpf(str(self.cpf))
            usuario.setNome(self.nome)            
            usuario.addSistemaPerfil(self.codigo, self.perfil)
            self.lista_usuarios.append(usuario) # A lista sistemas irá adicionar a lista o objeto sistema
        
        

# -------------------------- Carregamento da Matriz SoD  -----------------------------#
        self.Df_Matriz = loader.load('./Model/MatrizSod.csv') 
        for n in range(self.Df_Matriz.shape[0]) :
            self.codigoA = self.Df_Matriz['Código-A'][n]
            self.perfilA = self.Df_Matriz['Nome do Perfil-A'][n]
            self.codigoB = self.Df_Matriz['Código-B'][n]
            self.perfilB = self.Df_Matriz['Nome do Perfil-B'][n]
            matriz = MatrizSod.MatrizSod()
            matriz.setCodigoA(self.codigoA)
            matriz.setPerfilA(self.perfilA)            
            matriz.setCodigoB(self.codigoB)
            matriz.setPerfilB(self.perfilB)
            self.lista_matrizsod.append(matriz) # A lista sistemas irá adicionar a lista o objeto sistema
        

    # -------------------------- Carregamento do Banco de Dados  -----------------------------#    
        
        




#Programa Principal
#-----------------------------------------------------------------------------          
        import tkinter as tk
        from tkinter import Frame
        from tkinter import ttk
        


        janela = tk.Tk()
        janela.title(" Missão Certificação:")
        janela.geometry("1080x610+170+60")
        nb = ttk.Notebook(janela)
        nb.place(x=10,y=10, relwidth=0.98 , relheight=0.98)
        


        tb1 = Frame(nb)
        tb2 = Frame(nb)
        tb3 = Frame(nb)
        tb4 = Frame(nb)

        nb.add(tb1,text="  Cadastro de Usuários/Perfis   ")
        nb.add(tb2,text="  Cadastro de Perfis            ")
        nb.add(tb3,text="  Cadastro de Sistemas          ")
        nb.add(tb4,text="  Cadastro da Matriz Sod        ")

        
        TkPerfil(tb2, self)
        TkUsuario(tb1, self)
        TkSistema(tb3, self)
        TkMatrizsod(tb4, self)

        
        

        janela.mainloop()

        
#-----------------------------------------------------------------------------

        # while True:
        #     print("Menu:")
        #     print("(1) Listar Perfis")
        #     print("(2) Listar Sistemas")
        #     print("(3) Listar Matriz Sod")
        #     print("(4) Listar Usuários")
        #     print("(5) Adicionar novo perfil ao Usuário")
        #     print("(0) Para sair")

        #     escolha = int(input())
        #     if escolha == 0:
        #         break
        #     match escolha:
        #         case 1:
        #             for n in self.lista_perfis:
        #                 print(n.getCodigo(), n.getNome(), n.getDescricao())

        #         case 2:
        #             for n in self.lista_sistemas:
        #                 print(n.getCodigo(), n.getNome())

        #         case 3:
        #             for n in self.lista_matrizsod:
        #                 print(n.getCodigoA(), n.getPerfilA(), n.getCodigoB(), n.getPerfilB() )

        #         case 4:
        #             for n in self.lista_usuarios:
        #                 lista_aux = n.getSistemaPerfil()
        #                 print(n.getCpf(), n.getNome(), lista_aux[0], lista_aux[1] )
                        
                        
        #         case 5:
        #             print("Informe o Cpf do usuário:")
        #             usr = str(input())
        #             usr = "'" + f'{usr:12}' + "'"
                    
                    
        #             linha = self.Df_Usuarios.loc[self.Df_Usuarios['CPF'] == f'{usr}' ]
        #             indice = self.Df_Usuarios.index[self.Df_Usuarios['CPF'] == f'{usr}' ].tolist()
        #             if len(linha) == 0 :
        #                 print("Não foi encontrado usuário com este CPF")

        #             else:
        #                 print(indice)
        #                 indice = indice[0]
        #                 usr_select = self.lista_usuarios[indice]
        #                 print(f'''Usuário {linha['Nome'][0]} de CPF {linha['CPF'][0]}, tem os perfis:
        #                        {linha['Nome do Perfil'][0]} Com código do Sistema {linha['Código'][0]}''')

        #                 print("Informe agora o novo Perfil")
        #                 novo_perfil = str(input())
        #                 codigo_perfil = 300  # criar um dicionário entre perfil e codigo
        #                 #print(usr_select.addSistemaPerfil(codigo_perfil, novo_perfil))
        #                 if novo_perfil in usr_select.getSistemaPerfil():
        #                     print('O Usuário já tem este perfil cadastrado')
        #                     pass


        #                 else:

        #                     lista = usr_select.getSistemaPerfil()
        #                     linhas_matriz = self.Df_Matriz.values.tolist()
        #                     parada = 0
        #                     for item in lista:
        #                         for line in linhas_matriz:
        #                             # print (f" linha da matriz {line}")
        #                             # print( f"item da lista já cadastrado {item}")
        #                             if item in line and novo_perfil in line: 
        #                                 print(f"O perfil {novo_perfil} não é permitido ser cadastrado pois está em conflito de interesse com perfil já cadastrado anteriormente {item}")
        #                                 parada = 1
        #                                 break
                                        
        #                             elif item in line and codigo_perfil in line:
        #                                 print(f"O perfil {novo_perfil} não é permitido o cadastro pois está em conflito de interesse entre sistemas")                       
        #                                 parada = 1
        #                                 break      
                                        

        #                     if parada == 0:                    
        #                         print(usr_select.addSistemaPerfil(codigo_perfil, novo_perfil))
        #                         print(usr_select.getSistemaPerfil())
        #                     else:
        #                         pass

                              
                        
                        









