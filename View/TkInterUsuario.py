
import tkinter as tk
from tkinter import ttk


class TkUsuario:
    def __init__(self, win, controller):
        controller.loader
        self.objBD = controller.BdU
        #componentes
        self.lbCodigo=tk.Label(win, text='CPF(Pk):')
        self.lblNome=tk.Label(win, text='Nome do Funcionário')
        self.lblCodigo=tk.Label(win, text='Código do Sistema')
        self.lblPreco=tk.Label(win, text='Função:')

        self.txtCodigo=tk.Entry(win,)
        self.txtNome=tk.Entry(win,)
        self.txtCodigo2=tk.Entry(win,)
        self.txtPreco=tk.Entry(win,)
        

        self.btnCadastrar=tk.Button(win, text='Cadastrar Usuário', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)  

        
        
        



        #----- Componente TreeView --------------------------------------------
        
        self.dadosColunas = ("", "CPF(Pk)", "Nome do Usuário")            
                
        self.treeProdutos = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='left', fill ='x')
                                
        #self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeProdutos.heading("#0", text="")
        self.treeProdutos.heading("#1", text="CPF(Pk)")
        self.treeProdutos.heading("#2", text="Nome")
        

        self.treeProdutos.column("#0", width= 0)
        self.treeProdutos.column("#1", width= 180)
        self.treeProdutos.column("#2", width=180)
        
        self.treePerfil = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.treePerfil.heading("#0", text="")
        self.treePerfil.heading("#1", text="Código Sis.")
        self.treePerfil.heading("#2", text="Função")
        

        self.treePerfil.column("#0", width= 0)
        self.treePerfil.column("#1", width= 150)
        self.treePerfil.column("#2", width=150)

        self.treePerfil.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)

        self.treePerfil.place(relx = 0.57 , rely = 0.1, relwidth= 0.45, relheight= 0.45)
        
        
        
        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)                  
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.treeProdutos.place(relx = 0.01 , rely = 0.1, relwidth= 0.40, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)     
                                        
        
        self.lbCodigo.place( x=20, y=325)
        self.txtCodigo.place( x=80, y=325 , relwidth= 0.3)
        
        self.lblNome.place( x=20, y=375)
        self.txtNome.place( x=145, y=375 , relwidth= 0.32)
        
        # self.lblPreco.place( x=50, y=425)
        # self.txtPreco.place(x=250, y=425, relwidth= 0.50, relheight= 0.05)
               
        self.btnCadastrar.place( x=20, y=450)
        self.btnAtualizar.place( x=130, y=450)
        self.btnExcluir.place( x=200, y=450)
        self.btnLimpar.place( x=260, y=450)
    

    # Cadastro de Perfil/Sistema :
        self.treeProdutos.place(relx = 0.01 , rely = 0.1, relwidth= 0.55, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)


           
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            Cpf, Nome = item["values"][0:3]  
            self.txtCodigo.insert(0, Cpf)  
            self.txtNome.insert(0, Nome)  
              
#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              cpf=item[0]
              nome=item[1]
              
              print("Código = ", cpf)
              print("Nome = ", nome, "\n")
              
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(cpf,
                                           nome,))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar')            
#-----------------------------------------------------------------------------
#LerDados da Tela
#-----------------------------------------------------------------------------           
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          cpf = (self.txtCodigo.get())
          print('cpf', cpf)
          nome=self.txtNome.get()
          print('nome', nome)
        #   preco= str(self.txtPreco.get())          
        #   print('preco', preco)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return cpf, nome
    


#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          cpf, nome= self.fLerCampos()                    
          if (self.objBD.inserirDados(cpf, nome)):
             
            self.treeProdutos.insert('', 'end',
                                  iid=self.iid,                                   
                                  values=(cpf,
                                          nome))                        
            self.iid = self.iid + 1
            self.id = self.id + 1
            self.fLimparTela()
            print('Produto Cadastrado com Sucesso!')        

          else:
            print('Não foi possível fazer o cadastro.')
        except:
          print('Não foi possível fazer o cadastro.')
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------           
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          cpf, nome= self.fLerCampos()
          
          self.objBD.atualizarDados(cpf, nome)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Atualizado com Sucesso!')        
        except:
          print('Não foi possível fazer a atualização.')
          return False
#-----------------------------------------------------------------------------
#Excluir Produto
#-----------------------------------------------------------------------------                  
    def fExcluirProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          cpf, nome= self.fLerCampos()
          self.objBD.excluirDados(cpf)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do produto.')
#-----------------------------------------------------------------------------
#Limpar Tela
#-----------------------------------------------------------------------------                 
    def fLimparTela(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtCodigo.delete(0, tk.END)
          self.txtNome.delete(0, tk.END)
          self.txtPreco.delete(0, tk.END)
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')




