# “methinks it is like a weasel”
from random import choice

def geraAleatorio(n):
    lista_alfabeto = [
        'a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','x','w','y','z',
        ' ']
    lista_frase = ''
    while n > 0:
        lista_frase += choice(lista_alfabeto)
        n -= 1
    #return ''.join(lista_frase)
    return lista_frase



def comparaFrase(list_frase_orig, list_frase, n):
    print(list_frase)
    list_frase_gerada = [letra for palavra in list_frase for letra in palavra] 
    
    compara = False
    
    while list_frase_gerada != list_frase_orig:
        cont_iguais = 1
        for i in range(n):
            if list_frase_gerada[i] == list_frase_orig[i]:
                cont_iguais += 1 
            else:
                list_frase_gerada[i] = geraAleatorio(1)
                compara = False
        if cont_iguais == n:
            compara = True
    
    return compara, cont_iguais, ''.join(list_frase_gerada)

#def inicia():

frase_original = 'methinks it is like a weasel'
list_frase_orig = [letra for palavra in frase_original for letra in palavra]

print(comparaFrase(list_frase_orig, geraAleatorio(28), 28))  
