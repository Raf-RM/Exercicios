class Pessoa:
    def __init__(self, nome, vinculo, registro):
        self.nome =  nome 
        self.vinculo = vinculo
        self.registro = registro

        self.output = None

    def getNome(self):
        return self.nome
    def getVinculo(self):
        return self.vinculo
    def getRegistro(self):
        return self.registro

class NovoCadastro(Pessoa):
    def __init__(self):
        nome = input('Nome completo: ')
        vinculo = input('Tipo de vínculo: ')
        registro = input('Número de registro: ')

        Pessoa.__init__(self, nome, vinculo, registro)





