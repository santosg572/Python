# importar la funcion de busqueda
from googlesearch import search
# esta variable contiene el paramentro o consulta de busqueda

q = "parkinson"

# ahora ejecutamos la busqueda con la funcion search y pasamos como parametro la consulta

results = search(q, num_results=100)

# hacemos un recorrido de los resultados, cada resultado es una URL
for r in results:
	print(r)

