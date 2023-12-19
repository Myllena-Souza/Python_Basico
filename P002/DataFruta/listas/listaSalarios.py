from .analiseDados import AnaliseDados
from random import random

class ListaSalarios(AnaliseDados):

    def __init__(self,lista = []):
        super().__init__(type(float))
        for i in lista:
            if type(i) != float:
                raise Exception("Tipo inválido para salário")
        self.__lista = lista.copy()  

    def getLista(self):
        return self.__lista.copy()
    
    def addSalario(self):
        print("Informe o salário")
        try:
            salario = float(input())
            self.__lista.append(salario)
        except Exception as e:
            print(e) 

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite o salário {i+1}:")
                valor = float(input())
                self.__lista.append(valor)
        except Exception as e:
            print(e) 

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado   

    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]

    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]
    
    def reajusteDezPorcento(self):
        for i in map((lambda s : s + s*0.1), self.__lista):
            print(i)
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    
    def calculaMedia(a, b):
        media = (a + b) / 2
        return media
    
    def geraListaSalarios(n,sMin=1320.0,sMax=13200.0):
        salarios = [(sMin + random()*(sMax-sMin)) for _ in range(n)]
        return ListaSalarios(salarios)

