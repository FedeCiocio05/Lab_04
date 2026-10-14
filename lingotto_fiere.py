import csv
from stand import Stand
from standPremium import StandPremium
from standPreseExtra import StandPreseExtra
from espositore import Espositore


class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self.__nome = nome

        self.__stand = {}
        self.__espositori = {}
        # TODO

    """Aggiungere setter e getter se necessari"""
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuovo_nome):
        self.__nome = nuovo_nome
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open(file_path, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile, delimiter=',')

            for row in reader:  # per ogni riga nel file
                # salto le righe vuote
                if not row:
                    continue

                # estraggo il codice dalla prima colonna
                codice = row[0].strip()

                if codice.startswith('ST'):
                    # estraggo i singoli valori dalle colonne
                    superficie = float(row[1])
                    padiglione = int(row[2])
                    prezzo_base = float(row[3])

                    # creo un oggetto della tipologia corretta
                    if len(row) == 4:
                        stand = Stand(codice, superficie, padiglione, prezzo_base)

                    elif row[4].strip().isdigit():
                        numero_prese = int(row[4])
                        stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, numero_prese)

                    else:
                        posizione = row[4].strip()
                        stand = StandPremium(codice, superficie, padiglione, prezzo_base, posizione)

                    # aggiungo lo stand al dizionario
                    self.__stand[codice] = stand

                elif codice.startswith('ES'):
                    # estraggo i singoli valori dalle colonne
                    nome = row[1].strip()
                    cognome = row[2].strip()

                    # creo un oggetto Espositore con i dati della riga
                    espositore = Espositore(codice, nome, cognome)

                    # aggiungo l'espositore al dizionario
                    self.__espositori[codice] = espositore
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # controllo che lo stand esista
        if codice_stand not in self.__stand:
            raise ValueError(f'Lo stand {codice_stand} non esiste.')

        # controllo che l'espositore esista
        if codice_espositore not in self.__espositori:
            raise ValueError(f'Espositore {codice_espositore} non esistente.')

        # recupero gli oggetti dai dizionari
        stand = self.__stand[codice_stand]
        espositore = self.__espositori[codice_espositore]

        # controllo che lo stand sia disponibile
        if not stand.disponibile:
            raise ValueError(f'Lo stand {codice_stand} è già occupato.')

        # controllo che l'espositore non abbia già uno stand
        for altro_stand in self.__stand.values():
            if altro_stand.espositore == espositore:
                raise ValueError(f'Espositore {codice_espositore} già associato a uno stand.')

        # assegno l'espositore e aggiorno la disponibilità tramite il setter
        stand.espositore = espositore

        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # controllo se ci sono espositori
        if not self.__espositori:
            print('Non ci sono espositori registrati.')
            return

        # scorro tutti gli oggetti espositore
        for espositore in self.__espositori.values():
            codice_stand_assegnato = None

            # cerco uno stand associato all'espositore
            for codice_stand, stand in self.__stand.items():
                if stand.espositore == espositore:
                    codice_stand_assegnato = codice_stand
                    break

            # stampo l'espositore con l'eventuale stand assegnato
            if codice_stand_assegnato is None:
                print(f'{espositore} - Nessuno stand assegnato')
            else:
                print(f'{espositore} - Stand assegnato: {codice_stand_assegnato}')
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.__stand.values())
        # TODO
