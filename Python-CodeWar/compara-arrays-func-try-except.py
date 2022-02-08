# -- A ideia aqui era de receber duas listas contendo ou não números
#    e verificar se cada número na segunda lista era o quadrado de um número
#    na primeira lista
# -- Se uma das duas lista fosse None o resultado deveria ser falso
#    Se ambas fossem vazias o resultado deveria ser True uma vez que eram iguais

def comp(array1, array2):
    if array1 == [] == array2:
        return True
    if array1 == array2 == None:
        return True
    if array1 != None and array2 != None:
        arraysort1 = sorted([i*i for i in array1])
        arraysort2 = sorted(array2)
        contem = False
        for i in range(len(array1)):
            if arraysort1[i] == arraysort2[i]:
                contem = True
            else:
                contem = False
                break
        return contem
    else:
        return False

# -- A solução mais reduzida que vi foi utilizando tratamento de exeções
#    empregando o bloco "try and except". 
# -- A tenta executar o comando no bloco try se houver algum erro ela
#    executa o que há no except

def comp(array1, array2):
    try:
        # return sprted([i ** 2 for i in array1]) == sorted(array2)
        return sorted([i * i for i in array1]) == sorted(array2)
    except:
        return False

    
        
    
    