from DataFruta_V1 import AnaliseDados
import random
class ListaSalarios(AnaliseDados):

    def __init__(self, lista = None):
        super().__init__(type(float))
        for i in lista:
            if type(i) != float:
                raise Exception ("Tipo inválido para salário") 
        self.__lista = lista
        
    @property
    def lista(self):
        return self.__lista.copy()
    
    def addSalario(self):
        print("Informe o salário")
        try:
            salario = float(input())
            self.__lista.append(salario)     
        except Exception as ex:
            print(ex)
            
    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        try:
            for i in range(qtd):
                print(f"Digite o salário {i+1}:")
                valor = float(input())
                self.__lista.append(valor)
        except Exception as ex:
            print(ex)

    def mostraMediana(self):
        listaOrdenada = sorted(self.__lista)
        if listaOrdenada.__len__() % 2 == 0:
            resultado = ListaSalarios.calculaMedia(listaOrdenada[(listaOrdenada.__len__()//2)-1], listaOrdenada[(listaOrdenada.__len__()//2)])
        else:
            resultado = listaOrdenada[listaOrdenada.__len__() // 2]
        return resultado
    
    def mostraMediaAritmetica(self):
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
    
    def mostraVarianciaPopulacional(self):
        media = self.mostraMediaAritmetica()
        soma = 0
        for i in self.__lista:
            soma += (i - media) ** 2
        return (soma/len(self.__lista))
    
    def mostraVarianciaAmostral(self):
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
    
    def reajusteDezPorcento(self):
        for i in map((lambda s : s + s*0.1), self.__lista):
            print(i)
    
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
    
    def geraListaSalario(n, salarioMin = 1320, salarioMax = 13200):
        salarios = []
        for i in range(n):
            salarios.append(random.uniform(salarioMin, salarioMax))
        lista = ListaSalarios(salarios)
        return lista