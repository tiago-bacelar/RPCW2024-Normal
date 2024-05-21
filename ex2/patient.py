from rdflib import Graph, URIRef, Namespace, Literal
from rdflib.namespace import RDF, OWL
import json

g = Graph()
g.parse("med_tratamentos.ttl")

diseases = Namespace("http://www.example.org/disease-ontology#")

f = open("pg54257.json")
bd = json.load(f)
f.close()

nextID = 0
for doente in bd:
    nextID += 1
    uri = URIRef(f"{diseases}patient_{nextID}")
    nome = Literal(doente["nome"])

    g.add((uri, RDF.type, diseases.Patient))
    g.add((uri, diseases.hasName, nome))
    
    for sintoma in doente["sintomas"]:
        g.add((uri, diseases.exhibitsSymptom, URIRef(f"{diseases}{sintoma}")))


print(len(g))
#for stmt in g:
#    pprint.pprint(stmt)

g.serialize("med_doentes.ttl")