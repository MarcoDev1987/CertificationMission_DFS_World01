class Sistema:

    def __init__(self, codigo = 0, nome = ''):
        self.__codigo = codigo
        self.__nome = nome
    
    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getCodigo(self):
        return self.__codigo
    
    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    