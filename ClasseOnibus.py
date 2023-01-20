import warnings
import pandas as pd
from tabulate import tabulate
from SistemaCadastroV2.CadConex import conexao, cursor, gravar


# Classe dos ônibus
class Onibus:

    # Método construtor
    def __init__(self, placa: int, linha: int, modelo: str, ano: str, id_moto: int):
        self.placa = placa
        self.linha = linha
        self.modelo = modelo
        self.ano = ano
        self.id_moto = id_moto

    @property
    def placa(self) -> int:
        return self._placa

    @placa.setter
    def placa(self, valor_placa):
        self._placa = int(valor_placa)

    @property
    def linha(self) -> int:
        return self._linha

    @linha.setter
    def linha(self, valor_linha):
        self._linha = int(valor_linha)

    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, valor_modelo):
        self._modelo = str(valor_modelo)

    @property
    def ano(self) -> str:
        return self._ano

    @ano.setter
    def ano(self, valor_ano):
        self._ano = str(valor_ano)

    @property
    def id_moto(self) -> int:
        return self._id_moto

    @id_moto.setter
    def id_moto(self, valor_id_moto):
        self._id_moto = int(valor_id_moto)

    # Método para cadastro no banco de dados
    def cadastro(self):
        novo = f"""INSERT INTO [magno_lapenda.Onibus](placa, linha, modelo, ano, id_motorista)
        VALUES ({self.placa}, {self.linha}, '{self.modelo}', '{self.ano}', {self.id_moto})"""
        cursor.execute(novo)


def cadastrar_onibus():
    print("\n" * 25)
    try:
        placa = int(input('Digite o número da placa: '))
    except (Exception,):
        placa = int(input('\033[33mATENÇÃO: Informe apenas a numeração da placa: \033[m'))
    try:
        linha = int(input('Digite o número da linha: '))
    except (Exception,):
        linha = int(input('\033[33mATENÇÃO: Informe apenas a numeração da linha: \033[m'))
    modelo = str(input('Digite o modelo do ônibus: ')).strip().upper()
    ano = str(input('Digite o ano de fabricação: ')).strip()
    ano = ano[0:4]
    try:
        id_moto = int(input('Digite a ID do motorista: '))
    except (Exception,):
        id_moto = int(input('\033[33mATENÇÃO: Informe apenas a numeração de identificação do motorista: \033[m'))
    onibus = Onibus(placa, linha, modelo, ano, id_moto)
    try:
        onibus.cadastro()
        print("\n" * 25)
        print(f'\033[32m\nÔnibus cadastrado com sucesso!\033[m\n')
        gravar()
    except (Exception,):
        print('\033[31m\nERRO! Não foi possível cadastrar o ônibus.\033[m')
        pass


def deletar_onibus():
    print("\n" * 25)
    consultar_onibus()
    try:
        placa = int(input('\nDigite a placa do ônibus: '))
    except (Exception,):
        placa = int(input('\033[33m\nATENÇÃO: Informe apenas a numeração da placa: \033[m'))
    deletar = f"""DELETE FROM [magno_lapenda.Onibus] WHERE placa = {placa}"""
    cursor.execute(deletar)
    print("\n" * 25)
    print(f'\033[32mÔnibus deletado com sucesso!\033[m')
    gravar()


def consultar_onibus():
    print("\n" * 25)
    warnings.simplefilter('ignore', UserWarning)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    leitura = pd.read_sql("SELECT * FROM [magno_lapenda.Onibus]", conexao)
    tabela = tabulate(leitura, headers=['Placa', 'Linha', 'Modelo', 'Ano', 'ID Motorista'],
                      tablefmt='fancy_grid')
    print('=' * 67)
    print(f'\033[36m{"INFORMAÇÕES DA FROTA CADASTRADA":^67}\033[m')
    print('=' * 67)
    print(tabela)
