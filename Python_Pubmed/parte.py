file = "Machine_Learning_Tit"

fil = open(file+'.txt', "r")

datos = fil.readlines()

print(type(datos))

np1 = len(datos)
print(np1)

np2 = int(np1/2)

print(np2)

fil1 = open(file+'A'+'.txt', "w")

for i in range(np2-1):
 fil1.write(datos[i])

fil1.close()


fil2 = open(file+'B'+'.txt', "w")

for i in range(np2+1):
 fil2.write(datos[i+np2-1])

fil2.close()
