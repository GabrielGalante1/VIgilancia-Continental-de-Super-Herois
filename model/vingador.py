from model.codigo import Interface

class Vingador:
    lista_vingadores = []

    class CategoriaVingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta humano"
        ALIENIGENA = "Alienígena"
        DEUS = "Deus"
        CATEGORIAS_VALIDAS = [HUMANO, META_HUMANO, ALIENIGENA, DEUS]

    def __init__(self, vulgo, nome, categoria, poder1, poder2, poder3, poder_principal, fraqueza1, fraqueza2, fraqueza3, nivel_de_forca, tornozeleira = False, preso = False, chip_gps = False, convocado = False):
        self.vulgo = vulgo
        self.nome = nome
        self.categoria = categoria
        self.poderes = [poder1, poder2, poder3]
        self.poder_principal = poder_principal
        self.fraquezas = [fraqueza1, fraqueza2, fraqueza3]  # Fraquezas separadas por vírgulas
        self.nivel_de_forca = nivel_de_forca
        self.tornozeleira = False
        self.preso = False
        self.chip_gps = False
        self.convocado = False

    def __str__(self):
        poderes_str = ', '.join(self.poderes)
        fraquezas_str = ', '.join(self.fraquezas)
        return (f'{self.vulgo.ljust(20)} | {self.nome.ljust(20)} | {self.categoria.ljust(20)} | '
                f'{poderes_str.ljust(30)} | {self.poder_principal.ljust(20)} | {(fraquezas_str).ljust(20)} | '
                f'{str(self.nivel_de_forca).ljust(20)}')

    def listar_poderes(self):
        return f'Poderes: {", ".join(self.poderes)}'

    def convocar(self):
        vulgo = input("Digite o vulgo do Vingador que deseja convocar: ")
        vingador = next((v for v in Vingador.lista_vingadores if v.vulgo == vulgo), None)
        if vingador.convocado == False:
            vingador.convocado = True
            print(f'{self.vulgo} foi convocado para a missão.')
        elif vingador.convocado == True:
            print(f'{self.vulgo} já foi convocado para a missão.')
        

    def aplicar_tornozeleira():
        while True:
            try:
                vulgo = input("Digite o vulgo do Vingador que deseja aplica tornozeleira: ")
                vingador = next((v for v in Vingador.lista_vingadores if v.vulgo == vulgo), None)
            except ValueError:
                print("Vingador não encontrado.")
                
            if vingador.convocar == False:
                print("Vingador não convocado para a missão.")
            elif vingador.tornozeleira == True:
                print(f'Tornozeleira já aplicada ao Vingador {vingador.vulgo}.')
                break
            else:
                vingador.tornozeleira = False
                print(f'Tornozeleira aplicada ao Vingador {vingador.vulgo}.')
                Interface.VoltarMenu()
                break