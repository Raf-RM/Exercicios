from sympy import prime


# -- A ideia aqui é fazer uma função que dada uma lista desordenada encontra 
#    encontra os dois menores números da lista e retorna a soma deles

def soma_dois_menores(lista):
    lista.sort()
    return lista[0] + lista[1]

print(soma_dois_menores([19, 5, 42, 2, 77]))    
print(soma_dois_menores([10, 343445353, 3453445, 3453545353453]))

# -- Uma maneira mais scucinta é utilizar a função sum() que soma 2 ou mais argumentos
#    e pedir para somar sobre a lista ordenada até o segundo. É possível utilizar outra
#    maneira para ordenar a lista por meio da função sorted()

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))    
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))