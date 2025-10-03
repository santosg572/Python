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

for an in range(2005, 2030):
   a1 = str(an)
   a2 = str(an+1)
   fileo = file + '_' + a1
   fil = open(fileo + '.txt', 'w')
   query = '('+ palabra + '[Title]) AND (("'+ a1 + '/01/01"[Date - Publication] : "' + a2 + '"[Date - Publication]))'
   results = pubmed.query(query, max_results=500)
   for article in results:
     fil.write(article.toJSON())
   fil.close()



