class LogicGate:

    def __init__(self,n):
        self.label = n # rótulo interno
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n) #chamada explicita do construtor da classe pai

        self.entradaA = None
        self.entradaB = None
    
    def getEntradaA(self):
        if self.entradaA == None:
            return int(input('Digite a entrada do Pino A para a porta ' + self.getLabel() + '-->'))
        else:
            return self.entradaA.getFrom().getOutput()

    def getEntradaB(self):
        if self.entradaB == None:
            return int(input('Digite a entrada do Pino B para a porta ' + self.getLabel() + '-->'))
        else:
            return self.entradaB.getFrom().getOutput()

    def setNextEntrada(self,source):
        if self.entradaA == None:
            self.entradaA = source
        elif self.entradaB == None:
            self.entradaB = source
        else:
            raise RuntimeError('Erro: NÃO HÁ ENTRADAS DE PINO LIVRES!')    

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n) #chamada explicita do construtor da classe pai

        self.entrada = None

    def getEntrada(self):
        if self.entrada == None:
            return int(input('Digite a entrada do Pino para a porta ' + self.getLabel() + '-->'))
        else:
            return self.entrada.getFrom().getOutput()

    def setNextEntrada(self, source):
        if self.entrada == None:
            self.entrada = source
        else:
            return RuntimeError('Erro: NÃO HÁ ENTRADA DE PINO LIVRE!')

class AndGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getEntradaA()
        b = self.getEntradaB()

        return 1 if a == 1 and b == 1 else 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getEntradaA()
        b = self.getEntradaB()

        return 0 if a == 0 and b == 0 else 1

class NotGate(UnaryGate):
    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):

        entrada = self.getEntrada()

        return 1 if entrada == 0 else 0

class Connector:
    def __init__(self, fgate, tgate): #valores fluem da saida de uma porta para a entrada de outra porta
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextEntrada(self) #  metodo importante q permite que cada togate escolha a linha de entrada apropriada

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate


def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
    
