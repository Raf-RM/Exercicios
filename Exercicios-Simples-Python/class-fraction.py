# -- Criando uma clase Fraction que constroi um numeral fração do tipo 1/3

# -- Para reduzir as frações vamos contruir um método que calcule o MDC
def mdc(a, b):
    while a%b != 0:
        a_velho = a
        b_velho = b

        a = b_velho
        b = a_velho%b_velho

    return b


class Fraction:
    def __init__(self, numerador, denominador):
        self.num = numerador
        self.den = denominador

# -- Definindo uma função show para podermos imprimir o objeto em Fraction como string    
    def show(self):
        print(self.num, '/', self.den)

# -- Subscrevendo a fução str do python para funcionar em nossa classe
    def __str__(self):
        return str(self.num)+'/'+str(self.den)

# -- Subscrevendo a função adição para fazer adição das nossas frações
    def __add__(self, outro):
        novo_num  = self.num * outro.den + self.den * outro.num
        novo_den = self.den * outro.den
        d_comum = mdc(novo_num, novo_den)
        return Fraction(novo_num//d_comum, novo_den//d_comum)

# -- Subscrevendo o método de igualdade (__eq__) para que possamos criar igualdade profunda
    def __eq__(self, outro):
        primeiro = self.num * outro.den
        segundo = self.den * outro.num

        return primeiro == segundo

# -- Vamos implementar agora as funções *, /, e -
# -- Implementando a função de multiplicação
    def __mul__(self, outro):
        novo_num = self.num * outro.num
        novo_den = self.den * outro.den
        d_comum = mdc(novo_num, novo_den)
        return Fraction(novo_num//d_comum, novo_den//d_comum)

# -- Implementando a função de divisão
    def __truediv__(self, outro):
        novo_num = self.num * outro.den
        novo_den = self.den * outro.num
        d_comum = mdc(novo_num, novo_den)
        return Fraction(novo_num//d_comum, novo_den//d_comum)
# -- Implementando a função subtração
    def __sub__(self, outro):
        novo_num = self.num * outro.den - self.den * outro.num
        novo_den = self.den * outro.den
        d_comum = mdc(novo_num, novo_den)
        return Fraction(novo_num//d_comum, novo_den//d_comum)

# -- Vamos implementar agora as função de maior e menor (__gt__) e (__lt__) respectivamente
#    (FALTA IMPLEMENTAR)


myFraction = Fraction(3, 5)
myFraction.show()
print(myFraction)
print('Eu comprei', myFraction,'das ações da empresa!')

f1 = Fraction(3,4)
f2 = Fraction(1,2)
f3 = f1.__add__(f2)
f5 = f1 + f2
print('f3 =',f3)
print('f5 =', f5)
f4 = f1.__mul__(f2)
f6  = f1 * f2
print('f4 =',f4)
print('f6 =',f6)
f7 = f1.__truediv__(f2)
f8 = f1/f2
print('f7 =',f7)
print('f8 =',f8)
f9 = f1.__sub__(f2)
f10 = f1 - f2
print('f9 =',f9)
print('f10 =',f10)