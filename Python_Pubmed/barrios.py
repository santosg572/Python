from pymed import PubMed


# Create a PubMed object that GraphQL can use to query
# Note that the parameters are not required but kindly requested by PubMed Central
# https://www.ncbi.nlm.nih.gov/pmc/tools/developers/
pubmed = PubMed(tool="MyTool", email="my@email.address")

# Create a GraphQL query in plain text
#query = "meta-analysis[Title]"

#query = "Barrios FA[Author]"
#query = "Alcauter S[Author]"
#query = "Garza-Villarreal EA[Author]"
#query = "Gonzalez-Santos L[Author]"
#query = "Ortiz-Retana J[Author]"
#query = "Concha L[Author]"
query = "Merchant H[Author]"




# Execute the query against the API
results = pubmed.query(query, max_results=500)

# Loop over the retrieved articles
for article in results:

    # Print the type of object we've found (can be either PubMedBookArticle or PubMedArticle)
    print(type(article))

    # Print a JSON representation of the object
    print(article.toJSON())

