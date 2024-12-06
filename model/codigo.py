from vingador import Vingador
from database import Database
import os

class Interface:

    @staticmethod
    def ciencia():
        os.system('cls')
        print("""
██╗░░░██╗██╗███╗░░██╗░██████╗░ █████╗░██████╗░░█████╗░██╗░██████╗
██║░░░██║██║████╗░██║██╔════╝░██╔══██╗██╔══██╗██╔══██╗██║██╔════╝
╚██╗░██╔╝██║██╔██╗██║██║░░██╗░███████║██║░░██║██║░░██║██║╚█████╗░
░╚████╔╝░██║██║╚████║██║░░╚██╗██╔══██║██║░░██║██║░░██║██║░╚═══██╗
░░╚██╔╝░░██║██║░╚███║╚██████╔╝██║░░██║██████╔╝╚█████╔╝██║██████╔╝
░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝╚═════╝░

        """)

    @staticmethod
    def menu():
        Interface.ciencia()
        print("1. Cadastrar Vingador")
        print("2. Listar Vingadores")
        print("3. Detalhar Vingador")
        print("4. Convocar Vingador")
        print("5. Aplicar Tornozeleira")
        print("6. Aplicar Chip GPS")
        print("0. Sair")
        return input("Escolha uma opção: ")

    @staticmethod
    def cadastrar_vingador():
        Interface.ciencia()
        nome_heroi = input("Nome do Herói: ")
        nome_real = input("Nome Real: ")
        categoria = input("Categoria: ")
        if categoria not in Vingador.CategoriaVingadores.CATEGORIAS_VALIDAS:
            print("Categoria inválida. Tente novamente.")
            return
        poderes = input("Poderes (separados por vírgula): ").split(",")
        poder_principal = input("Poder Principal: ")
        fraquezas = input("Fraquezas (separadas por vírgula): ").split(",")
        nivel_de_forca = int(input("Nível de Força (0-10000): "))
        if nivel_de_forca < 0 or nivel_de_forca > 10000:
            print("Nível de força inválido. Tente novamente.")
            return
        novo_vingador = Vingador(nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca)
        novo_vingador.salvar()
        Vingador.lista_vingadores.append(novo_vingador)
        print(f"Vingador {nome_heroi} cadastrado com sucesso!")

    @staticmethod
    def listar_vingadores():
        Interface.ciencia()
        Vingador.listar_herois()

    @staticmethod
    def detalhar_vingador():
        Interface.ciencia()
        Vingador.detalhar_vingador()

    @staticmethod
    def acao_em_vingador(acao):
        Interface.ciencia()
        nome_heroi = input("Nome do Herói: ")
        db = None
        try:
            db = Database()
            db.connect()
            query = "SELECT nome_heroi FROM heroi WHERE nome_heroi = %s"
            db.cursor.execute(query, (nome_heroi,))
            resultado = db.cursor.fetchone()
            if resultado:
                vingador = Vingador(nome_heroi, "", "", [], "", [], 0)  # Cria um objeto Vingador temporário
                print(acao(vingador))
            else:
                print(f"Vingador '{nome_heroi}' não encontrado no banco de dados.")
        except Exception as e:
            print(f"Erro ao verificar vingador no banco de dados: {e}")
        finally:
            if db:
                db.disconnect()

    @staticmethod
    def convocar_vingador():
        Interface.ciencia()
        Vingador.convocar()

    @staticmethod
    def aplicar_tornozeleira():
        Interface.ciencia()
        Vingador.aplicar_tornozeleira()

    @staticmethod
    def aplicar_chip_gps():
        Interface.ciencia()
        Vingador.aplicar_chip_gps()