import warnings
import pandas as pd
from tabulate import tabulate
from CadConex import conexao, cursor, gravar


# Classe dos cartões
class Cartao:

    # Método construtor
    def __init__(self, id_user: int, id_cartao: int, credito: float, tipo: str, emissao: str):
        self.id_user = id_user
        self.id_cartao = id_cartao
        self.credito = credito
        self.tipo = tipo
        self.emissao = emissao

    @property
    def id_user(self) -> int:
        return self._id_user

    @id_user.setter
    def id_user(self, valor_id_user):
        self._id_user = int(valor_id_user)

    @property
    def id_cartao(self) -> int:
        return self._id_cartao

    @id_cartao.setter
    def id_cartao(self, valor_id_cartao):
        self._id_cartao = int(valor_id_cartao)

    @property
    def credito(self) -> float:
        return self._credito

    @credito.setter
    def credito(self, valor_credito):
        self._credito = float(valor_credito)

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, valor_tipo):
        self._tipo = str(valor_tipo)

    @property
    def emissao(self) -> str:
        return self._emissao

    @emissao.setter
    def emissao(self, data_emissao):
        self._emissao = str(data_emissao)

    # Método para cadastro no banco de dados
    def cadastro(self):
        novo = f"""INSERT INTO [magno_lapenda.Cartao](id_cartao, id_user, credito, tipo, data_emissao)
        VALUES ({self.id_user}, {self.id_cartao}, {self.credito}, '{self.tipo}', '{self.emissao}')"""
        cursor.execute(novo)


def cadastrar_cartao():
    print("\n" * 25)
    try:
        idt = int(input('Digite o número de identificação (ID) do cartão: '))
    except (Exception,):
        idt = int(input('\033[33mATENÇÃO: Informe apenas a numeração de identificação do cartão: \033[m'))
    try:
        idt_user = int(input('Digite o número de identificação (ID) do titular: '))
    except (Exception,):
        idt_user = int(input('\033[33mATENÇÃO: Informe apenas a numeração de identificação do titular: \033[m'))
    try:
        credito = float(input('Digite o valor do crédito a ser fornecido: '))
    except (Exception,):
        print('\033[33mATENÇÃO: Não utilizar virgula. O valor deve ser indicado como no exemplo: 100.50\033[m')
        credito = float(input('Digite novamente o valor desejado para crédito: '))
    tipo = str(input('Digite o tipo do cartão: ')).strip().upper()
    data_emissao = str(input('Digite a data de emissão do cartão (aaaa-mm-dd): ')).strip()
    if len(data_emissao) != 10:
        data_emissao = str(input('\033[33mATENÇÃO: Digite a data no formato ANO-MÊS-DIA: \033[m')).strip()
    cartao = Cartao(idt, idt_user, credito, tipo, data_emissao)
    try:
        cartao.cadastro()
        print("\n" * 25)
        print(f'\033[32m\nCartão cadastrado com sucesso!\033[m\n')
        gravar()
    except (Exception,):
        print('\033[31m\nERRO! Não foi possível cadastrar o cartão.\033[m')
        pass


def deletar_cartao():
    print("\n" * 25)
    consultar_cartao()
    try:
        idt = int(input('\nDigite o número de identificação (ID) do cartão: '))
    except (Exception,):
        idt = int(input('\033[33m\nATENÇÃO: Informe apenas a numeração de identificação do cartão: \033[m'))
    deletar = f"""DELETE FROM [magno_lapenda.Cartao] WHERE id_cartao = {idt}"""
    cursor.execute(deletar)
    print("\n" * 25)
    print(f'\033[32mCartão deletado com sucesso!\033[m')
    gravar()


def consultar_cartao():
    print("\n" * 25)
    warnings.simplefilter('ignore', UserWarning)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    leitura = pd.read_sql("SELECT * FROM [magno_lapenda.Cartao]", conexao)
    tabela = tabulate(leitura, headers=['ID Cartão', 'ID Usuário', 'Crédito (R$)', 'Tipo do cartão', 'Data de Emissão'],
                      tablefmt='fancy_grid')
    print('=' * 90)
    print(f'\033[36m{"INFORMAÇÕES DOS CARTÕES CADASTRADOS":^90}\033[m')
    print('=' * 90)
    print(tabela)
