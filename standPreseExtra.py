from stand import Stand

class StandPreseExtra(Stand):
    def __init__(self, codice, superficie, padiglione, prezzo_base, numeroPrese):
        super().__init__(codice, superficie, padiglione, prezzo_base)
        self.__numeroPrese = numeroPrese

    def calcola_prezzo(self):
        return super().calcola_prezzo() * (1 + 0.07 * self.__numeroPrese)

    def __str__(self):
        return f'{super().__str__()} - Prese aggiuntive: {self.__numeroPrese}'