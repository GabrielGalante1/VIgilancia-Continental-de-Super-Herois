from vingador import Vingador

class Interface:
    @staticmethod
    def limpar_tela():
        # Implementação da função para limpar a tela
        pass

    @staticmethod
    def menu():
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
        Vingador.listar_herois()

    @staticmethod
    def detalhar_vingador():
        Vingador.detalhar_vingador()

    @staticmethod
    def acao_em_vingador(acao):
        nome_heroi = input("Nome do Herói: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.nome_heroi == nome_heroi), None)
        if vingador:
            print(acao(vingador))
        else:
            print(f"Vingador '{nome_heroi}' não encontrado.")

    @staticmethod
    def convocar_vingador():
        Vingador.convocar()