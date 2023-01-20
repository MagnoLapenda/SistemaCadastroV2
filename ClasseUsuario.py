import warnings
import pandas as pd
from tabulate import tabulate
from SistemaCadastroV2.CadConex import conexao, cursor, gravar


# Classe dos usuários
class Usuario:

    # Método construtor
    def __init__(self, id_user: int, nome: str, sobrenome: str, email: str, bairro: str, nasc: str):
        self.id_user = id_user
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.bairro = bairro
        self.nasc = nasc

    @property
    def usuario(self) -> int:
        return self.id_user

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def sobrenome(self) -> str:
        return self._sobrenome

    @property
    def email(self) -> str:
        return self._email

    @property
    def bairro(self) -> str:
        return self._bairro

    @property
    def nasc(self) -> str:
        return self._nasc

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @usuario.setter
    def usuario(self, novo_id_user):
        self.id_user = int(novo_id_user)

    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self._sobrenome = str(novo_sobrenome)

    @email.setter
    def email(self, novo_email):
        self._email = str(novo_email)

    @bairro.setter
    def bairro(self, novo_bairro):
        self._bairro = str(novo_bairro)

    @nasc.setter
    def nasc(self, data_nasc):
        self._nasc = str(data_nasc)

    # Método para cadastro no banco de dados
    def cadastro(self):
        novo = f"""INSERT INTO [magno_lapenda.Usuario](id, nome, sobrenome, email, bairro, data_nascimento)
        VALUES ({self.id_user}, '{self.nome}', '{self.sobrenome}', '{self.email}', '{self.bairro}', '{self.nasc}')"""
        cursor.execute(novo)


def cadastrar_usuario():
    print("\n" * 25)
    try:
        idt = int(input('Digite o número de identificação (ID) do usuário: '))
    except (Exception,):   # Quebra galho para evitar o "too broad exception"
        idt = int(input('\033[33mATENÇÃO: Informe apenas a numeração de identificação do usuário: \033[m'))
    nome = str(input('Digite o primeiro nome do usuário: ')).strip().upper()
    sobrenome = str(input('Digite o sobrenome do usuário: ')).strip().upper()
    email = str(input('Digite o e-mail do usuário: ')).strip().upper()
    bairro = str(input('Digite o bairro do usuário: ')).strip().upper()
    nasc = str(input('Digite a data de nascimento do usuário (aaaa-mm-dd): ')).strip()
    if len(nasc) != 10:
        nasc = str(input('\033[33mATENÇÃO: Digite a data no formato ANO-MÊS-DIA: \033[m')).strip()
    user = Usuario(idt, nome, sobrenome, email, bairro, nasc)
    try:
        user.cadastro()
        print("\n" * 25)
        print(f'\033[32m\nUsuário cadastrado com sucesso!\033[m\n')
        gravar()
    except (Exception,):
        print('\033[31m\nERRO! Não foi possível cadastrar o usuário.\033[m')
        pass


def deletar_usuario():
    print("\n" * 25)
    consultar_usuarios()
    try:
        idt = int(input('\n\nDigite o número de identificação (ID) do usuário: '))
    except (Exception,):
        idt = int(input('\033[33m\nATENÇÃO: Informe apenas a numeração de identificação do usuário: \033[m'))
    deletar = f"""DELETE FROM [magno_lapenda.Usuario] WHERE id = {idt}"""
    cursor.execute(deletar)
    print("\n" * 25)
    print(f'\033[32mUsuário deletado com sucesso!\033[m')
    gravar()


def consultar_usuarios():
    print("\n" * 25)
    warnings.simplefilter('ignore', UserWarning)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    leitura = pd.read_sql("SELECT * FROM [magno_lapenda.Usuario]", conexao)
    tabela = tabulate(leitura, headers= ['ID Usuário', 'Nome', 'Sobrenome', 'E-mail', 'Bairro',
                      'Data de Nascimento'],tablefmt='fancy_grid')
    print('=' * 117)
    print(f'\033[36m{"INFORMAÇÕES DOS USUÁRIOS CADASTRADOS":^117}\033[m')
    print('=' * 117)
    print(tabela)
