class Perfil:
    def __init__(self, codigo = 0, nome = '', descricao = ''):
        self.__codigo = codigo
        self.__nome = nome
        self.__descricao = descricao

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo
    
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def setDescricao(self, descricao):
        self.__descricao = descricao

    def getDescricao(self):
        return self.__descricao