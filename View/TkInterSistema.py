import tkinter as tk
from tkinter import messagebox, StringVar
from tkinter import ttk


class TkSistema:
    def __init__(self, win, controller):
        controller.loader
        self.objBD = controller.BdS
        self.objBD.CriarTabelas()
        #componentes
        self.lbCodigo=tk.Label(win, text='Código do Sistema:')
        self.lblNome=tk.Label(win, text='Nome do Sistema')
        

        
        
        def on_write(*args):
          s = var.get()
          if len(s) > 0:
              if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                  var.set(s[:-1])
              else: # aproveitar apenas os primeiros 5 chars
                  var.set(s[:max_len])

        
        max_len = 3 # maximo num de caracteres
        var = StringVar()
        var.trace("w", on_write) # rastrear valor da variavel e executar funcao de validacao quando mudar

        self.txtCodigo=tk.Entry(win, textvariable=var)
        
        self.txtNome=tk.Entry(win,)
       
        

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)  

        
        
        



        #----- Componente TreeView --------------------------------------------
        # self.dadosColunas = ("Código", "Nome", "Preço")
        self.dadosColunas = ("", "Codigo do Sistema", "Nome do Sistema")            
                
        self.treeSistemas = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeSistemas.yview)        
        self.verscrlbar.pack(side ='left', fill ='x')
                                
        #self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeSistemas.heading("#0", text="")
        self.treeSistemas.heading("#1", text="Codigo do Sistema")
        self.treeSistemas.heading("#2", text="Nome do Sistema")
        

        self.treeSistemas.column("#0", width= 1)
        self.treeSistemas.column("#1", width= 200)
        self.treeSistemas.column("#2", width=200)
        
        

        self.treeSistemas.pack(padx=10, pady=10)
        
        
        self.treeSistemas.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)                  
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.treeSistemas.place(relx = 0.02 , rely = 0.1, relwidth= 0.95, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)     
                                        
        
        self.lbCodigo.place( x=100, y=325)
        self.txtCodigo.place( x=250, y=325, relwidth= 0.25, relheight= 0.04 )
        
        self.lblNome.place( x=100, y=375)
        self.txtNome.place( x=250, y=375, relwidth= 0.25, relheight= 0.04)
        
        
               
        self.btnCadastrar.place( x=100, y=500)
        self.btnAtualizar.place( x=200, y=500)
        self.btnExcluir.place( x=300, y=500)
        self.btnLimpar.place( x=400, y=500)
                   
           
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeSistemas.selection():  
            item = self.treeSistemas.item(selection)  
            Codigo,Nome = item["values"][0:2]  
            self.txtCodigo.insert(0, Codigo)  
            self.txtNome.insert(0, Nome)  
             
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
              
              print("Código = ", codigo)
              print("Nome = ", nome)
              
                        
              self.treeSistemas.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(codigo,
                                           nome))                        
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
          codigo = str(self.txtCodigo.get())
          print('codigo', codigo)
          nome=self.txtNome.get()
          print('nome', nome)
          
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return codigo, nome
    


#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          
          print("************ dados dsponíveis ***********") 
          codigo, nome= self.fLerCampos()
          if(len(codigo) < 3):
            messagebox.showerror(title= "O Código do Sistema deve ser cadastrado com 3 digitos", message= "O Código do Sistema deve haver ter 3 digitos.")                     
          if(len(nome) == 0 ):
            messagebox.showerror(title= "O Nome do Sistema deve ter pelo menos 1 caracter", message= "O Nome do Perfil deve ter pelo menos 1 caracter.\n Revise o preenchimento dos campos.")                     
          else:
            Erro = ""
            Boolean, Erro = self.objBD.inserirDados(codigo, nome)
          
            if (Boolean):
                self.treeSistemas.insert('', 'end',
                                    iid=self.iid,                                   
                                    values=(codigo,
                                            nome))                        
                self.iid = self.iid + 1
                self.id = self.id + 1
                self.fLimparTela()
                print('Produto Cadastrado com Sucesso!')        

            elif(Erro != ''):
                messagebox.showerror (title= "Houve um erro ao cadastrar o Sistema!", message= f"{Erro}") 


            else:
                messagebox.showerror(title= "O Código do Sistema é Unico!", message= "Verifique se o Código inserido já está cadastrado na tabela.")
                print('Não foi possível fazer o cadastro.')
        except:
          print('Não foi possível fazer o cadastro.')
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------           
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          codigo, nome= self.fLerCampos()
          
          self.objBD.atualizarDados(codigo, nome)          
          #recarregar dados na tela
          self.treeSistemas.delete(*self.treeSistemas.get_children()) 
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
          codigo, nome= self.fLerCampos()
          self.objBD.excluirDados(nome, codigo)          
          #recarregar dados na tela
          self.treeSistemas.delete(*self.treeSistemas.get_children()) 
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
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')



   