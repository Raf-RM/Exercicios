# “methinks it is like a weasel”
from random import choice

def geraAleatorio(n):
    lista_alfabeto = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','x','w','y','z',
        ' ']
    lista_frase = []
    while n > 0:
        lista_frase.append(choice(lista_alfabeto))
        n -= 1
    #return ''.join(lista_frase)
    return lista_frase


def comparaFrase(frase_original, list_frase_gerada, n):
    list_frase_orig = [letra for palavra in frase_original for letra in palavra]
    compara = True
    cont_iguais = 0
    for i in range(n):
        if list_frase_gerada[i] == list_frase_orig[i]:
            cont_iguais += 1 
        else:
            compara = False
    return compara, cont_iguais

def inicia():
    frase_original = 'methinks it is like a weasel'
    n = len(frase_original)
    igual = False
    cont = 0
    maior_n_iguais = 0
    while not igual:
        list_frase_gerada = geraAleatorio(n)
        igual, n_iguais = comparaFrase(frase_original, list_frase_gerada, n)
        if n_iguais > maior_n_iguais:
            maior_n_iguais = n_iguais
            melhor_frase = ''.join(list_frase_gerada)

        cont += 1
        if cont == 10000:
            print(maior_n_iguais, melhor_frase)
            melhor_frase = ''
            maior_n_iguais = 0
            cont = 0
            
  



#print(comparaFrase('methinks it is like a weasel', ['b','c','d','e']))