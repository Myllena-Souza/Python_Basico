from ..resources import AnaliseDados
import random
import numpy as np
class ListaSalarios(AnaliseDados):

    def __init__(self, lista=None):
        super().__init__(type(float))
        if(lista != None):
            for i in lista:
                if type(i) != float:
                    raise Exception("Tipo inválido para salário")
            self.__lista = np.array(lista)
        else:
            self.__lista = np.array(lista)

    @property
    def lista(self):
        return self.__lista.copy()
    
    def addSalario(self):
        print("Informe o salário")
        try:
            salario = float(input())
            salariosExistentes = self.__lista.copy()
            self.__lista = np.zeros(self.__lista.size+1)
            self.__lista[:-2] = salariosExistentes
            self.lista[-1] = salario           
        except Exception as e:
            print(e)      

    def entradaDeDados(self):
        print("Quantos elementos existirão na lista de salários?")
        qtd = int(input())
        self.__lista = np.zeros(qtd)
        try:
            for i in range(qtd):
                print(f"Digite o salário {i+1}:")
                valor = float(input())
                self.__lista[i] = valor
        except Exception as e:
            print(e) 

    def mostraMediana(self):
        return np.median(self.__lista)
    
    def mostraMedianaInferior(self):
        
        listaInf = np.sort(self.lista)[:self.__lista.size//2]
        return np.median(listaInf)
            
    def mostraMedianaSuperior(self):
        listaSup = np.sort(self.lista)[self.__lista.size//2:]
        return np.median(listaSup)


    def mostraMediaAritmetica(self):
        return np.mean(self.__lista)


    def mostraMediaGeometrica(self):
        produtorio = np.prod(self.__lista)
        return produtorio**(1/self.__lista.size)
    
    def mostraMediaHarmonica(self):
        inverso = 1/self.__lista
        return self.__lista.size/np.sum(inverso)
    
    def mostraDesvioPadraoPopulacional(self):
        return np.std(self.__lista)
    
    def mostraDesvioPadraoAmostral(self):
        return np.std(self.__lista,ddof=1)
    
    def mostraVarianciaPopulacional(self):
        return np.std(self.__lista)
    
    def mostraVarianciaAmostral(self):
        return np.var(self.__lista,ddof=1)
    
    def mostraMenor(self):
        return np.min(self.__lista)

    def mostraMaior(self):
        return np.max(self.__lista)
    
    def reajusteDezPorcento(self):
        self.__lista = self.__lista*1.1
    
    def listarEmOrdem(self):
        listaOrdenada = np.sort(self.lista)
        for i in listaOrdenada:
            print(str(i))
    
    def __str__(self):
        listaStr = []
        separador = ", "
        for i in self.__lista:
            listaStr.append(str(i))
        string = separador.join(listaStr)
        return string
    

    def geraListaSalario(n, iMin = 1320, iMax = 13200):
        salarios = []
        for i in range(n):
            salarios.append(random.uniform(iMin, iMax))
        lista = ListaSalarios(salarios)
        return lista