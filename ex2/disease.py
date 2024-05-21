from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import RDF, OWL
import pprint

g = Graph()
g.parse("medical.ttl")

diseases = Namespace("http://www.example.org/disease-ontology#")

with open("Disease_Syntoms.csv") as file:
    for line in [line.rstrip() for line in file][1:]:
        d = URIRef(f"{diseases}{line.split(',')[0]}")
        g.add((d, RDF.type, diseases.Disease))

        for s in line.split(',')[1:]:
            if s:
                uri = URIRef(f"{diseases}{s}")
                g.add((uri, RDF.type, diseases.Symptom))
                g.add((d, diseases.hasSymptom, uri))

with open("Disease_Description.csv") as file:
    for line in [line.rstrip() for line in file][1:]:
        d = URIRef(f"{diseases}{line.split(',',1)[0]}")
        desc = line.split(',',1)[1]
        g.add((d, diseases.hasDescription, Literal(desc)))

print(len(g))
#for stmt in g:
#    pprint.pprint(stmt)

g.serialize("med_doencas.ttl")