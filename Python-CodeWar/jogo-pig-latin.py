# -- A ideia aqui é construir uma função que faça um jogo de palavras (jogo americano Pig Latin)
#    pegando a primeira letra de cada palavra da string e colocando ela no final acressentando um 'ay'
def jogoPigLatin(text):
    text_list = text.split()
    new_list = []
    
    for i in text_list:
        if i != '!' and i != '?' and i != '.' and i != ',' and i != ';' and i != ':':
            first = i[0]
            new_i = i[1:] + first + 'ay'
            new_list.append(new_i)
        else:
            new_list.append(i)

    return ' '.join(new_list)

teste = 'Pig latin is cool'
print(jogoPigLatin(teste))

# -- Uma maneira mais inteligente de se fazer isso é refatorando o código e utilizando a função isalnum()
#    Esta função verifica se todos os caracteres em uma determinada string são alfa numericos ou não (abc123)
def pig_it(text):
    text_list = text.split()
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalnum() else word for word in text_list])

print(pig_it(teste))