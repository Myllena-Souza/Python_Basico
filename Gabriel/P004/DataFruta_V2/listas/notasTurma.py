import numpy as np
class NotasTurma:
    def __init__(self, nAlunos = 30, nCreditos = 3):
        self._notas = np.zeros((nAlunos//1,nCreditos//1))

    def notasAleatorias(self):
        self._notas = np.random.uniform(low = 0, high = 10, size = self._notas.shape)
    
    def leNotas(self):
        nAlunos, nCreditos = self._notas.shape
        for aluno in range(nAlunos):
            for nota in range(nCreditos):
                try:
                    print("Digite a nota ",nota," do aluno ",aluno)
                    n = float(input())
                    self._notas[aluno,nota] = n
                except Exception as e:
                    print(e) 
    
    def mediaTurma(self):
        return np.mean(self._notas)
    
    def mediaAluno(self, index = 0):
        return np.mean(self._notas[index,:])

    def mediaAvaliaçao(self, index = 0):
        return np.mean(self._notas[:,index])
    
    def quantAprovados(self):
        media = np.mean(self._notas,axis=1)
        return np.count_nonzero(media>6)
    
    def quantReprovados(self):
        media = np.mean(self._notas,axis=1)
        return np.count_nonzero(media<6)

    def menorNota(self):
        _, nCreditos = self._notas.shape
        menorNota = np.zeros(nCreditos+1)
        menorNota[:nCreditos] = np.min(self._notas,axis=0)
        media = np.mean(self._notas,axis=1)
        menorNota[-1] = np.min(media)
        return menorNota
    def maiorNota(self):
        _, nCreditos = self._notas.shape
        maiorNota = np.zeros(nCreditos+1)
        maiorNota[:nCreditos] = np.max(self._notas,axis=0)
        media = np.mean(self._notas,axis=1)
        maiorNota[-1] = np.max(media)
        return maiorNota

    def __str__(self):
        return str(self._notas)