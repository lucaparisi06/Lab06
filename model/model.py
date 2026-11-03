from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        connessione = get_connection()
        if connessione is None:
            return None
        raccolta_strumenti = []
        cur = connessione.cursor(dictionary=True)
        query = "SELECT * FROM strumento"
        try:
            cur.execute(query)
            for riga in cur:
                mio_strumento = Strumento(
                    codice=riga['codice'],
                    tipo=riga['tipo'],
                    marca=riga['marca'],
                    anno_acquisto=riga['anno_acquisto'],
                    valore=riga['valore'],
                    disponibile=riga['disponibile']
                )
                raccolta_strumenti.append(mio_strumento)
        except Exception as e:
            print("Errore: ", e)
            return None
        finally:
            cur.close()
            connessione.close()
        return raccolta_strumenti

    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        connessione = get_connection()
        if connessione is None:
            return None
        strumenti_trovati = []
        cur = connessione.cursor(dictionary=True)
        query = "SELECT * FROM strumento WHERE tipo = %s"
        try:
            cur.execute(query, (tipo,))
            for riga in cur:
                mio_strumento = Strumento(
                    codice=riga['codice'],
                    tipo=riga['tipo'],
                    marca=riga['marca'],
                    anno_acquisto=riga['anno_acquisto'],
                    valore=riga['valore'],
                    disponibile=riga['disponibile']
                )
                strumenti_trovati.append(mio_strumento)
        except Exception as e:
            print("Errore: ", e)
            return None
        finally:
            cur.close()
            connessione.close()
        return strumenti_trovati