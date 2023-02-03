import warnings
import pandas as pd
from tabulate import tabulate
from CadConex import conexao, cursor, gravar


# Classe dos motoristas
class Motorista:

    # Método construtor
    def __init__(self, id_moto: int, cnh: int, nome: str, sobrenome: str, nasc: str):
        self.id_moto = id_moto
        self.cnh = cnh
        self.nome = nome
        self.sobrenome = sobrenome
        self.nasc = nasc

    @property
    def id_moto(self) -> int:
        return self._id_moto

    @id_moto.setter
    def id_moto(self, valor_moto):
        self._id_moto = int(valor_moto)

    @property
    def cnh(self) -> int:
        return self._cnh

    @cnh.setter
    def cnh(self, valor_cnh):
        self._cnh = int(valor_cnh)

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor_nome):
        self._nome = str(valor_nome)

    @property
    def sobrenome(self) -> str:
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor_sobrenome):
        self._sobrenome = str(valor_sobrenome)

    @property
    def nasc(self) -> str:
        return self._nasc

    @nasc.setter
    def nasc(self, valor_nasc):
        self._nasc = str(valor_nasc)

    # Método para cadastro no banco de dados
    def cadastro(self):
        novo = f"""INSERT INTO [magno_lapenda.Motorista](id_motorista, cnh, nome, sobrenome, data_nascimento)
        VALUES ({self.id_moto}, {self.cnh}, '{self.nome}', '{self.sobrenome}', '{self.nasc}')"""
        cursor.execute(novo)


def cadastrar_motorista():
    print("\n" * 25)
    try:
        idt = int(input('Digite o número de identificação (ID) do motorista: '))
    except (Exception,):
        idt = int(input('\033[33mATENÇÃO: Informe apenas a numeração de identificação do motorista: \033[m'))
    try:
        cnh = int(input('Digite a CNH do motorista: '))
    except (Exception,):
        cnh = int(input('\033[33mATENÇÃO: Informe apenas a numeração da CNH: \033[m'))
    nome =str(input('Digite o nome do motorista: ')).strip().upper()
    sobrenome = str(input('Digite o sobrenome do motorista: ')).strip().upper()
    data_nasc = str(input('Digite a data de nascimento do motorista (aaaa-mm-dd): ')).strip()
    if len(data_nasc) != 10:
        data_nasc = str(input('\033[33mATENÇÃO: Digite a data no formato ANO-MÊS-DIA: \033[m')).strip()
    moto = Motorista(idt, cnh, nome, sobrenome, data_nasc)
    try:
        moto.cadastro()
        print("\n" * 25)
        print(f'\033[32m\nMotorista cadastrado com sucesso!\033[m\n')
        gravar()
    except (Exception,):
        print('\033[31m\nERRO! Não foi possível cadastrar o motorista.\033[m')
        pass


def deletar_motorista():
    print("\n" * 25)
    consultar_motorista()
    try:
        idt = int(input('\nDigite o número de identificação (ID) do motorista: '))
    except (Exception,):
        idt = int(input('\033[33m\nATENÇÃO: Informe apenas a numeração de identificação do motorista: \033[m'))
    deletar = f"""DELETE FROM [magno_lapenda.Motorista] WHERE id_motorista = {idt}"""
    cursor.execute(deletar)
    print("\n" * 25)
    print(f'\033[32mMotorista deletado com sucesso!\033[m')
    gravar()


def consultar_motorista():
    print("\n" * 25)
    warnings.simplefilter('ignore', UserWarning)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    leitura = pd.read_sql("SELECT * FROM [magno_lapenda.Motorista]", conexao)
    tabela = tabulate(leitura, headers=['ID Motorista', 'CNH', 'Nome', 'Sobrenome', 'Data de Nascimento'],
                      tablefmt='fancy_grid')
    print('=' * 81)
    print(f'\033[36m{"INFORMAÇÕES DOS MOTORISTAS CADASTRADOS":^81}\033[m')
    print('=' * 81)
    print(tabela)
