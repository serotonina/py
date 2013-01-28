def tamanho_lista(lista):
    tamanho = 0
    for i in lista
        tamanho += 1
    return tamanho
#ou return len(lista)

def fat_rec(n):
    assert n>=0 #so num positivo
    if n <1:
        return 1
    return n*fat_rec(n-1)

def n_pares(lista):
    pares = 0
    for elemento in lista:
        if elemento%2 == 0
             pares += 1
    return pares

def n_impares(lista):
    impares = 0
    for elemento in lista:
        if elemento%2 != 0
            impares += 1
    return impares

def fibonacci_it (n):
    assert n>= 0
    if n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    a,b = 0,1
    sequencia = [0,1]
    while n > 1:
        b = sequencia [-1] + sequencia [-2]
        sequencia.append(b)
