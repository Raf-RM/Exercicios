# -- Definindo listas, strings, tuplas, conjuntos e dicionários
# -- Listas:
lista_1 = [15,-2,'só testes',0.35]
lista_2 = []
lista_1.insert(3,'item')
print(lista_1)
lista_2.insert(0,'item')
print(lista_2)
lista_1.pop(3)
print(lista_1)
print(lista_1.count(0.35))
print(lista_1.index(0.35))
lista_1.remove(0.35)
print(lista_1)

# -- Strings
string_1 = 'Esta é uma frase normal.'
string_2 = '1,2,3,4,5'
print(string_1[0], string_2[4])
print(string_2.split(','))
print(string_1.split())
print(string_1.split('a'))
print(string_2.center(30))
print(string_1.rjust(50))
print(string_1.ljust(50))
print(string_2.find('3'))


# -- Tuplas
tupla_1 = ('uma string', 1, -8, 3.45)
tupla_2 = (1,2,3,4,5)
print(7 in tupla_1)
print(1 in tupla_1)
print(len(tupla_2))


# -- Conjuntos
conj_1 = {'Arroz', 'Feijão', 'Macarrão', 2, 3}
conj_2 = set()
print(len(conj_2))
conj_2.add('Batata Frita')
print(conj_1 | conj_2)
conj_1.remove('Macarrão')
print(conj_1.union(conj_2))

# -- Dicionários
dic_1 = {'key_1' : 'valor_1', 'key_2' : 'valor_2', 'key_3' : 'valor_3'}
dic_2 = {1 : 'Sim', 2 : 'Não'}

print(dic_2[1])
print('key_3' in dic_1)
print(dic_1.keys(), dic_2.keys())
print(dic_1.values(), dic_2.values())
print(dic_2.items())
print(dic_2.get(2))
print(dic_1.get('key_4', 'Não tem essa chave aqui!'))


