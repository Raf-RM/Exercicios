# -- Criando uma clase Fraction que constroi um numeral fração do tipo 1/3

class Fraction:
    def __init__(self, numerador, denominador):
# -- Para reduzir as frações vamos contruir um método que calcule o MDC 
        if type(numerador) == type(denominador) == int:
            if numerador < 0 and denominador < 0:
                a = abs(numerador)
                b = abs(denominador)
            elif numerador >= 0 and denominador < 0:
                a = - numerador
                b = abs(denominador) 
            else:
                a = - numerador
                b = denominador                                
            while a%b != 0:
                a_velho = a
                b_velho = b

                a = b_velho
                b = a_velho%b_velho
                
            self.num = numerador//b
            self.den = denominador//b
        else:
            raise RuntimeError('O numerador e o denominador da fração devem ser números inteiros!')

    def getNum(self):
        return self.num
    
    def getDen(self):
        return self.den

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
        return Fraction(novo_num, novo_den)

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
        return Fraction(novo_num, novo_den)

# -- Implementando a função de divisão
    def __truediv__(self, outro):
        novo_num = self.num * outro.den
        novo_den = self.den * outro.num
        return Fraction(novo_num, novo_den)

# -- Implementando a função subtração
    def __sub__(self, outro):
        novo_num = self.num * outro.den - self.den * outro.num
        novo_den = self.den * outro.den
        return Fraction(novo_num, novo_den)

# -- Vamos implementar agora as função de maior e menor (__gt__) e (__lt__) respectivamente
    def __gt__(self, outro):
        return True if ((self.num/self.den) - (outro.num/outro.den)) > 0 else False
    
    def __lt__(self, outro):
        return True if ((self.num/self.den) - (outro.num/outro.den)) < 0 else False

# -- Vamos implementar agora as função de maior ou igual, menor ou igual e não igual 
#    (__ge__), (__le__) e (__ne__) respectivamente
    def __ge__(self, outro):
        return True if ((self.num/self.den) - (outro.num/outro.den)) >= 0 else False 

    def __le__(self, outro):
        return True if ((self.num/self.den) - (outro.num/outro.den)) <= 0 else False   

    def __ne__(self,outro):
        return True if ((self.num/self.den) - (outro.num/outro.den)) == 0 else False    




myFraction = Fraction(3, 5)
myFraction.show()
print(myFraction)
print('Eu comprei', myFraction,'das ações da empresa!')

f1 = Fraction(-3,-4)
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
f11 =  f2.__gt__(f1)
f12 = f2 < f1
print('f11 =', f11)
print('f12 =', f12)
f1 = Fraction(1,2)
f13 = f1.__ge__(f2)
f14 = f1 <= f2
f15 = f1 == f2
f1 = Fraction(3,4)
f16 = f1 == f2
print('f13 =', f13)
print('f14 =', f14)
print('f15 =', f15)
print('f16 =', f16)
print('Numerador = ',f1.getNum(),'e Denominador =',f1.getDen())



f1 = Fraction(0.5,8)
