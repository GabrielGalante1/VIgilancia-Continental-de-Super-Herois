from model.codigo import Interface
from model.vingador import Vingador

def main():
    Vingador('Thor', 'Thor', 'Deus', ['Força', 'Imortalidade'], 'Eletricidade', ['Arrogancia', 'Orgulho'], 9000)
    Vingador('Hulk', 'Bruce Banner', 'Meta-Humano', ['Força', 'Resistência', 'Fator Cura'], 'Transformação', ['Autocontrole', 'Raiva'], 10000)
    Vingador('Capitão América', 'Steve Rogers', 'Humano', ['Força', 'Agilidade', 'Resistência'], 'Força', ['Humano', 'Idade'], 100)
    Vingador('Viuva Negra', 'Natasha Romanoff', 'Humano', ['Utilitários', 'Furtividade'], 'Agilidade', ['Humano', 'Insegurança'],20)
Interface.menu()