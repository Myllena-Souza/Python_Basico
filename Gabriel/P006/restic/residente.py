from datetime import datetime
import pandas as pd

class Residente:
    def __init__(self):
        print(pd.__version__)
        self.__cpf = None
        self.__anoNascimento = None
        self.__identificador = None
        self.__trilha = None
        self.__idade = None
        self.__formacao = None
        self.__formacaoGeral = None
        self.__formacaoEspecifica = None
        self.__andamentoGraduacao = None
        self.__anosFormado = None
        self.__experienciaPrevia = None
        self.__dataFrame = None

    @property
    def DataFrame(self):
        return self.__dataFrame.copy

    def setCpf(self, cpf):
            cpf = str(cpf)
            cpf = ''.join(digito for digito in cpf if digito.isdigit())
            if len(cpf)!=11:
                raise Exception("Quantidade de digítos númericos inválidos")
            self.__cpf = cpf
    
    def setAnoNascimento(self, anoNasc):
        anoAtual = datetime.today().year
        if anoNasc.isdigit():
            pass
        else:
            raise Exception("Ano invalido")
        _anoNascimento = abs(int(anoNasc))
        self.__anoNascimento = anoNasc
        self.__idade = anoAtual-_anoNascimento

    
    def setTrilha(self, indiceTrilha):
        trilhas = ["tic18Py","tic18Net","tic18Jav"]
        self.__trilha = trilhas[int(indiceTrilha)]


    def setIdentificador(self):
        self.__identificador = self.__trilha + self.__cpf[0:3] + str(self.__anoNascimento)[-2:]

    
    def setFormacao(self, formacao):
        formacao = int(formacao)
        if  formacao<0 or formacao>3:
            raise Exception("Formação inválida")
        self.__formacao = formacao
    
    def setFormacaoEspecifica(self, formacaoEspecifca):
        self.__formacaoEspecifica = str(formacaoEspecifca).lower()
        self.__formacaoGeral = int('eng' in self.__formacaoEspecifica)

    def setAndamentoGraduacao(self, andamentoGraduacao):
        self.__andamentoGraduacao = float(andamentoGraduacao)
        if  self.__andamentoGraduacao<=1:
            self.__andamentoGraduacao *=100

        if  self.__andamentoGraduacao<0:
            raise Exception("Valor inválido")


    def setAnosFormado(self,anosFormado):
        anosFormado = int(anosFormado)
        self.__anosFormado = anosFormado
    
    def setExperienciaPrevia(self, experienciaPrevia):
        self.__experienciaPrevia = bool(experienciaPrevia)

    def setdataFrame(self):     
        colunas = ["Identificador",
                   "Idade", 
                   "Formação", 
                   "Formação Geral", 
                   "Formação Específica", 
                   "Andamento da Graduação", 
                   "Anos de Formado", 
                   "Experiencia Previa"]
        
        dados = [self.__identificador,
                 self.__idade,
                 self.__formacao,
                 self.__formacaoGeral,
                 self.__formacaoEspecifica,
                 self.__andamentoGraduacao,
                 self.__anosFormado,
                 self.__experienciaPrevia]
        self.__dataFrame = pd.DataFrame(dados,index=colunas)


    def entrevista(self):
        print(50*"--")
        cpf = input("Digite seu CPF: ")
        try:
            self.setCpf(cpf)
            print(f"CPF: {self.__cpf}")
        except Exception as e:
            print(e)

        print(50*"--")
        anoNasc = input("Digite o ano de nascimento: ")
        try:
            self.setAnoNascimento(anoNasc)
            print(f"Ano de Nascimento: {self.__anoNascimento}")
        except Exception as e:
            print(e)


        print(50*"--")
        for i,trilha in enumerate(["Python",".Net","Java"]):
            print(str(i)+" - "+trilha)
        try:
            indiceTrilha = input("Digite o indice corespondente a trilha: ")
            self.setTrilha(indiceTrilha)
            print(f"Trilha: {self.__trilha}")
        except Exception as e:
            print(e)


        print(50*"--")
        try:

            self.setIdentificador()
            print(self.__identificador)
        except Exception as e:
            print(e)

        print(50*"--")
        for i,trilha in enumerate(["Tecnico","Tecnico com Superior Incompleto","Superior Incompleto","Superior Completo"]):
            print(str(i)+" - "+trilha)
        formacao = input("Digite o indice corespondente a sua formação: ")
        try:
            self.setFormacao(formacao)
            print(f"Formação: {self.__formacao}")
        except Exception as e:
            print(e)

        print(50*"--")
        formacaoEsp = input("Digite o nome da sua área de formação especifica: ")
        try:
            self.setFormacaoEspecifica(formacaoEsp)
            print(f"Formação geral: {self.__formacaoGeral}, Formação Específica: {self.__formacaoEspecifica}")
        except Exception as e:
            print(e)

        if self.__formacao == 1 or self.__formacao == 2:
            print(50*"--")
            porcentagem = input("Digite a porcentagem de conclusão da gradução (0-100)%: ")
            try:
                self.setAndamentoGraduacao(porcentagem)
                print(f"Porcentagem de conclusão da graduação: {self.__andamentoGraduacao}")
            except Exception as e:
                print(e)
        
        if self.__formacao == 3:
            print(50*"--")
            anos = input("Digite a quantidade de anos que você concluiu a grauduação: ")
            try:
                self.setAnosFormado(anos)
                print(f"Anos que concluiu a graduação: {self.__anosFormado}")
            except Exception as e:
                print(e)
        
        print(50*"--")
        resposta = input("Voce possuia expeciencia previa com programação? (s/n): ")
        try:
            self.setExperienciaPrevia( resposta[0].lower() == "s" )
            print(f"Experiencia Previa com Programação: {self.__experienciaPrevia}")
        except Exception as e:
            print(e)
        
        self.setdataFrame()
    
    def imprimeDataFrame(self):
        print(self.__dataFrame)


        
        

        

