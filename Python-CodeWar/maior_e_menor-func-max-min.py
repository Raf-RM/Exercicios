# -- A ideia aqui é construir uma função que receba uma string de números separados por espaço (ex: "1 3 2 7 4 9 0")
#    e retorne uma string contendo o maior número e o menor número (ex: "0 9")

# -- Primeira solução (antes da refatoração). 

def maior_e_menor(string):
    lista = string.split()
    maior = int(lista[-1])
    menor = int(lista[0])
    for item in lista:
        if int(item) < menor:
            menor = int(item)
        elif int(item) > maior:
            maior = int(item)
    return str(maior) + ' ' + str(menor)


print(maior_e_menor("1 2 3 4 5"))
print(maior_e_menor("1 2 -3 4 5"))
print(maior_e_menor("1 9 3 4 -5"))

# -- Refatorando podemos obter uma lista contendo os itens de entrada como inteiros int() e então
#    aplicar as funções max() e min() para poder encontrar qual é o maior e o menor valor da lista

def high_and_low(numbers):
    list_numbers = [int(item) for item in numbers.split()]          # retorna um inteiro para cada item construindo 
    return str(max(list_numbers)) + ' ' + str(min(list_numbers))    # assim uma nova lista só com inteiros
    #return "{} {}".format(max(list_numbers), min(list_numbers))
    #return "%i %i" % (max(list_numbers), min(list_numbers))         # outras maneiras de formatar a saida

print(high_and_low("1 2 3 4 5"))
print(high_and_low("1 2 -3 4 5"))
print(high_and_low("1 9 3 4 -5"))    
