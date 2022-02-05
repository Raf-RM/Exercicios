def to_jaden_case(string):
    string_list = string.split()
    new_string = string_list[0].capitalize()
    for i in range(len(string_list)):
        if i > 0:
            new_string = new_string + ' ' + string_list[i].capitalize()
    return new_string

print(to_jaden_case('da nada não. pai do tiaguim.'))

# -- A ideia aqui era de criar uma função que pega a string e coloca a primeira letra de cada palavra na string em maiscula
# -- de maneira mais simples podemos fazer como segue abaixo

def tjc(string):
    string_list = string.split()
    espaco = ' '
    new_string = espaco.join(item.capitalize() for item in string_list)
    return new_string

print(tjc('da nada não. pai do tiaguim. com a versão dois.'))

# -- Aqui usamos a função .join que é um método de string que retorna uma string cujo os elementos foram unidos por um separador
#    (no nosso caso o separador é 'espaco')

# -- Uma maneira ainda mais sucinta é dada por

def sucinta_tjc(string):
    return ' '.join(item.capitalize() for item in string.split())

print(sucinta_tjc('da nada não. pai do tiaguim. Com uma forma mais sucinta ainda.'))

# -- Esse método junta o pega cada termo (item) da frase (string) separado pela função split(), 
#    coloca a primeira letra de cada em maisculo com a função capitalize() e concatena esses termos separandos com ' ' com a função .join 