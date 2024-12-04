from database import Database

class Vingador:
    lista_vingadores = []

    class CategoriaVingadores:
        HUMANO = "Humano"
        META_HUMANO = "Meta-humano"
        ALIENIGENA = "Alienígena"
        DEIDADE = "Deidade"
        CATEGORIAS_VALIDAS = [HUMANO, META_HUMANO, ALIENIGENA, DEIDADE]

    def __init__(self, nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_de_forca):
        self.nome_heroi = nome_heroi
        self.nome_real = nome_real
        self.categoria = categoria
        self.poderes = poderes
        self.poder_principal = poder_principal
        self.fraquezas = fraquezas
        self.nivel_de_forca = nivel_de_forca
        self.tornozeleira = False
        self.chip_gps = False
        self.convocado = False

    def __str__(self):
        return (f'{self.nome_heroi.ljust(20)} | {self.nome_real.ljust(20)} | {self.categoria.ljust(15)} | '
                f'{"Sim" if self.tornozeleira else "Não"} | {"Sim" if self.chip_gps else "Não"}')

    def detalhes(self):
        poderes_str = ", ".join(self.poderes)
        fraquezas_str = ", ".join(self.fraquezas)
        return (f'Nome do Herói: {self.nome_heroi}\n'
                f'Nome Real: {self.nome_real}\n'
                f'Categoria: {self.categoria}\n'
                f'Poderes: {poderes_str}\n'
                f'Poder Principal: {self.poder_principal}\n'
                f'Fraquezas: {fraquezas_str}\n'
                f'Nível de Força: {self.nivel_de_forca}\n'
                f'Tornozeleira: {"Aplicada" if self.tornozeleira else "Não Aplicada"}\n'
                f'Chip GPS: {"Aplicado" if self.chip_gps else "Não Aplicado"}\n'
                f'Convocado: {"Sim" if self.convocado else "Não"}')

    def aplicar_tornozeleira(self):
        if self.tornozeleira == True:
            return f'{self.nome_heroi} já está com a tornozeleira aplicada.'
        elif self.convocado == False:
            return f'{self.nome_heroi} precisa ser convocado antes de aplicar a tornozeleira.'
        else:
            self.tornozeleira = True
            # Vinculando ao banco de dados
            try:
                db = Database()
                db.connect()
                update_query = "UPDATE tornozeleira SET status = %s, data_ativacao = CURDATE() WHERE heroi_id = (SELECT heroi_id FROM heroi WHERE nome_heroi = %s)"
                db.cursor.execute(update_query, ('Ativa', self.nome_heroi))
                db.connection.commit()
            except Exception as e:
                return f"Erro ao aplicar a tornozeleira no banco de dados: {e}"
            finally:
                db.disconnect()

            if self.nome_heroi in ["Thor", "Hulk"]:
                return f'{self.nome_heroi} resistiu, mas a tornozeleira foi aplicada com sucesso.'
            return f'Tornozeleira aplicada a {self.nome_heroi}.'

    def aplicar_chip_gps(self):
        if not self.tornozeleira:
            return f'{self.nome_heroi} precisa estar com a tornozeleira antes de aplicar o chip GPS.'
        if self.chip_gps:
            return f'Chip GPS já foi aplicado em {self.nome_heroi}.'
        self.chip_gps = True
        return f'Chip GPS aplicado a {self.nome_heroi}.'
    
    def prender(self):
        return f'{self.nome_heroi} teve o mandado de prisão emitido!'
    
    def listar_poderes(self):
        return self.poderes

    @staticmethod
    def listar_herois():
        db = None
        try:
            db = Database()
            db.connect()
            query = "SELECT nome_heroi, nome_real, categoria FROM heroi"
            db.cursor.execute(query)
            resultados = db.cursor.fetchall()
            for linha in resultados:
                nome_heroi, nome_real, categoria = linha
                print(f'{nome_heroi.ljust(20)} | {nome_real.ljust(20)} | {categoria.ljust(15)}')
        except Exception as e:
            print(f"Erro ao listar vingadores: {e}")
        finally:
            if db:
                db.disconnect()

    @staticmethod
    def detalhar_vingador():
        nome_heroi = input("Nome do Herói: ")
        db = None
        try:
            db = Database()
            db.connect()
            query = "SELECT nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca FROM heroi WHERE nome_heroi = %s"
            db.cursor.execute(query, (nome_heroi,))
            resultado = db.cursor.fetchone()
            if resultado:
                (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca) = resultado
                poderes = poderes.split(",")
                fraquezas = fraquezas.split(",")
                detalhes = (f'Nome do Herói: {nome_heroi}\n'
                            f'Nome Real: {nome_real}\n'
                            f'Categoria: {categoria}\n'
                            f'Poderes: {", ".join(poderes)}\n'
                            f'Poder Principal: {poder_principal}\n'
                            f'Fraquezas: {", ".join(fraquezas)}\n'
                            f'Nível de Força: {nivel_forca}\n')
                print(detalhes)
            else:
                print(f"Vingador '{nome_heroi}' não encontrado no banco de dados.")
        except Exception as e:
            print(f"Erro ao detalhar vingador: {e}")
        finally:
            if db:
                db.disconnect()

    @staticmethod
    def convocar():
        nome_heroi = input("Nome do Herói: ")
        db = None
        try:
            db = Database()
            db.connect()
            query = "UPDATE heroi SET convocado = %s WHERE nome_heroi = %s"
            db.cursor.execute(query, (True, nome_heroi))
            db.connection.commit()
            vingador = next((v for v in Vingador.lista_vingadores if v.nome_heroi == nome_heroi), None)
            if vingador:
                vingador.convocado = True 
            print(f"Vingador {nome_heroi} convocado com sucesso.")
        except Exception as e:
            print(f"Erro ao convocar vingador: {e}")
        finally:
            if db:
                db.disconnect()

    def salvar(self):
        db = None
        try:
            db = Database()
            db.connect()
            query = """
                INSERT INTO heroi (nome_heroi, nome_real, categoria, poderes, poder_principal, fraquezas, nivel_forca, convocado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            valores = (
                self.nome_heroi,
                self.nome_real,
                self.categoria,
                ",".join(self.poderes),
                self.poder_principal,
                ",".join(self.fraquezas),
                self.nivel_de_forca,
                self.convocado
            )
            db.execute_query(query, valores)
            print(f"Vingador {self.nome_heroi} salvo no banco de dados com sucesso.")
        except Exception as e:
            print(f"Erro ao salvar vingador no banco de dados: {e}")
        finally:
            if db:
                db.disconnect()