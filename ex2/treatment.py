from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import RDF, OWL
import pprint

g = Graph()
g.parse("med_doencas.ttl")

diseases = Namespace("http://www.example.org/disease-ontology#")

with open("Disease_Treatment.csv") as file:
    for line in [line.rstrip() for line in file][1:]:
        d = URIRef(f"{diseases}{line.split(',')[0]}")
        #g.add((d, RDF.type, diseases.Disease))

        for t in line.split(',')[1:]:
            if t:
                uri = URIRef(f"{diseases}{t}")
                g.add((uri, RDF.type, diseases.Treatment))
                g.add((d, diseases.hasTreatment, uri))

print(len(g))
#for stmt in g:
#    pprint.pprint(stmt)

g.serialize("med_tratamentos.ttl")