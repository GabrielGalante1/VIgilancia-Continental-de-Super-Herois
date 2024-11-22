import os
import time
from model.vingador import Vingador

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
''', 0.007)
            Interface.animacao = False
        print('\nSeja bem-vindo! Escolha uma das opções abaixo\n')
        print('1. Cadastrar Vingador')
        print('2. Ver lista de Vingadores')
        print('0. Sair')
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
            try:
                nivel_de_forca = int(input('Nível de força (Entre 0 a 10000): '))
                if nivel_de_forca <= 0 or nivel_de_forca >= 10000:
                    Vingador.nivel_de_forca = 5000
                    print("O número de força digitado não correspondeu ao esperado.")
                    print("O número de força foi definido para 5000.")
                    time.sleep(1)
                    os.system("cls")
                else:
                    break
            except ValueError:
                print("Por favor, digite um número válido.")
                time.sleep(1)
                os.system("cls")

        vingador = Vingador(
            input('Vulgo: '),
            input('Nome real: '),
            categoria,
            input('Poder 1: '),
            input('Poder 2: '),
            input('Poder 3: '),
            input('Poder principal: '),
            input('Fraqueza 1: '),
            input('Fraqueza 2: '),
            input('Fraqueza 3: '),
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
            print("3. Avançado")
            print("0. Sair")
            Interface.ler_opcao_usuario(Interface.detalhes_vingador, Interface.deletar_vingador, Interface.avancado, Interface.menu)
        Interface.VoltarMenu()

    def avancado():
        print("O que você deseja fazer?")
        print("1. Aplicar tornozeleira")
        print("2. Mandato de prisão")
        print("0. Sair")
        Interface.ler_opcao_usuario(Vingador.aplicar_tornozeleira, Interface.menu)


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
    def ler_opcao_usuario(met1=None, met2=None, met3=None, met4=None):
        opcao = input("\nDigite sua opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if opcao == "1" and met1:
            met1()
        elif opcao == "2" and met2:
            met2()
        elif opcao == "3" and met3:
            met3()
        elif opcao == "0" and met4:
            met4()