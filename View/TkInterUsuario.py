import pandas as pd
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class TkUsuario:
    def __init__(self, win, controller):
        controller.loader
        self.objBD = controller.BdU
        self.objBD.CriarTabelas()
        self.objBD2 = controller.BdUP
        self.objBD2.CriarTabelas()
        self.objBD3 = controller.BdM
        
        #componentes
        self.lbCodigo=tk.Label(win, text='CPF(Pk):')
        self.lblNome=tk.Label(win, text='Nome do Funcionário:')
        self.lblCodigo=tk.Label(win, text='Código do Sistema:')
        self.lblPerfil=tk.Label(win, text='Função:')

        


        


        def on_write(*args):
          s = var.get()
          if len(s) > 0:
              if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                  var.set(s[:-1])
              else: # aproveitar apenas os primeiros 5 chars
                  var.set(s[:11])

        def on_write3(*args):
          s = var2.get()
          if len(s) > 0:
              if not s[-1].isdigit(): # retirar ultimo caracter caso nao seja digito
                  var2.set(s[:-1])
              else: # aproveitar apenas os primeiros 5 chars
                  var2.set(s[:3])
        
        
        var = StringVar()
        var.trace("w", on_write) # rastrear valor da variavel e executar funcao de validacao quando mudar

        
        var2 = StringVar()
        var2.trace("w", on_write3) # rastrear valor da variavel e executar funcao de validacao quando mudar


        self.txtCodigo=tk.Entry(win, textvariable=var)
        
        self.txtNome=tk.Entry(win, )
        self.txtCodigo2=tk.Entry(win, textvariable=var2)
        self.txtPreco=tk.Entry(win,)
        self.txtPerfil=tk.Entry(win,)
        

        self.btnCadastrar=tk.Button(win, text='Cadastrar Usuário', command=self.fCadastrarProduto)        
        self.btnAtualizar=tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)        
        self.btnExcluir=tk.Button(win, text='Excluir', command=self.fExcluirUsuario)        
        self.btnLimpar=tk.Button(win, text='Limpar', command=self.fLimparTela)  

        self.btnCadastrarPS=tk.Button(win, text='Cadastrar Perfil/Sistema', command=self.fCadastrarPerfil)
        self.btnLimpar2=tk.Button(win, text='Limpar', command=self.fLimparTela2)
        self.btnExcluirPS=tk.Button(win, text='Excluir Perfil/Sistema', command=self.fExcluirPerfil)
        



        #----- Componente TreeView --------------------------------------------
        
        self.dadosColunas = ("", "CPF", "Nome do Usuário")       
        self.dadosColunas2 = ("", "Codigo do Sistema", "Perfil")       
                
        self.treeProdutos = ttk.Treeview(win, height= 4, 
                                       columns=self.dadosColunas,
                                       selectmode='browse')
        
        self.treePerfil = ttk.Treeview(win, height= 4, 
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
                               self.apresentarRegistrosSelecionados2)

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

        self.lblCodigo.place( relx=0.65, y=325)
        self.txtCodigo2.place( relx= 0.65, y=346 , relwidth= 0.3)
        
        
        self.lblPerfil.place( relx=0.65, y=377)
        self.txtPerfil.place(relx= 0.65, y=396 , relwidth= 0.34)
               
        self.btnCadastrar.place( x=20, y=450)
        self.btnAtualizar.place( x=130, y=450)
        self.btnExcluir.place( x=200, y=450)
        self.btnLimpar.place( x=260, y=450)

        self.btnCadastrarPS.place(relx= 0.60, y=450)
        self.btnLimpar2.place( relx=0.75, y=450)
        self.btnExcluirPS.place(relx= 0.82, y=450)
    

    # Cadastro de Perfil/Sistema :
        self.treeProdutos.place(relx = 0.01 , rely = 0.1, relwidth= 0.55, relheight= 0.45)
        self.verscrlbar.place( relwidth= 0.98, rely=50, relheight= 0.45)


           
        self.carregarDadosIniciais()
        
#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados(self, event):  
        self.fLimparTela()  
        for selection in self.treeProdutos.selection():  
            item = self.treeProdutos.item(selection)  
            
            cpf, Nome = item["values"][0:2]
            cpf = f"{cpf}".zfill(11)
            print(cpf)
            self.txtCodigo.insert(0, cpf )
            self.txtNome.insert(0, Nome)

            self.fLimparTela2() 
            if (len(cpf) == 11):
                self.treePerfil.delete(*self.treePerfil.get_children())
                self.id2 = 0
                self.iid2 = 0
                registros2 = self.objBD2.Obter_registros_CPF(cpf)
                print("************ dados dsponíveis no BD PerfilUsuario ***********")        
                for item2 in registros2:
                    #cpf=item[0]
                    codigo2=item2[0]
                    codigo2 = f"{codigo2}".zfill(3)
                    perfil=item2[1]
                    print("Cpf = ", cpf)
                    print("Código = ", codigo2)
                    print("Função = ", perfil, "\n")
                    
                            
                    self.treePerfil.insert('', 'end',
                                        iid=self.iid2,                                  
                                        values=(codigo2,
                                                perfil,))                        
                    self.iid2 = self.iid2 + 1
                    self.id2 = self.id2 + 1
            print('Dados da Base')
        
                  

#-----------------------------------------------------------------------------
    def apresentarRegistrosSelecionados2(self, event):  
        
        self.fLimparTela2()

        for selection in self.treePerfil.selection():  
            item = self.treePerfil.item(selection)  
            
            codigo2, perfil = item["values"][0:2]
            codigo2 = f"{codigo2}".zfill(3)
             
            
            print(codigo2)
            print(perfil)
            
            self.txtCodigo2.insert(0, codigo2) 
            self.txtPerfil.insert(0, perfil)


#-----------------------------------------------------------------------------
    def carregarDadosIniciais(self):
        try:
          self.id = 0
          self.iid = 0          
          registros= self.objBD.selecionarDados()
          print("************ dados dsponíveis no BD ***********")        
          for item in registros:
              cpf=item[0]
              cpf = f"{cpf}".zfill(11)
              nome=item[1]
              
              print("Cpf = ", cpf)
              print("Nome = ", nome, "\n")
              
                        
              self.treeProdutos.insert('', 'end',
                                   iid=self.iid,                                   
                                   values=(cpf,
                                           nome,))                        
              self.iid = self.iid + 1
              self.id = self.id + 1

              self.treePerfil.delete(*self.treePerfil.get_children())
              self.id2 = 0
              self.iid2 = 0
              registros2 = self.objBD2.Obter_registros_CPF(cpf)
              print("************ dados dsponíveis no BD PerfilUsuario ***********")        
              for item2 in registros2:
                #cpf=item[0]
                codigo2=item2[0]
                codigo2 = f"{codigo2}".zfill(3)
                perfil=item2[1]
                print("Cpf = ", cpf)
                print("Código = ", codigo2)
                print("Função = ", perfil, "\n")
                
                        
                self.treePerfil.insert('', 'end',
                                    iid=self.iid2,                                  
                                    values=(codigo2,
                                            perfil,))                        
                self.iid2 = self.iid2 + 1
                self.id2 = self.id2 + 1
              


          print('Dados da Base')        
        except:
          print('Ainda não existem dados para carregar')            
#-----------------------------------------------------------------------------

    def carregarDadosIniciaisPerfil(self, cpf):
      self.id2 = 0
      self.iid2 = 0
      registros2 = self.objBD2.Obter_registros_CPF(cpf)
      print("************ dados dsponíveis no BD PerfilUsuario ***********")        
      for item2 in registros2:
        #cpf=item[0]
        codigo2=item2[0]
        codigo2 = f"{codigo2}".zfill(3)
        perfil=item2[1]
        print("Cpf = ", cpf)
        print("Código = ", codigo2)
        print("Função = ", perfil, "\n")
        
                
        self.treePerfil.insert('', 'end',
                            iid=self.iid2,                                  
                            values=(codigo2,
                                    perfil,))                        
        self.iid2 = self.iid2 + 1
        self.id2 = self.id2 + 1
   
#LerDados da Tela 
#-----------------------------------------------------------------------------           
    def fLerCampos(self):
        try:
          print("************ dados dsponíveis ***********") 
          cpf = str(self.txtCodigo.get())
          print('cpf', cpf)
          nome=self.txtNome.get()
          print('nome', nome)
        
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return cpf, nome




#LerDados da Tela 2
#-----------------------------------------------------------------------------           
    def fLerCampos2(self):
        try:
          print("************ dados dsponíveis ***********") 
          
          
          codigo2 = str(self.txtCodigo2.get())
          print('Cod. Sis.', codigo2)
          perfil= self.txtPerfil.get()
          print('Função', perfil)
        
          print('Leitura dos Dados com Sucesso!')        
        except:
          print('Não foi possível ler os dados.')
        return codigo2, perfil



#-----------------------------------------------------------------------------
#Cadastrar Usuario
#-----------------------------------------------------------------------------           
    def fCadastrarProduto(self):
        try:
          print("************ dados dsponíveis ***********") 
          cpf, nome= self.fLerCampos()

          if len(cpf) == 11:
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
            messagebox.showerror(title= "CPF Inválido", message= "CPF deve conter 11 digitos númericos, sem o uso de pontos e/ou traços.")
            print('Não foi possível fazer o cadastro.')
        except:
          print('Não foi possível fazer o cadastro.')
#-----------------------------------------------------------------------------
    def frestricaoMatrizSod(self, cpf, codigo2, perfil):
      
      self.registros_usr = self.objBD2.Obter_registros_CPF(cpf)
      dfU = pd.DataFrame.from_items(self.registros_usr)
      
      linhas_matriz = dfU.values.tolist()
      
      self.registros_matriz = self.objBD3.selecionarDados()
      dfM = pd.DataFrame.from_tems(self.registros_matris)
      cadastros = dfM.values.tolist()
      
      # cadastros = list(map(str,cadastros))
      # restricoesM = list(map(str, restricoesM))
      print("Registro da matriz", linhas_matriz)
      print("Registro do usr", cadastros[1])
      print(codigo2)
      print(perfil)

      passagem = 0

      for cadastro in cadastros:
        for line in linhas_matriz:
          if (line[1] == '' and cadastro in line and codigo2 in line):
              print("Restricao de Sistemas", line)
              passagem = 1
              motivo = 'os setores'
              resposta = f'o setor de código {cadastro[0]}'
              registro = line
              break
          if( cadastro[0] in line and cadastro[1] in line and  codigo2 in line and perfil in line):
              print("Restricao de Perfis", line)
              passagem = 1
              motivo = 'as funções'
              resposta = f' a função ({cadastro[1]}) de código {cadastro[0]}'
              registro = line
              break

      if passagem == 0:
          print("Não foi encontrado restriçao")
          return True

      else:
        messagebox.showerror(title= "Restrição na Matriz SoD", message= f'Registro na MatrizSOD:{registro}\nFoi encontrado restrição no registro de ({perfil}) de código {codigo2}. \nRestrição entre {motivo} da empresa. \nO conflito é entre {resposta} cadastrado previamente para este funcionário.')
        return False



    def fCadastrarPerfil(self):
      try:
        print("************ dados dsponíveis ***********") 
        codigo2, perfil= self.fLerCampos2()
        cpf, nome = self.fLerCampos()
        self.registros_usr = self.objBD2.Obter_registros_CPF(cpf)
        cadastros = list(map(list,self.registros_usr))
      
        
      
        self.registros_matriz = self.objBD3.selecionarDados()
        linhas_matriz = list(map( list,self.registros_matriz))
        print("Registro da matriz", linhas_matriz)
        print("Registro do usr", cadastros)
        print(codigo2)
        print(perfil)
        codigo2 = int(codigo2)
        passagem = 0


        for line in linhas_matriz:
          for cadastro in cadastros:
            
            print(cadastro[0])
            if ( cadastro[0] in line and '' in line and codigo2 in line) :
                print("Restricao de Sistemas", line)
                passagem = 1
                motivo = 'os setores'
                resposta = f'o setor de código {cadastro[0]}'
                registro = line
                break
            if(cadastro[1] in line and perfil in line):
                print("Restricao de Perfis", line)
                passagem = 1
                motivo = 'as funções'
                resposta = f' a função ({cadastro[1]}) de código {cadastro[0]}'
                registro = line
                break

        if passagem == 0:
            if ( self.objBD2.inserirDados(cpf, codigo2, perfil)):
              self.treePerfil.insert('', 'end',
                                  iid=self.iid,                                   
                                  values=(codigo2,
                                          perfil))                        
              self.iid = self.iid + 1
              self.id = self.id + 1
              self.fLimparTela2()
              print('Produto Cadastrado com Sucesso!')        
              self.treePerfil.delete(*self.treePerfil.get_children())
              self.carregarDadosIniciaisPerfil(cpf)
            
            else:
              messagebox.showerror(title= "Código ou Perfil Inválido", message= """\n 
              O Codigo do Sistema ou o Perfil não estão de acordo com os possíveis cadastros.\n 
              Confira na tabela apresentada na Aba 'CADASTRO DE PERFIS' as possíveis combinações""")
              print('Não foi possível fazer o cadastro.')

        else:
          messagebox.showerror(title= "Restrição na Matriz SoD", message= f'Registro na MatrizSOD:{registro}\nFoi encontrado restrição no registro de ({perfil}) de código {codigo2}. \nRestrição entre {motivo} da empresa. \nO conflito é entre {resposta} cadastrado previamente para este funcionário.')
          


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
#Excluir Usuario
#-----------------------------------------------------------------------------                  
    def fExcluirUsuario(self):
        try:
          print("************ dados dsponíveis ***********")        
          cpf, nome= self.fLerCampos()
          codigo2, perfil = self.fLerCampos2()
          self.objBD.excluirDados(cpf)          
          #recarregar dados na tela
          self.treeProdutos.delete(*self.treeProdutos.get_children()) 
          self.carregarDadosIniciais()
          self.fLimparTela()
          print('Produto Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do produto.')
#-----------------------------------------------------------------------------


#Excluir Usuario Perfil
#-----------------------------------------------------------------------------                  
    def fExcluirPerfil(self):
        try:
          print("************ dados dsponíveis ***********")
          cpf, nome = self.fLerCampos()        
          codigo2, perfil= self.fLerCampos2()
          item_selecionado = self.treePerfil.selection()
          self.objBD2.excluirDados(cpf, codigo2, perfil)     
          #recarregar dados na tela

          self.treePerfil.delete(item_selecionado) 
          # self.carregarDadosIniciais()
          self.fLimparTela2()
          print('Perfil Excluído com Sucesso!')        
        except:
          print('Não foi possível fazer a exclusão do perfil.')
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



    def fLimparTela2(self):
        try:
          print("************ dados dsponíveis ***********")        
          self.txtCodigo2.delete(0, tk.END)
          self.txtPerfil.delete(0, tk.END)
          
          print('Campos Limpos!')        
        except:
          print('Não foi possível limpar os campos.')

    

