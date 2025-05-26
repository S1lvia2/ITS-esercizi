from datetime import date

class Impiegato:
    def _init_(self, nome: str, cognome: str, nascita: date, stipendio: float):
        self._nome = nome
        self._cognome = cognome
        self._nascita = nascita
        self._stipendio = stipendio
    
    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_cognome(self, cognome):
        self._cognome = cognome

    def get_cognome(self):
        return self._cognome

    def set_nascita(self, nascita):
        self._nascita = nascita

    def get_nascita(self):
        return self._nascita

    def set_stipendio(self, stipendio):
        self._stipendio = stipendio

    def get_stipendio(self):
        return self._stipendio

    

class Dipartimento:
    def _init_(self, nome: str, telefono: list, indirizzo=None):
        self._nome = nome
        self._telefono = telefono
        self._indirizzo = indirizzo
    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome
    
    def set_telefono(self, telefono):
        self._telefono = telefono

    def get_telefono(self):
        return self._telefono
    
    def set_indirizzo(self, indirizzo):
        self._indirizzo = indirizzo
    
    def get_indirizzo(self):
        return self._indirizzo

    


class Progetto:
    def _init_(self, nome: str, budget: float):
        self._nome = nome
        self._budget = budget

    def set_nome(self, nome):
        self._nome = nome

    def get_nome(self):
        return self._nome

    def set_budget(self, budget):
        self._budget = budget

    def get_budget(self):
        return self._budget

    

class Afferenza:
    def _init_(self, data_afferenza: date):
        self._data_afferenza = data_afferenza

    def set_data_afferenza(self, data):
        self._data_afferenza = data
        
    def get_data_afferenza(self):
        return self._data_afferenza

    