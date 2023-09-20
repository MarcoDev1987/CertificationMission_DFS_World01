
import tkinter as tk
from tkinter import ttk, messagebox


class TkMatrizsod:
    def __init__(self, win, controller):
        controller.loader
        self.objBD = controller.BdM
        self.objBD.CriarTabelas()
        #componentes
        self.lblSistemaA=tk.Label(win, text='Sistema A:')
        self.lblPerfilA=tk.Label(win, text='Perfil A')
        self.lblSistemaB=tk.Label(win, text='Sistema B:')
        self.lblPerfilB=tk.Label(win, text='Perfil B:')
        

        self.txtSistemaA=tk.Entry(win,)
        self.txtPerfilA=tk.Entry(win,)
        self.txtSistemaB=tk.Entry(win,)
        self.txtPerfilB=tk.Entry(win,)
       

        self.btnCadastrar=tk.Button(win, text='Cadastrar', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirProduto)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)  

        
        
        



        #----- Componente TreeView --------------------------------------------
        # self.dadosColunas = ("Sistema A", "Perfil A", "Sistema B", "Perfil B")
        self.dadosColunas = ("", "Sistema A", "Perfil A", "Sistema B","Perfil B")            
                
        self.treeProdutos = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.verscrlbar = ttk.Scrollbar(win,
                                        orient="vertical",
                                        command=self.treeProdutos.yview)        
        self.verscrlbar.pack(side ='left', fill ='x')
                                
        #self.treeProdutos.configure(yscrollcommand=self.verscrlbar.set)
        
        self.treeProdutos.heading("#0", text="")
        self.treeProdutos.heading("#1", text="Sistema A")
        self.treeProdutos.heading("#2", text="Perfil A")
        self.treeProdutos.heading("#3", text="Sistema B")
        self.treeProdutos.heading("#4", text="Perfil B")
        
        self.treeProdutos.column("#0", width= 1)
        self.treeProdutos.column("#1", width= 220)
        self.treeProdutos.column("#2", width=220)
        self.treeProdutos.column("#3", width= 220)
        self.treeProdutos.column("#4", width= 220)
        
        self.treeProdutos.pack(padx=10, pady=10)
        
        
        self.treeProdutos.bind("<<TreeviewSelect>>",
                               self.apresentarRegistrosSelecionados)                  
        #---------------------------------------------------------------------        
        #posicionamento dos componentes na janela
        #---------------------------------------------------------------------                
        self.treeProdutos.place(relx = 0.02 , rely = 0.05, relwidth= 0.95, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)     
                                        
        
        self.lblSistemaA.place( x=100, y=325)
        self.txtSistemaA.place( x=250, y=325, relwidth= 0.50, relheight= 0.05)
        
        self.lblPerfilA.place( x=100, y=375)
        self.txtPerfilA.place( x=250, y=375, relwidth= 0.50, relheight= 0.05)
        
        self.lblSistemaB.place( x=100, y=425)
        self.txtSistemaB.place(x=250, y=425, relwidth= 0.50, relheight= 0.05)

        self.lblPerfilB.place( x=100, y=475)
        self.txtPerfilB.place(x=250, y=475, relwidth= 0.50, relheight= 0.05)

        
               
        self.btnCadastrar.place( x=100, y=520)
        self.btnAtualizar.place( x=200, y=520)
        self.btnExcluir.place( x=300, y=520)
        self.btnLimpar.place( x=400, y=520)
                   
           
        self.carregarDadosIniciais()
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            SistemaA,PerfilA,SistemaB, PerfilB = item["values"][0:4]  
            self.txtSistemaA.insert(0, SistemaA)  
            self.txtPerfilA.insert(0, PerfilA)  
            self.txtSistemaB.insert(0, SistemaB)  
            self.txtPerfilB.insert(0, PerfilB)
            
#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              SistemaA=item[0]
              PerfilA=item[1]
              SistemaB=item[2]
              PerfilB=item[3]
              
              print("Sistema A = ", SistemaA)
              print("Perfil A = ", PerfilA)
              print("Sistema B  = ", SistemaB )
              print("Perfil B  = ", PerfilB,"\n" )
                                
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(SistemaA,
                                           PerfilA,
                                           SistemaB,
                                           PerfilB,
                                          ))                        
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
          SistemaA = int(self.txtSistemaA.get())
          print('Sistema A', SistemaA)
          PerfilA=self.txtPerfilA.get()
          print('Perfil A', PerfilA)
          SistemaB= str(self.txtSistemaB.get())          
          print('Sistema B', SistemaB)
          PerfilB= str(self.txtPerfilB.get())          
          print('Perfil B', PerfilB)
         
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return SistemaA, PerfilA, SistemaB, PerfilB
    


#-----------------------------------------------------------------------------
#Cadastrar Produto
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          SistemaA, PerfilA, SistemaB, PerfilB= self.fLerCampos()
          if (( SistemaA != "" and PerfilA != "" and SistemaB != "" and PerfilB != "") or (
             PerfilA == "" and PerfilA == "") ):
              Erro = ""
              Boolean, Erro = self.objBD.inserirDados(SistemaA, PerfilA, SistemaB, PerfilB)                    
              if (Boolean):
                
                self.treeProdutos.insert('', 'end',
                                      iid=self.iid,                                   
                                      values=(SistemaA,
                                              PerfilA,
                                              SistemaB,
                                              PerfilB,
                                              ))                        
                self.iid = self.iid + 1
                self.id = self.id + 1
                self.fLimparTela()
                print('Produto Cadastrado com Sucesso!')        

          else:
            print('Não foi possível fazer o cadastro.')
            messagebox.showerror (title= "Houve um erro ao fazer o cadastro da Matriz!", message= "Para o preenchimento correto da matriz Ou todos os campos devem ser preenchidos pois assim a segregação é entre Funções ou preencher somente os campos Sistemas pois assim se refere a segregação entre Sistemas")
        except:
          messagebox.showerror (title= "Houve um erro ao cadastrar o Sistema!", message= f"{Erro}") 
          print('Não foi possível fazer o cadastro.')
#-----------------------------------------------------------------------------
#Atualizar Produto
#-----------------------------------------------------------------------------           
    def fAtualizarProduto(self):
        try:
          print("************ dados dsponíveis ***********")        
          SistemaA, PerfilA, SistemaB, PerfilB= self.fLerCampos()
          self.objBD.atualizarDados(SistemaA, PerfilA, SistemaB, PerfilB)          
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
          SistemaA, PerfilA, SistemaB, PerfilB = self.fLerCampos()          
          self.objBD.excluirDados(SistemaA, PerfilA, SistemaB, PerfilB)
                    
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
          self.txtSistemaA.delete(0, tk.END)
          self.txtPerfilA.delete(0, tk.END)
          self.txtSistemaB.delete(0, tk.END)
          self.txtPerfilB.delete(0, tk.END)
          
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')


