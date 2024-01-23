from .analiseDados import AnaliseDados
from random import randint
class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = []):
        super().__init__(type(int))
        for i in lista:
            if type(i) != int:
                raise Exception("Tipo inválido para idade")
        self.__lista = lista.copy()

    def getLista(self):
        return self.__lista.copy()
    
    def addIdade(self):
        try:
            idade = int(input())
            self.__lista.append(idade)
        except Exception as e:
            print(e) 
    
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite a idade {i+1}:")
                valor = int(input())
                self.__lista.append(valor)
        except Exception as e:
            print(e) 
    
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado    
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]

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

    def geraListaIdade(n,iMin=18,iMax=65):
        idades = [randint(iMin,iMax) for _ in range(n)]
        return ListaIdades(idades)

    def mediaAritimetica(self):
        return sum(self.__lista)/len(self.__lista)
    
    def mediaGeometrica(self):
        media = 1.0
        for item in self.__lista:
            media *= item
        return media**(1.0/self.__lista.__len__())
    
    def mediaHarmonica(self):
        divisor = 1
        for item in self.__lista:
            divisor += 1/item
        return len(self.__lista)/divisor

    def medianaInferior(self):
        listaOrdenada = sorted(self.__lista)
        listaOrdenada = listaOrdenada[0:listaOrdenada.__len__()//2]
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado 
    
    def medianaSuperior(self):
        listaOrdenada = sorted(self.__lista)
        listaOrdenada = listaOrdenada[listaOrdenada.__len__()//2:]
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def varianciaPopulacional(self):
        variancia = 0
        media = self.mediaAritimetica()
        for item in self.__lista:
            variancia += (item-media)**2
        return (variancia/self.__lista.__len__())

    def desvioPadraoPopulacional(self):
        return self.varianciaPopulacional()**1/2
    
    def varianciaAmostral(self):
        variancia = 0
        media = self.mediaAritimetica()
        for item in self.__lista:
            variancia += (item-media)**2
        return (variancia/(self.__lista.__len__()-1))
    
    def desvioPadraoAmostral(self):
        return self.varianciaAmostral()**1/2