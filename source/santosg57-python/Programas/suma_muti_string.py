import sys

def RealizaSumas(x=''):
  res = ecuentra_Oper(x)
  oper1 = float(res[0])
  operacion = res[1]
  x = res[2]

  suma = oper1

  while operacion != 'x':
    res = ecuentra_Oper(x)
    s1 = float(res[0])
    ope = res[1]
    x = res[2]
    if operacion == '+':
      suma = suma + s1
    else:
      suma = suma - s1
    operacion = ope
  return suma

def ecuentra_Oper(x=''):
  i1 = x.find('+')
  i2 = x.find('-')
  oper= 'x'
  s2 = ''
  if i1 < 0 and i2 < 0:
    s1 = x
  else:
    if i1 < i2:
      if i1 > 0:
        ii = i1
      else:
        ii = i2
    else:
      if i2 > 0:
        ii = i2
      else:
        ii = i1

    s1 = x[:ii]
    oper = x[ii]
    s2 = x[ii+1:]
  res = [s1, oper, s2]
  return res


x = '23-33-22-22+10'

x = sys.argv[1]

res = RealizaSumas(x)

print('La suma de ' + x + '      es: ' + str(res))

 
  
