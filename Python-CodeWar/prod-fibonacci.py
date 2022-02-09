# -- A ideia aqui era a de criar uma função que dado um determinado número (prod) 
#    verificasse se esse número era o produto de dois valores consecutivos da
#    sequência de fibonacci

from sympy import N


def productFib(prod):
    n_1 = 0
    n = 1  
    while 0 <= n * n_1 < prod:
        res = n + n_1
        n_1 = n
        n = res
    return [n_1, n, n * n_1 == prod]

print(productFib(4895))
print(productFib(5895))

# -- Refatorando essa primeira versão é possível rescrever mais sucintamente como

def product_fib(prod):
    n_1, n = 0, 1
    while (n_1 * n) < prod:
        n_1, n = n, n_1 + n
    return [n_1, n, n * n_1 == prod]

print(product_fib(4895))
print(product_fib(5895))