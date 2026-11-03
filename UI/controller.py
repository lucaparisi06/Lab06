import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

    # Altre Funzioni Event Handler
    def mostra_strumenti(self, e):
        self._view.lista_strumenti.controls.clear()
        strumenti = self._model.get_strumenti()
        if strumenti is None or len(strumenti) == 0:
            self._view.show_alert("Non ci sono strumenti nel database")
            return
        for s in strumenti:
            self._view.lista_strumenti.controls.append(ft.Text(str(s)))
        self._view.update()

    def cerca_strumenti(self, e):
        tipo_strum_cercato = self._view.input_tipo_strumento.value
        if tipo_strum_cercato is None or tipo_strum_cercato.strip() == "":
            self._view.show_alert("Si prega di inserire un tipo di strumento valido")
            return
        self._view.lista_strumenti_ricerca.controls.clear()
        strumenti_trovati = self._model.cerca_strumenti_per_tipo(tipo_strum_cercato)
        if strumenti_trovati is None or len(strumenti_trovati) == 0:
            self._view.show_alert(f"Nessuno strumento trovato per il tipo '{tipo_strum_cercato}'")
            return
        for s in strumenti_trovati:
            self._view.lista_strumenti_ricerca.controls.append(ft.Text(str(s)))
        self._view.update()