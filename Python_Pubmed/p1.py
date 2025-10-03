from pymed import PubMed
pubmed = PubMed(tool="MyTool", email="my@email.address")
results = pubmed.query("magnetic resonance", max_results=500)

print(help(results.from_iterable))


