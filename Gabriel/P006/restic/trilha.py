import pandas as pd
from  .residente import Residente


class Trilha:
    def __init__(self,nomeTrilha):
        self.__residentes = pd.DataFrame([])
        self.__nomeTrilha = nomeTrilha

    
    @property
    def residentes(self):
        return self.__residentes.copy

    
    def addResidente(self, residente=None):
        if  not isinstance(residente,Residente):
            residente = Residente().entrevista()
        try:
           dataFrameResidente = residente.dataFrame.T
           dataFrameResidente["Trilha"] = [self.__nomeTrilha]
           self.__residentes = pd.concat([self.__residentes, dataFrameResidente])
        except Exception as e:
            print(e)
    
    
