dd ='''
DOMINANCIA DE LA MANO
1.- Tirar una pelota
2.- Sacar punta a un lapicero
3.- Clavar un clavo
4.- Cepillarse los dientes
5.- Girar el pomo de la puerta
6.- Sonarse
7.- Utilizar las tijeras
8.- Cortar con un cuchillo
9.- Peinarse
10.- Escribir
DOMINANCIA DEL PIE DER. IZQU.
1.- Dar una patada a un balón
2.- Escribir una letra con el pie
3.- Saltar a la pata coja unos 10 metros
4.- Mantener el equilibrio sobre un pie
5.- Subir un escalón
6.- Girar sobre un pie
7.- Sacar un balón de algún rincón o debajo de una silla
8.- Conducir un balón unos 10 mts.
9.- Elevar una pierna sobre una mesa o silla.
10.- Pierna que adelantas al desequilibrarte adelante
DOMINANCIA DEL OJO DER. IZQU.
1.- Sighting (cartón de 15 x 25 con un agujero en el centro de 0,5 cm diamétro)
2.- Telescopio ( tubo largo de cartón )
3.- Caleidoscopio - Cámara de fotos
DOMINANCIA DEL OÍDO DER. IZQU.
1.- Escuchar en la pared
2.- Coger el teléfono
3.- Escuchar en el suelo
'''
dd = dd[1:]
dd = dd.split('\n')

print('=========================')

print('---------------- '+ dd[0] + ' ----------------------')

dd = dd[1:]

for i in range(10):
  ss = dd[i]
  rr = input(ss)
  print(rr)








