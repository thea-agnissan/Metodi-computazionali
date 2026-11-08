import numpy as np

# Decido di passare la distanza del pianeta dal Sole come parametro (sono dati tabulati)
class pianeta:
    def __init__(self, nome, massa, raggio, distanza_sole):
        self.nome = nome
        self.massa = massa  # in kg
        self.raggio = raggio  # in km
        self.distanza_sole = distanza_sole  # in UA (Unità Astronomiche)

# Operatore minore di (<)
    def __lt__(self, other):
        if not isinstance(other, pianeta):
            return NotImplemented
        return self.distanza_sole < other.distanza_sole

    # Operatore maggiore di (>)
    def __gt__(self, other):
        if not isinstance(other, pianeta):
            return NotImplemented
        return self.distanza_sole > other.distanza_sole

    # Rappresentazione testuale dell'oggetto per una stampa pulita
    def __repr__(self):
        return f"Nome: {self.nome}, Massa : {self.massa} kg, Raggio : {self.raggio} km , Distanza dal Sole: {self.distanza_sole} UA"