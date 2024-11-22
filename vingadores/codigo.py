import os
import time

class Vingador:
    lista_vingadores = []

    class CategoriaVingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        CATEGORIAS_VALIDAS = [HUMANO, META_HUMANO, ALIENIGENA, DEUS]

    NIVEIS_DE_FORCA_VALIDOS = ["baixo", "médio", "alto", "muito alto"]

    def __init__(self, vulgo, nome, categoria, poder1, poder2, poder3, poder_principal, fraquezas, nivel_de_forca):
        self.vulgo = vulgo
        self.nome = nome
        self.categoria = categoria
        self.poderes = [poder1, poder2, poder3]
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas.split(', ')  # Fraquezas separadas por vírgulas
        self.nivel_de_forca = nivel_de_forca

    def __str__(self):
        poderes_str = ', '.join(self.poderes)
        return (f'{self.vulgo.ljust(20)} | {self.nome.ljust(20)} | {self.categoria.ljust(20)} | '
                f'{poderes_str.ljust(30)} | {self.poder_principal.ljust(20)} | {", ".join(self.fraquezas).ljust(20)} | '
                f'{str(self.nivel_de_forca).ljust(20)}')

    def listar_poderes(self):
        return f'Poderes: {", ".join(self.poderes)}'

    def aplicar_tornozeleira(self):
        print(f'Tornozeleira aplicada ao Vingador {self.vulgo}.')

    def aplicar_chip_gps(self):
        print(f'Chip GPS implantado em {self.vulgo}.')

    def convocar(self):
        print(f'{self.vulgo} foi convocado para a missão.')

    def prender(self):
        print(f'{self.vulgo} foi preso.')

class Interface:
    animacao = True

    @staticmethod
    def animacaoLinhas(texto, duracao):
        for ch in texto:
            time.sleep(duracao)
            print(ch, end="", flush=True)

    @staticmethod
    def menu():
        if Interface.animacao:
            Interface.animacaoLinhas('''
██╗░░░██╗██╗███╗░░██╗░██████╗░░█████╗░██████╗░░█████╗░██████╗░███████╗░██████╗
██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝
╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██████╔╝█████╗░░╚█████╗░
░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██╔══██╗██╔══╝░░░╚═══██╗
░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║░░██║███████╗██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░
''', 0.01)
            Interface.animacao = False
        print('\nSeja bem-vindo! Escolha uma das opções abaixo\n')
        print('1. Cadastrar Vingador')
        print('2. Ver lista de Vingadores')
        print('3. Sair')
        Interface.ler_opcao_usuario(Interface.Cadastro, Interface.listar_vingadores, Interface.sair)

    @staticmethod
    def VoltarMenu():
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls" if os.name == "nt" else "clear")
        Interface.menu()

    @staticmethod
    def Cadastro():
        while True:
            categoria = input('Categoria (Humano, Meta humano, Alienígena, Deus): ')
            if categoria not in Vingador.CategoriaVingadores.CATEGORIAS_VALIDAS:
                print("Categoria inválida. Por favor, digite uma categoria válida.")
                time.sleep(1)
                os.system("cls")
            else:
                break

        while True:
            nivel_de_forca = input('Nível de força (baixo, médio, alto, muito alto): ')
            if nivel_de_forca.lower() not in Vingador.NIVEIS_DE_FORCA_VALIDOS:
                print("Nível de força inválido. Por favor, digite um nível de força válido.")
                time.sleep(1)
                os.system("cls")
            else:
                break

        vingador = Vingador(
            input('Vulgo: '),
            input('Nome real: '),
            categoria,
            input('Poder 1: '),
            input('Poder 2: '),
            input('Poder 3: '),
            input('Poder principal: '),
            input('Fraquezas (separadas por vírgula): '),
            nivel_de_forca
        )
        Vingador.lista_vingadores.append(vingador)
        print(f'Vingador cadastrado com sucesso! Vulgo: {vingador.vulgo}, Nome real: {vingador.nome}')
        Interface.VoltarMenu()

    @staticmethod
    def listar_vingadores():
        if not Vingador.lista_vingadores:
            print("Nenhum Vingador cadastrado.")
        else:
            print(f'{"Vulgo".ljust(20)} | {"Nome".ljust(20)} | {"Categoria".ljust(20)} | {"Poderes".ljust(30)} | {"Poder principal".ljust(20)} | {"Fraquezas".ljust(20)} | {"Nível de força".ljust(20)}')
            for vingador in Vingador.lista_vingadores:
                print(vingador)
            print("\nEscolha uma opção:")
            print("1. Visualizar mais detalhes de um Vingador")
            print("2. Deletar um Vingador")
            print("3. Voltar ao menu")
            Interface.ler_opcao_usuario(Interface.detalhes_vingador, Interface.deletar_vingador, Interface.menu)
        Interface.VoltarMenu()

    @staticmethod
    def detalhes_vingador():
        vulgo = input("Digite o vulgo do Vingador que deseja ver detalhes: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.vulgo == vulgo), None)
        if vingador:
            print(f'\nDetalhes do Vingador {vingador.vulgo}:')
            print(f'Nome real: {vingador.nome}')
            print(f'Categoria: {vingador.categoria}')
            print(vingador.listar_poderes())
            print(f'Poder principal: {vingador.poder_principal}')
            print(f'Fraquezas: {", ".join(vingador.fraquezas)}')
            print(f'Nível de força: {vingador.nivel_de_forca}')
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def deletar_vingador():
        vulgo = input("Digite o vulgo do Vingador que deseja deletar: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.vulgo == vulgo), None)
        if vingador:
            Vingador.lista_vingadores.remove(vingador)
            print(f'Vingador {vulgo} deletado com sucesso.')
        else:
            print("Vingador não encontrado.")
        Interface.VoltarMenu()

    @staticmethod
    def sair():
        print("Encerrando o programa...")
        time.sleep(1)
        exit()

    @staticmethod
    def ler_opcao_usuario(met1=None, met2=None, met3=None):
        opcao = input("\nDigite sua opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcao == "1" and met1:
            met1()
        elif opcao == "2" and met2:
            met2()
        elif opcao == "3" and met3:
            met3()