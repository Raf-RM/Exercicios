# -- A ideia aqui era de construir uma função que recebesse um número n representando um ano
#    e devolvesse ele escrito em algorítmos romanos baseado nessas regras para números romanos:
#    https://en.wikipedia.org/wiki/Roman_numerals

def ano_em_romano(n):
    myDict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    list_n = [int(i) for i in (str(n))]
    leng = len(list_n)
    cont = 1
    nova_lista = []
    string =''
    for i in list_n:
        dig = i * (1*10**(leng-cont))
        cont += 1
        nova_lista.append(dig)
    for i in nova_lista:
        if 0 < i // 1000 <= 3 :
            string = string + (i // 1000)*myDict[1000]        
        elif 100 <= i <= 300:
            string = string + (i//100)*myDict[100]         
        elif i == 400:
            string = string + myDict[100] + myDict[500]
        elif i == 500:
            string = string + myDict[500]
        elif 500 < i <= 800:
            string = string + myDict[500] + ((i-500)//100)*myDict[100]
        elif i == 900:
            string = string + myDict[100] + myDict[1000]
        elif 10 <= i <= 30:
            string = string + (i//10)*myDict[10]
        elif i == 40:
            string = string + myDict[10] + myDict[50]
        elif i == 50:
            string = string + myDict[50]
        elif 50 < i <= 80:
            string = string + myDict[50] + ((i - 50)//10)*myDict[10]  
        elif i == 90:
            string = string + myDict[10] + myDict[100]
        elif 0 < i <= 3:
            string = string + (i)*myDict[1]
        elif i == 4:
            string = string + myDict[1] + myDict[5]
        elif i == 5:
            string = string + myDict[5]
        elif 5 < i <= 8:
            string = string + myDict[5] + (i - 5)*myDict[1]  
        elif i == 9:
            string = string + myDict[1] + myDict[10]         

    return string

print(ano_em_romano(1998))
print(ano_em_romano(2022))
print(ano_em_romano(80))
print(ano_em_romano(1440))
print(ano_em_romano(1358))
print(ano_em_romano(1880))

# -- Uma maneira legal e mais cucinta seria aplicando a função sorted() que pode atuar sobre 
#    qualquer iterável e utilizando a flag reverse = True para realizarmos uma ordenação descendente

def solution(n):
    myDict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    roman_string = ''
    for key in sorted(myDict.keys(), reverse = True):
        while n >= key:
            roman_string += myDict[key]
            n -= key
    return roman_string

print(solution(1998))
print(solution(2022))
print(solution(80))
print(solution(1440))
print(solution(1358))
print(solution(1880))
