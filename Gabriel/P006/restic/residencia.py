import pandas as pd
from trilha import Trilha

class Residencia():
    def __init__(self):
        self.residentes = pd.DataFrame([])
    
    def addTrilha(self, trilha):
        if not isinstance(trilha, Trilha):
            raise Exception("Tipo invalido")
        self.__residentes = pd.concat([self.__residentes, trilha.residentes])

