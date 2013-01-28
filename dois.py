def temstring(s):
    comstring = filter (lambda x: s in x, lista)
    return comstring
 
def somatuplas (t, b):
    return tuple(sum(t) for t in zip(t,b)) 
