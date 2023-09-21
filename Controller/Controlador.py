from Model.TabelaSistema import TabelaSistema as TbS
from Model.TabelaPerfil import TabelaPerfil as TbP
from Model.TabelaUsuario import TabelaUsuario as TbU
from Model.TabelaUsuarioPerfil import TabelaUsuarioPerfil as TbUP
from Model.TabelaMatrizSod import TabelaMatrizSod as TbM
from Model.Loader import Loader
      #Package.Module        #Class


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
        
    


    def run(self):
        #Carregar todos os arquivos csv
        loader = Loader()
        self.loader = loader.AbrirConexaoBD()

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

        








