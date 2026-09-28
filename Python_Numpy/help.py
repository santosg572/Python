import numpy.random as rr

dd = dir(rr)

#print(dd)

k = 1
for ss in dd:
  ss.replace('\n','')
  es_mayuscula = ss[0].isupper()
  ss0 = ss[0]
 
  if not (es_mayuscula or (ss0 == '_')):
    print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&' + str(k) + ' - ' + ss + ' &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
    k = k+1
    print(help(eval('rr.'+ss)))


