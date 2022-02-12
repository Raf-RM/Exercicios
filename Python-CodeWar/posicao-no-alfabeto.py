# -- A ideia aqui era a de construir uma função que recebe uma string de texto e devolve
#    uma string contendo números refeerntes as letras do alfabeto.
def posicao_alfabeto(texto):
    meu_dicionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,
                      'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,
                      's':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    lista_saida = []
    for i in texto:
        if i.lower() in meu_dicionario:
            lista_saida.append(str(meu_dicionario[i.lower()])) 

    return ' '.join(item for item in lista_saida)

print(posicao_alfabeto('Testes pra vê se deu.'))

# -- Refatorando essa primeira versão fica
def alphabet_position(text):
    myDict = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,
              'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,
              'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    
    string = ' '.join(str(myDict[i.lower()]) for i in text if i.lower() in myDict)

    return string

print(alphabet_position('Testes pra vê se deu.'))

# -- Retirando o dicionario e deixando uma lista com as letras do alfabeto
def alphabet_posi(text):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'    
    string = ' '.join(str((alfabeto.index(i.lower()))+1) for i in text if i.lower() in alfabeto)

    return string

print(alphabet_posi('Testes pra vê se deu.'))