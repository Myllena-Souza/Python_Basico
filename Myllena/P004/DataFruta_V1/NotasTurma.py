import numpy as np

class NotasTurma:
    def __init__(self, nAlunos = 30, nCreditos = 3):
        self.notas = np.zeros((nAlunos, nCreditos))
    
    def leNotas(self):
        for i in range(len(self.notas)):
            for k in range(len(self.notas[0])):
                print("Informe a nota do crédito " + str(k+1) + " do aluno " + str(i+1))
                nota = float(input())
                self.notas[i,k] = nota
                
    def mediaTurma(self):
    
    