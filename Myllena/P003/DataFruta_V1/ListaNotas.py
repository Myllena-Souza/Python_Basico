from DataFruta_V1.analiseDados import AnaliseDados
import random

class ListaNotas(AnaliseDados):
    
    def __init__(self, lista = None):
        super().__init__(type(float))
        for i in lista:
            if type(i) != float:
                raise Exception ("Nota inválida")
        self.__lista = lista
        
    @property
    def lista(self):
        return self.__lista.copy()
    
    def geraListaIdade(n, idadeMin = 18, idadeMax = 65):
        idades = []
        for i in range(n):
            idades.append(random.randint(idadeMin, idadeMax))
        lista = ListaNotas(idades)
        return lista
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaNotas.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def calculaMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]   
