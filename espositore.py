class Espositore:
    def __init__(self, codice, nome, cognome):
        self.__codice = codice
        self.__nome = nome
        self.__cognome = cognome

    def __str__(self):
        return f'{self.__codice}: {self.__nome} {self.__cognome}'

    def __eq__(self, other):
        # controllo che l'altro oggetto sia un espositore
        if not isinstance(other, Espositore):
            return NotImplemented
        return self.__codice == other.__codice