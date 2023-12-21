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
    
    def addNota(self):
        print("Informe a Nota")
        try:
            nota = float(input())
            self.__lista.append(nota)
        except Exception as ex:
            print(ex)
            
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de notas?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite a nota {i+1}:")
                valor = float(input())
                self.__lista.append(valor)
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
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]
    
    def calculaMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]
    
    def mostraMediaAritmetrica(self):
        y = sum(self.__lista)
        return y/len(self.__lista)
    
    def mostraMediaGeometrica(self):
        y = 1
        for i in self.__lista:
            y *= i
        return y ** (1/len(self.__lista))
    
    def mostraMediaHarmonica(self):
        y = 0
        for i in self.__lista:
            y += 1/i
        return len(self.__lista)/y
    
    def mostraDesvPadPopulacional(self):
        variacia = self.mostraVariPopulacional()
        return  variacia  ** 1/2
    
    def mostraDesvPadAmostral(self):
        variacia = self.mostraVariAmostral()
        return  variacia  ** 1/2
    
    def mostraVariPopulacional(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista))
    
    def mostraVariAmostral(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista) - 1)
    
    def maiorque(self, n):
        maior = [notas for notas in self.__lista if notas > n]
        return maior
    
    def menorQue(self, n):
        menor = [notas for notas in self.__lista if notas < n]
        return menor
    
    def aprovados(self, media):
        aprovados = [notas for notas in self.__lista if notas >= media]
        return aprovados

    def reprovados(self, media):
        reprovados = [notas for notas in self.__lista if notas < media]
        return reprovados
    
    def passarMaiorNotaPara10(self):
        nota = self.mostraMaior()
        self.__lista = [(notas*10)/nota for notas in self.__lista]