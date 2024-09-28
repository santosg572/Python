filenom = 'paginas_drive.txt'

fichero = open(filenom)

caracter = fichero.readlines()

print(type(caracter))

nl = len(caracter)

ss=[]
for dd in caracter:
   dd1 = dd.split(',')
   dd2 = dd1[0]
   dd3 = dd2.replace("'", '')
   ss.append(dd3)
   ss.sort()

print(ss)


fichero.close()


nombreO = 'paginaN_drive.txt'

fileO = open(nombreO, 'w')

for line in ss:
    fileO.write(line)
    fileO.write("\n")
    
fileO.close()
