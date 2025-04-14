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

class ControlloMilitare(Fanteria, Artiglieria, Cavalleria, SupportoLogistico, Ricognizione):
   
    def __init__(self):
        self.unita_registrate = {}  # chiave: nome unità, valore: oggetto

    def registra_unita(self, unita):
        self.unita_registrate[unita.nome] = unita
        print(f"Registrata unità: {unita.nome}")

    def mostra_unita(self):
        print("Unità registrate:")
        for unita in self.unita_registrate:
            print(f"- {unita.nome} )")

    def dettagli_unita(self, nome_unita):
        unita = self.unita_registrate.get(nome_unita)
        if unita:
            print(f"Dettagli per {nome_unita}:")
            print(f"  Numero soldati: {unita.numero_soldati}")
        else:
            print(f"Nessuna unità trovata con il nome '{nome_unita}'.")
            
class Esercito(ControlloMilitare):
    
    def __init__(self):
        self.controllo = {}  # chiave: id, valore: oggetto
    

    def registra_esercito(self, controllo):
        id = 0
        while(True):
            self.controllo[id] = controllo
            id = id + 1
            print(f"Registrata unità: {controllo.nome}")
            scelta = input("Vuoi continuare ad inserire un controllo nell'esercito? (s/n)").strip().lower()
            if scelta == "no":
                break

        
        
