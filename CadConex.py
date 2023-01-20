import pyodbc

server = 'Nome do servidor'
driver = '{ODBC Driver 18 for SQL Server}'
database = 'Nome do banco de dados'
username = 'Email do usuário'
Authentication = 'ActiveDirectoryInteractive'
port = '1433'

conexao = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';AUTHENTICATION='+Authentication+';'
                         'PORT='+port+';DATABASE='+database+';UID='+username)

cursor = conexao.cursor()


def gravar():
    cursor.commit()


def fechar_conexao():
    cursor.close()
    conexao.close()
