from pymed import PubMed
import sys

print(sys.argv)

mes = sys.argv[1]
dia = sys.argv[2]
yy = sys.argv[3]

pubmed = PubMed(tool="MyTool", email="my@email.address")

#query = "(fmri[Title]) AND (2022/1/1[Date - Publication] : 3000[Date - Publication])"

#mes = "12"
#dia = "01"

#query = '("2024/12/04"[Date - Publication] : "2024/12/04"[Date - Publication])'
query = '("20'+ yy + '/' + mes + '/' + dia + '"[Date - Publication] : "20' + yy + '/' + mes + '/' + dia + '"[Date - Publication])'

# Execute the query against the API
results = pubmed.query(query, max_results=5000)

# Loop over the retrieved articles
for article in results:

    # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
    print(type(article))

    # Print a JSON representation of the object
    print(article.toJSON())

