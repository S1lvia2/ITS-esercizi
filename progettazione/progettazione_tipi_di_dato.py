class CodiceFiscale:
    def __init__(self, valore: str):
        self.valore = valore.upper()

    def __eq__(self, other):
        return isinstance(other, CodiceFiscale) and self.valore == other.valore

    def __hash__(self):
        return hash(self.valore)

    def __repr__(self):
        return f"CodiceFiscale('{self.valore}')"


class PartitaIVA:
    def __init__(self, valore: str):
        self.valore = valore

    def __eq__(self, other):
        return isinstance(other, PartitaIVA) and self.valore == other.valore

    def __hash__(self):
        return hash(self.valore)

    def __repr__(self):
        return f"PartitaIVA('{self.valore}')"


class Indirizzo:
    def __init__(self, via: str, citta: str):
        self.via = via
        self.citta = citta

    def __eq__(self, other):
        return isinstance(other, Indirizzo) and self.via == other.via and self.citta == other.citta

    def __hash__(self):
        return hash((self.via, self.citta))

    def __repr__(self):
        return f"Indirizzo('{self.via}', '{self.citta}')"




class Direttore:
    def __init__(self, nome: str, cognome: str, data_nascita: str, anni_servizio: int, cf: CodiceFiscale):
        self.nome = nome
        self.cognome = cognome
        self.data_nascita = data_nascita
        self.anni_servizio = anni_servizio
        self.cf = cf

    def __eq__(self, other):
        return isinstance(other, Direttore) and self.cf == other.cf

    def __hash__(self):
        return hash(self.cf)

    def __repr__(self):
        return f"Direttore({self.nome} {self.cognome}, CF={self.cf})"


class Fornitore:
    def __init__(self, ragione_sociale: str, partita_iva: PartitaIVA, indirizzo: Indirizzo, telefono: str, email: str):
        self.ragione_sociale = ragione_sociale
        self.partita_iva = partita_iva
        self.indirizzo = indirizzo
        self.telefono = telefono
        self.email = email

    def __eq__(self, other):
        return isinstance(other, Fornitore) and self.partita_iva == other.partita_iva

    def __hash__(self):
        return hash(self.partita_iva)

    def __repr__(self):
        return f"Fornitore('{self.ragione_sociale}', PI={self.partita_iva})"
