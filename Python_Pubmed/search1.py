# importar la funcion de busqueda
from googlesearch import search
# esta variable contiene el paramentro o consulta de busqueda

#q = "java"
#q = "R lenguage"
#q = "Python lenguage"
#q = "gifted"
#q = "free pendulum"
#q = "FSL Software"
#q = "FreeSurfer"
q = "open datasets MRI"

# ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta
results = search(q)
# hacemos un recorrido de los resultados, cada resultado es una URL
for r in results:
	print(r)

