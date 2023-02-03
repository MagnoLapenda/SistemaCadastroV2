import pyodbc

server = 'tcp: Servidor'
driver = '{ODBC Driver 18 for SQL Server}'
database = 'Banco de dados'
username = 'Email de login'
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
