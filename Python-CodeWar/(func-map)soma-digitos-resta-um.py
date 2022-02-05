# -- A ideia aqui é fazer um programa que soma os digitos de um dado valor até que só reste um único digito
# -- Exemplo: 347 --> 3 + 4 + 7 = 14  -- reaplicando --> 1 = 4 = 5 -- resta um único digito = 5

def resta_um(numero):
    if numero/10 < 1:
        return numero
    else:
        soma = 0
        string_num = str(numero)
        for i in range(len(string_num)):
            soma += int(string_num[i])
        return resta_um(soma)

print(resta_um(132189))

# -- Uma outra maneira de fazermos isso é utilizando a função map() que aplica uma função a cada item em um iterável
#    no nosso caso ela vai aplicar a função int() em cada item obtido pela função str(n) e retorna um iterador para podermos 
#    (um objeto map) para utilizar em outra parte do nosso programa

def resta_um_raiz(n):
    soma = 0
    if n<10:
        return n
    else:
        mapeando = map(int,str(n))
        soma = sum(mapeando)
        return resta_um_raiz(soma)
    
print(resta_um_raiz(132189))

# -- Nesta versão a função a função str() tranforma nosso número em uma string que pode ser acessada item a item (string[0], string[1], string[2]...)
#    como uma lista. A função map então aplica a cada item dessa nova string do número a função int() que transforma aquela
#    string[i] em um número inteiro e então retorna um iterável (tipo uma lista) e então a função sum() realiza uma soma de todos
#    elementos de um iterável (no nosso caso será o iterável retornado pela função map()).
# 
# -- Uma maneira mais sucinta de fazer isso é dada por:

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))

print(digital_root(132189))