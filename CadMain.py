from SistemaCadastroV2.CadConex import fechar_conexao
from SistemaCadastroV2.ClasseCartao import consultar_cartao, deletar_cartao, cadastrar_cartao
from SistemaCadastroV2.ClasseMotorista import cadastrar_motorista, deletar_motorista, consultar_motorista
from SistemaCadastroV2.ClasseOnibus import cadastrar_onibus, deletar_onibus, consultar_onibus
from SistemaCadastroV2.ClasseUsuario import cadastrar_usuario, deletar_usuario, consultar_usuarios


# Pergunta apresentada ao final de cada ação nos painéis específicos
def perguntar():
    print("""
Deseja algo mais?
- Digite \033[32m 1 \033[m para voltar ao menu principal
- Digite \033[31m 2 \033[m para sair da aplicação""")
    resp = input('Opção: ').strip()
    while resp not in ['1', '2']:
        print('\033[33mATENÇÃO: Digite apenas 1 ou 2.\033[m')
        resp = input('Opção: ').strip()
    while True:
        if resp == '1':
            print("\n" * 25)
            break
        elif resp == '2':
            print("\n" * 25)
            print(f'\nObrigado!')
            fechar_conexao()
            exit()


# MENU INICIAL
print('-=' * 21)
print('§', f'\033[34m{"   Bem vindo(a) ao sistema CadUni!   "}\033[m', ' §')
print('-=' * 21)
usuario = str(input('Qual o seu nome? ')).strip().upper()

def main():
    while True:
        print(f"""
    Olá, {usuario}! Em que posso te ajudar?
    
    [1] Usuários
    [2] Cartões dos usuários
    [3] Motoristas
    [4] Frota de ônibus
    [5] Sair do programa
    """)

        esc = input('Digite a opção desejada: ').strip()
        while esc not in ['1', '2', '3', '4', '5']:
            esc = input('\033[33mATENÇÃO: Escolha apenas um número entre 1 e 5: \033[m')
            print('')


        # Menu de opções referente ao cadastro dos usuários
        if esc == '1':
            print("\n" * 25)
            print(f"""
Qual ação você gostaria de realizar?

[1] Cadastrar novo usuário
[2] Excluir usuário
[3] Visualizar usuários cadastrados
""")

            perg = input('Digite a opção desejada: ').strip()
            while perg not in ['1', '2', '3']:
                perg = input('\033[33mATENÇÃO: Escolha apenas um número entre 1 e 3: \033[m')
                print('')

            if perg == '1':
                print("\n" * 25)
                try:
                    cadastrar_usuario()
                except (Exception,):
                    print('\033[31m\nERRO! Não foi possível cadastrar o usuário.\033[m')
                    pass
                perguntar()

            elif perg == '2':
                print("\n" * 25)
                try:
                    deletar_usuario()
                except (Exception,):
                    print('\033[33m\nO usuário informado não foi cadastrado.\033[m')
                    pass
                perguntar()

            elif perg == '3':
                print("\n" * 25)
                consultar_usuarios()
                perguntar()


        # Menu de opções referente ao cadastro dos cartões
        elif esc == '2':
            print("\n" * 25)
            print(f"""
Qual ação você gostaria de realizar?

[1] Cadastrar novo cartão
[2] Excluir cartão
[3] Visualizar cartões cadastrados
""")

            perg = input('Digite a opção desejada: ').strip()
            while perg not in ['1', '2', '3']:
                perg = input('\033[33mATENÇÃO: Escolha apenas um número entre 1 e 3: \033[m')
                print('')

            if perg == '1':
                print("\n" * 25)
                try:
                    cadastrar_cartao()
                except (Exception,):
                    print('\033[31m\nERRO! Não foi possível cadastrar o cartão.\033[m')
                    pass
                perguntar()

            elif perg == '2':
                print("\n" * 25)
                try:
                    deletar_cartao()
                except (Exception,):
                    print('\033[33m\nO cartão informado não foi cadastrado.\033[m')
                    pass
                perguntar()

            elif perg == '3':
                print("\n" * 25)
                consultar_cartao()
                perguntar()

        # Menu de opções referente ao cadastro dos motoristas
        elif esc == '3':
            print("\n" * 25)
            print(f"""
Qual ação você gostaria de realizar?

[1] Cadastrar novo motorista
[2] Excluir motorista
[3] Visualizar motoristas cadastrados
""")

            perg = input('Digite a opção desejada: ').strip()
            while perg not in ['1', '2', '3']:
                perg = input('\033[33mATENÇÃO: Escolha apenas um número entre 1 e 3: \033[m')
                print('')

            if perg == '1':
                print("\n" * 25)
                try:
                    cadastrar_motorista()
                except (Exception,):
                    print('\033[31m\nERRO! Não foi possível cadastrar o motorista.\033[m')
                    pass
                perguntar()

            elif perg == '2':
                print("\n" * 25)
                try:
                    deletar_motorista()
                except (Exception,):
                    print('\033[33m\nO motorista informado não foi cadastrado.\033[m')
                    pass
                perguntar()

            elif perg == '3':
                print("\n" * 25)
                consultar_motorista()
                perguntar()


# Menu de opções referente ao cadastro da frota de ônibus
        elif esc == '4':
            print("\n" * 25)
            print(f"""
Qual ação você gostaria de realizar?

[1] Cadastrar novo ônibus
[2] Excluir ônibus
[3] Visualizar frota de ônibus
""")

            perg = input('Digite a opção desejada: ').strip()
            while perg not in ['1', '2', '3']:
                perg = input('\033[33mATENÇÃO: Escolha apenas um número entre 1 e 3: \033[m')
                print('')

            if perg == '1':
                print("\n" * 25)
                try:
                    cadastrar_onibus()
                except (Exception,):
                    print('\033[31m\nERRO! Não foi possível cadastrar o ônibus.\033[m')
                    pass
                perguntar()

            elif perg == '2':
                print("\n" * 25)
                try:
                    deletar_onibus()
                except (Exception,):
                    print('\033[33m\nO ônibus informado não foi cadastrado.\033[m')
                    pass
                perguntar()

            elif perg == '3':
                print("\n" * 25)
                consultar_onibus()
                perguntar()

        # Opção de sair da aplicação
        elif esc == '5':
            print("\n" * 25)
            print(f'\nVolte sempre, {usuario}!')
            fechar_conexao()
            exit()

main()
