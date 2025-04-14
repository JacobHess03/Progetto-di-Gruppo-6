# Classe base
class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"{self.nome} si sta muovendo con {self.numero_soldati} soldati.")

    def attacca(self):
        print(f"{self.nome} attacca il nemico!")

    def ritira(self):
        print(f"{self.nome} si sta ritirando strategicamente.")


# Classi derivate
class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super(self, nome, numero_soldati)
    def costruisci_trincea(self):
        print(f"{self.nome} costruisce trincee per la difesa temporanea.")


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super(self, nome, numero_soldati)
    def calibra_artiglieria(self):
        print(f"{self.nome} calibra i pezzi di artiglieria per una maggiore precisione.")


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super(self, nome, numero_soldati)
    def esplora_terreno(self):
        print(f"{self.nome} esplora il terreno per raccogliere informazioni sul nemico.")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati):
        super(self, nome, numero_soldati)
    def rifornisci_unita(self):
        print(f"{self.nome} si occupa del rifornimento e della manutenzione delle truppe.")


class Ricognizione(UnitaMilitare):
    
    def __init__(self, nome, numero_soldati):
        super(self, nome, numero_soldati)
    def conduci_ricognizione(self):
        print(f"{self.nome} conduce una missione di sorveglianza.")


# Classe ControlloMilitare
class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
    def __init__(self):
        self.unita_registrate = []

    def registra_unita(self, unita):
        self.unita_registrate.append(unita)
        print(f"Registrata unità: {unita.nome}")

    def mostra_unita(self):
        print("Unità registrate:")
        for unita in self.unita_registrate:
            print(f"- {unita.nome} ({unita.__class__.__name__})")

    def dettagli_unita(self, nome_unita):
        for unita in self.unita_registrate:
            if unita.nome == nome_unita:
                print(f"Dettagli per {nome_unita}:")
                print(f"  Tipo: {unita.__class__.__name__}")
                print(f"  Numero soldati: {unita.numero_soldati}")
                return
        print(f"Nessuna unità trovata con il nome '{nome_unita}'.")
