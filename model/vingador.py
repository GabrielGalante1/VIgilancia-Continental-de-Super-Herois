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

    @staticmethod
    def aplicar_tornozeleira():
        nome_heroi = input("Nome do Herói: ")
        db = None
        try:
            db = Database()
            db.connect()
            
            # Verificar se o herói existe e seu status de convocação
            query = "SELECT heroi_id, convocado FROM heroi WHERE nome_heroi = %s"
            db.cursor.execute(query, (nome_heroi,))
            resultado = db.cursor.fetchone()
            
            if resultado is None:
                print(f"Herói {nome_heroi} não encontrado no banco de dados.")
                return
            
            heroi_id, convocado = resultado
            
            if not convocado:
                print(f'{nome_heroi} precisa ser convocado antes de aplicar a tornozeleira.')
                return
            
            # Verificar se já tem tornozeleira
            query = "SELECT status FROM tornozeleira WHERE heroi_id = %s"
            db.cursor.execute(query, (heroi_id,))
            tornozeleira = db.cursor.fetchone()
            
            if tornozeleira and tornozeleira[0] == 'Ativa':
                print(f'{nome_heroi} já está com a tornozeleira aplicada.')
                return
                
            # Criar ou atualizar tornozeleira
            if not tornozeleira:
                insert_query = """
                    INSERT INTO tornozeleira (heroi_id, status, data_ativacao) 
                    VALUES (%s, %s, CURDATE())
                """
                db.cursor.execute(insert_query, (heroi_id, 'Ativa'))
            else:
                update_query = """
                    UPDATE tornozeleira 
                    SET status = %s, data_ativacao = CURDATE() 
                    WHERE heroi_id = %s
                """
                db.cursor.execute(update_query, ('Ativa', heroi_id))
            
            db.connection.commit()
            
            if nome_heroi in ["Thor", "Hulk"]:
                print(f'{nome_heroi} resistiu, mas a tornozeleira foi aplicada com sucesso.')
            else:
                print(f'Tornozeleira aplicada a {nome_heroi}.')
                
        except Exception as e:
            print(f"Erro ao aplicar tornozeleira: {e}")
        finally:
            if db:
                db.disconnect()

    def aplicar_chip_gps(self):
        db = None
        try:
            db = Database()
            db.connect()
            
            # Verificar se o herói existe no banco de dados
            query = "SELECT heroi_id FROM heroi WHERE nome_heroi = %s"
            db.cursor.execute(query, (self.nome_heroi,))
            resultado = db.cursor.fetchone()
            
            if resultado is None:
                return f"Herói {self.nome_heroi} não encontrado no banco de dados."
            
            heroi_id = resultado[0]
            
            # Verificar se o herói tem uma tornozeleira ativa
            query = "SELECT tornozeleira_id FROM tornozeleira WHERE heroi_id = %s AND status = 'Ativa'"
            db.cursor.execute(query, (heroi_id,))
            resultado = db.cursor.fetchone()
            
            if resultado is None:
                return f'{self.nome_heroi} precisa estar com a tornozeleira ativa antes de aplicar o chip GPS.'
            
            tornozeleira_id = resultado[0]
            
            if self.chip_gps:
                return f'Chip GPS já foi aplicado em {self.nome_heroi}.'
            
            # Inserir o chip GPS na tabela chip_gps
            insert_query = """
                INSERT INTO chip_gps (tornozeleira_id, localizacao_atual, ultima_localizacao) 
                VALUES (%s, %s, %s)
            """
            db.cursor.execute(insert_query, (tornozeleira_id, 'Localização Inicial', 'Localização Inicial'))
            db.connection.commit()
            
            self.chip_gps = True
            return f'Chip GPS aplicado a {self.nome_heroi}.'
            
        except Exception as e:
            return f"Erro ao aplicar chip GPS: {e}"
        finally:
            if db:
                db.disconnect()

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
            
            # Verificar se o herói existe no banco de dados
            query = "SELECT convocado FROM heroi WHERE nome_heroi = %s"
            db.cursor.execute(query, (nome_heroi,))
            resultado = db.cursor.fetchone()
            
            if resultado is None:
                print(f"Herói {nome_heroi} não encontrado no banco de dados.")
                return
            
            convocado = resultado[0]
            
            if convocado:
                print(f"Herói {nome_heroi} já foi convocado.")
                return
            
            # Atualizar o status de convocação do herói no banco de dados
            update_query = "UPDATE heroi SET convocado = %s WHERE nome_heroi = %s"
            db.cursor.execute(update_query, (True, nome_heroi))
            db.connection.commit()
            
            # Atualizando o atributo 'convocado' do vingador na lista
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