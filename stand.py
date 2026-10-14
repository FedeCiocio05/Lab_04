class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base

        # per gestire la parte dopo
        self.__disponibile = True
        self.__espositore = None

    @property
    def disponibile(self):
        # leggo se lo stand è disponibile
        return self.__disponibile

    @property
    def espositore(self):
        # leggo l'espositore assegnato allo stand
        return self.__espositore

    @espositore.setter
    def espositore(self, nuovo_espositore):
        # assegno l'espositore allo stand
        self.__espositore = nuovo_espositore

        # aggiorno la disponibilità
        if nuovo_espositore is None:
            self.__disponibile = True
        else:
            self.__disponibile = False

    def calcola_prezzo(self):
        return self.__prezzo_base

    def __str__(self):
        stato = "Disponibile" if self.__disponibile else "Occupato"
        return f'{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}'

    def __lt__(self, other):
        return self.calcola_prezzo() < other.calcola_prezzo()