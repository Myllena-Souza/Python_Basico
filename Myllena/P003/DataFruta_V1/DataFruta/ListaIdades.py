from DataFruta_V1 import AnaliseDados
import random
class ListaIdades(AnaliseDados):
    
    def __init__(self, lista = None):
        super().__init__(type(int))
        for i in lista:
            if type(i) != int:
                raise Exception ("Idade invalida")
        self.__lista = lista
        
    @property
    def lista(self):
        return self.__lista.copy()
    
    def addIdade(self):
        print("Informe a idade")
        try:
            idade = int(input())
            self.__lista.append(idade)
        except Exception as ex:
            print(ex)
            
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de idades?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite a idade {i+1}:")
                valor = int(input())
                self.__lista.append(valor)
        except Exception as ex:
            print(ex)
            
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
            
    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaIdades.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def mostraDesvPadPopulacional(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista)) ** 1/2
    
    def mostraDesvPadAmostral(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista) - 1) ** 1/2
    
    def mostraVariAmostral(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista) - 1)
    
    def mostraMenor(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[0]
    
    def mostraMaior(self):
        listaOrdenada = sorted(self.__lista)
        return listaOrdenada[listaOrdenada.__len__() - 1]

    def listarEmOrdem(self):
        listaOrdenada = sorted(self.__lista)
        for i in listaOrdenada:
            print(str(i))

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
    
    def geraListaIdade(n, idadeMin = 18, idadeMax = 65):
        idades = []
        for i in range(n):
            idades.append(random.randint(idadeMin, idadeMax))
        lista = ListaIdades(idades)
        return lista
