# --  A ideia aqui era construir uma função que codificasse uma mensagem utilizando o sistema rot13
#     mas sem aplicar a função encode do python.
def rot13(mensagem):
    dict_1 = {'a':'n','b':'o','c':'p','d':'q','e':'r','f':'s','g':'t','h':'u','i':'v','j':'w','k':'x','l':'y','m':'z',
              'n':'a','o':'b','p':'c','q':'d','r':'e','s':'f','t':'g','u':'h','v':'i','w':'j','x':'k','y':'l','z':'m'}
    dict_2 = {'A':'N','B':'O','C':'P','D':'Q','E':'R','F':'S','G':'T','H':'U','I':'V','J':'W','K':'X','L':'Y','M':'Z',
              'N':'A','O':'B','P':'C','Q':'D','R':'E','S':'F','T':'G','U':'H','V':'I','W':'J','X':'K','Y':'L','Z':'M'}
    codificada = ''
    for i in mensagem:
        if i in dict_1:
            codificada += dict_1[i]
        elif i in dict_2:
            codificada += dict_2[i]
        else:
            codificada += i
    return codificada

print(rot13('Uma frase pra testas 1 trme - ou algo assim ?'))
