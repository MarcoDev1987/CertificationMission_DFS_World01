
import tkinter as tk
from tkinter import ttk


class TkPerfil:
    def __init__(self, win, controller):
        controller.loader
        self.objBD = controller.BdP
        #componentes
        self.lbCodigo=tk.Label(win, text='Código do Sistema:')
        self.lblNome=tk.Label(win, text='Nome do Perfil/Função')
        self.lblPreco=tk.Label(win, text='Descrição detalhada:')

        self.txtCodigo=tk.Entry(win,)
        self.txtNome=tk.Entry(win,)
        self.txtPreco=tk.Entry(win,)
        

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)  

        
        
        



        #----- Componente TreeView --------------------------------------------
        # self.dadosColunas = ("Código", "Nome", "Preço")
        self.dadosColunas = ("", "Codigo do Sistema(Fk)", "Nome(Pk)", "Descrição detalhada")            
                
        self.treeProdutos = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='left', fill ='x')
                                
        #self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeProdutos.heading("#0", text="")
        self.treeProdutos.heading("#1", text="Codigo do Sistema(Fk)")
        self.treeProdutos.heading("#2", text="Nome(Pk)")
        self.treeProdutos.heading("#3", text="Descrição detalhada")        

        self.treeProdutos.column("#0", width= 1)
        self.treeProdutos.column("#1", width= 200)
        self.treeProdutos.column("#2", width=200)
        self.treeProdutos.column("#3", width= 300)
        

        self.treeProdutos.pack(padx=10, pady=10)
        
        
        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)                  
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.treeProdutos.place(relx = 0.02 , rely = 0.1, relwidth= 0.95, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)     
                                        
        
        self.lbCodigo.place( x=100, y=325)
        self.txtCodigo.place( x=250, y=325)
        
        self.lblNome.place( x=100, y=375)
        self.txtNome.place( x=250, y=375)
        
        self.lblPreco.place( x=100, y=425)
        self.txtPreco.place(x=250, y=425, relwidth= 0.50, relheight= 0.05)
               
        self.btnCadastrar.place( x=100, y=500)
        self.btnAtualizar.place( x=200, y=500)
        self.btnExcluir.place( x=300, y=500)
        self.btnLimpar.place( x=400, y=500)
                   
           
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            Codigo,Nome,Preco = item["values"][0:3]  
            self.txtCodigo.insert(0, Codigo)  
            self.txtNome.insert(0, Nome)  
            self.txtPreco.insert(0, Preco)  
#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              codigo=item[0]
              nome=item[1]
              preco=item[2]
              print("Código = ", codigo)
              print("Nome = ", nome)
              print("Preço  = ", preco, "\n")
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(codigo,
                                           nome,
                                           preco))                        
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
          codigo = int(self.txtCodigo.get())
          print('codigo', codigo)
          nome=self.txtNome.get()
          print('nome', nome)
          preco= str(self.txtPreco.get())          
          print('preco', preco)
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return codigo, nome, preco
    


#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          codigo, nome, preco= self.fLerCampos()                    
          if (self.objBD.inserirDados(codigo, nome, preco)):
             
            self.treeProdutos.insert('', 'end',
                                  iid=self.iid,                                   
                                  values=(codigo,
                                          nome,
                                          preco))                        
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
          codigo, nome, preco= self.fLerCampos()
          
          self.objBD.atualizarDados(codigo, nome, preco)          
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
          codigo, nome, preco= self.fLerCampos()
          self.objBD.excluirDados(codigo)          
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




