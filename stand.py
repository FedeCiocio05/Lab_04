class Stand:
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.__codice = codice
        self.__superficie = superficie
        self.__padiglione = padiglione
        self.__prezzo_base = prezzo_base

        # per gestire la parte dopo
        self.__disponibile = True
        self.__espositore = None

    def calcola_prezzo(self):
        return self.__prezzo_base

    def __str__(self):
        stato = "Disponibile" if self.__disponibile else "Occupato"

        return f'{self.__codice}: {self.__superficie} mq - Padiglione {self.__padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}'