# -- A ideia aqui é construir uma função que recebe um iterável (lista ou string por exemplo) e retorna
#    uma lista contendo apenas os itens que nãos e repetem em sequência.
 
def unico_na_ordem(entrada):
    lista_entrada = list(entrada)
    lista_saida = []
    for i in range(len(lista_entrada)):
        if i == 0:
            lista_saida.append(lista_entrada[0])
        elif lista_entrada[i] != lista_entrada[i-1] and i > 0:
            lista_saida.append(lista_entrada[i])
    return lista_saida

print(unico_na_ordem('AAAABBBCCDAABBB'))
print(unico_na_ordem('ABBCcAD'))
print(unico_na_ordem([1,2,2,3,3]))

# -- Como tanto a string quanto a lista são iteráveis não há necessidade de reescrever a entrada como uma lista
#    
def unique_in_order(iterable):
    out_list = []
    for i in iterable:
        if len(out_list) == 0 or i != out_list[-1]: # se a lista estiver vazia ele coloca o primeiro item do 
            out_list.append(i)                      # iterável ou se o item do iterável for diferente do
    return out_list                                 # do último item add na lista de saida ele coloca o item 
                                                    # na lista de saida
print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))

# --  A maneira mais sucinta de resolução desse problema pode ser obtida por aplicação da função lambda
#     e função enumerate

u_i_o = lambda entrada: [item for indice, item in enumerate(entrada) if indice == 0 or entrada[indice-1] != item]

print(u_i_o('AAAABBBCCDAABBB'))
print(u_i_o('ABBCcAD'))
print(u_i_o([1,2,2,3,3]))

# -- Nessa última a função enumerate() recebe um iteravel de entrada e retorna um objeto iterável contendo um indice
#    para cada item da entrada. 