# -- A ideia era escrever uma função que, ao receber uma url, retornasse somente o nome do site:
#    ex: http://www.google.com --> google

def nome_site(url):
    out_string = ''.join(url.split('http://'))
    out_string = ''.join(out_string.split('https://'))
    list_out = out_string.split('.')
    if list_out[0] == 'www':
        return list_out[1]
    else:
        return list_out[0]

print(nome_site('http://www.google.com'))

# -- Minha versão refatorada onde eu escrevo tudo em uma única linha aplicando consecutivamente 
#    a função split() e join()
def dom_site(url):
    list_out = ''.join(''.join(''.join(url.split('http://')).split('https://')).split('www.')).split('.')
    return list_out[0]

print(dom_site('http://google.com'))

# -- Uma maneira ainda mais esperta de se fazer isso é empregando somente split() consecutivamente
#    o primeiro split vai cria uma lista com dois elementos o que tem antes de '//' e oque tem depois
#    selecionamos o segundo elemento (utilizando [-1]) e aplicamos o mesmo processo para 'www.'
#    será criado uma segunda lista com dois elementos o primeiro '' e o segundo 'tudo que tem depois de www.'
#    selecionamos o útlimo elemento novamente (o segundo) utilizando [-1] e aplicamos o split agora para o '.'
#    que ira criar uma lista de elementos dividindo os elementos onde havia '.' aqui o importante é o só o primeiro
#    elemento antes do ponto então pra pega-lo utilizamos [0] idependente de quantos elementos a lista tenha 
def domain_name(url):
    name = ((url.split('//')[-1]).split('www.')[-1]).split('.')[0]
    return name

print(domain_name('http://www.google.com'))

