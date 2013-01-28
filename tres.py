os.chmod('py.python', 777)

def verificar(str):
    return re.match('int [a-zA-Z]* = \number', str) == None

import math
def area_circulo(r):
     return math.pi*math.pow(r,2)

n = 6
def bits (n):
     if (n%2==0):
         return math.log(n,2)
     else:
         return int (math.log(n,2)+1)

lista = ['a', 0909, 'dx-w']
def sorteia_elemento (lista):
     return lista [(random.randint(0,(len(lista)-1)))]


from datetime import datetime
d = datetime (1990, 12, 31, 23, 12, 11)
def diferenca_data(data):
      return (datetime.now()-data)

