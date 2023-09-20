class Usuario:
    def __init__(self, cpf = 0, nome = '', codigo = '', perfil = ''):
        self.__cpf = cpf
        self.__nome = nome
        self.__codigo = codigo
        self.__perfil = perfil
        self.__lista_perfil = []

    def setCpf(self, cpf):
        self.__cpf = cpf

    def getCpf(self):
        return self.__cpf
    
    
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
 
        
    
    def addSistemaPerfil(self, codigo, perfil):
        self.__codigo = codigo
        self.__perfil = perfil

        
        if self.__perfil not in self.__lista_perfil :
            self.__lista_perfil.extend([self.__codigo, self.__perfil])
            return 'Cadastro realizado com sucesso'
        
        else:
            return 'O Usuário já tem este perfil cadastrado'

    def getSistemaPerfil(self):
        return self.__lista_perfil

    
    