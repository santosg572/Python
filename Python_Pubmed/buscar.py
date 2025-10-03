from pymed import PubMed
import sys

print(sys.argv[0])
print(sys.argv[1])
print(len(sys.argv))

pubmed = PubMed(tool="MyTool", email="my@email.address")

#query = "ANTs[Title/Abstract]"

palabra = sys.argv[1]
file = sys.argv[2]

#query = palabra+"[Title/Abstract]"
query = '('+ palabra + '[Title]) AND (("2005/01/01"[Date - Publication] : "3000"[Date - Publication]))'
print(query)

results = pubmed.query(query, max_results=500)

fil = open(file+'.txt', 'w')

for article in results:
# print(article.toJSON())
 fil.write(article.toJSON())

fil.close()


