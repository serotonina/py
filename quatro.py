class ConversorRomano:
    def converte_pra_decimal(num):
        if num in ['I', 'II', 'III']:
            return len(num)
        if num == 'IV':
            return 4
        if num == 'V':
            return 5
        if num == 'VI':
            return 6
        if num == 'VII':
            return 7
        if num == 'VIII':
            return 8
        if num == 'IX':
            return 10

#testes
#Teste Um:
ConversorRomano.converte_pra_decimal ('I') == 1
ConversorRomano.converte_pra_decimal ('II') == 2

def conta_palitos (n):
    if n == 1 or n == 2 or n == 3 :
        return n*palito
    if (n % math.sqrt(n) == 0 ):
        return int (math.sqrt(n)) * palito + '*' + int (math.sqrt (n))*palito
    if (n%2 == 0):
        return 2*palito + '*' +  n/2*palito
    for n in n
    else:
        return int (n/2)*palito + '+' + int ((n/2)+1)*palito
