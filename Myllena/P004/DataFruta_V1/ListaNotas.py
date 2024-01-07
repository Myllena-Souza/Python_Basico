from DataFruta_V1.analiseDados import AnaliseDados
import numpy as np
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
    
    def addNota(self):
        print("Informe a Nota")
        size = len(self.__lista)
        newLista = np.zeros(size+1)
        newLista [:-1] = self.__lista
        try:
            nota = float(input())
            self.__lista = newLista
            self.__lista[-1] = nota
        except Exception as ex:
            print(ex)
            
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de notas?")
        qtd = int(input())
        self.__lista = np.zeros(qtd)
        try:
            for i in range(qtd):
                print(f"Digite a nota {i+1}:")
                valor = float(input())
                self.__lista[i] = valor
        except Exception as ex:
            print(ex)
    
    def mostraMedia(a, b):
        media = (a + b) / 2
        return media

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaNotas.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def calculaMaior(self):
        return self.__lista.max()
    
    def calculaMenor(self):
        return self.__lista.min()
    
    def mostraMediaAritmetrica(self):
        
        return self.__lista.mean()
    
    def mostraMediaGeometrica(self):
        y = np.prod(self.__lista)
        return y ** (1/len(self.__lista))
    
    def mostraMediaHarmonica(self):
        y = 1/self.__lista
        y = np.sum(y)
        return len(self.__lista)/y
    
    def mostraDesvPadPopulacional(self):
        return self.__lista.std(ddof=0)
    
    def mostraDesvPadAmostral(self):
        return self.__lista.std(ddof=1)
    
    def mostraVariPopulacional(self):
        return self.__lista.var(ddof=0)
    
    def mostraVariAmostral(self):
        return self.__lista.var(ddof=1)
    
    def maiorque(self, n):
        filtro = self.__lista > n
        maior = self.__lista[filtro]
        return maior
    
    def menorQue(self, n):
        filtro = self.__lista < n
        menor = self.__lista[filtro]
        return menor
    
    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        for i in listaOrdenada:
            print(str(i))
    
    def geraListaNotas(n, iMin = 0, iMax = 10):
        notas = [random.uniform(iMin, iMax) for _ in range(n)] 
        lista = ListaNotas(np.array(notas))
        return lista
    
    def aprovados(self, media):
        filtro = self.__lista >= media
        aprovados = self.__lista[filtro]
        return aprovados

    def reprovados(self, media):
        filtro = self.__lista < media
        reprovados = self.__lista[filtro]
        return reprovados
    
    def passarMaiorNotaPara10(self):
        nota = self.mostraMaior()
        self.__lista = (self.__lista * 10) / nota