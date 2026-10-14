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
    # TODO

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""

        def carica_file_dati(self, file_path):
            """Carica i dati (stand ed espositori) dal file"""

            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    reader = csv.reader(infile, delimiter=',')

                    for row in reader:  # per ogni riga nel file
                        try:
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

                        except IndexError:
                            # errore se la riga ha meno colonne del previsto
                            print('Attenzione: errore sugli indici, riga incompleta.')

                        except ValueError:
                            # errore se i valori non sono convertibili nel formato corretto
                            print('Attenzione: la riga contiene valori non validi.')

            except FileNotFoundError:
                # nel caso il file non esiste
                raise FileNotFoundError(f'Errore: il file {file_path} non esiste.')

            except Exception as errore:
                # altro errore non previsto
                print(f'Errore imprevisto: {errore}')
        # TODO

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        # TODO

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        # TODO

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        # TODO
