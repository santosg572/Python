import re

patron = re.compile('[0-9]')

cadena = 'a44453'
cadena = 'abc'

p = patron.search(cadena)  

if p == None:
 print(0)
else:  
 print(p.span())

