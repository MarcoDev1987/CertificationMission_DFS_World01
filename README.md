# CertificationMission_DFS_World01
Projeto em Python com abordagem à questão de Segregation Of Duties (Segregação de Funções):

Foi utilizado o padrão de arquitetura de software MVC (Model View Controller)

Como GUI foi utilizado o TkInter, biblioteca de interface gráfica do Python.

# (1) Explicações do projeto:
O trabalho tem o intuito de simular o funcionamento de um sistema de Segregação de Funções, no qual é um mecânismo muito utilizado em sistemas empresarias que busca a proteção de dados e minimização de possíveis fraudes. Buscando a proteção de dados sensíveis da empresa.

# (2) Manual de uso:
Para executá-lo em sua máquina é necessário a instalação de alguns pacotes, são eles:
psycopg2 e TkInter
E a instalação de um SGBD para Banco de Dados (PostgreSQL) como o PgAdm4.

# (3) Link do vídeo do funcionamento do sistema, de forma resumida:
#    https://www.youtube.com/watch?v=aCo_WqCRni8&t=33s




Formatação das Tabelas:


PERFIS:
Codigo do Sistema(chave Herdada de Sistemas)   |  Nome(Pk)  |     Descrição detalhada



SISTEMAS:
Código(Pk)       |  Nome     



USUARIOS:
CPF(Pk)          |  Nome(Pk)       |  Código Sistema(Pk)   |   Nome do Perfil(Pk)  


MATRIZ SOD:

Cod.Sist A |   Perfil A      |    Cod.Sist B   |     Perfil B  


