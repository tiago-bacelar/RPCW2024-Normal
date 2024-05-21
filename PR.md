# Ex1

Foi criada uma ontologia no Protege e guardada em formato ttl
A ontologia foi carregada para o graphdb para testar as queries
Foi criado um ficheiro queries.txt com as queries desenvolvidas



# Ex2

Os nomes das doencas e dos sintomas foram tratados (nos proprios csvs) de forma a substituir espaços por underscores usando a seguinte substituição: "\n([()\w]+) +([()\w]+)" -> "\n$1_$2"
O ficheiro ttl foi editado para a sintaxe ser valida (faltavam dois ;)
Foi adicionada a data property hasDescription a medical.ttl
Foi criado um script python chamado disease.py que produz o output med_doencas.ttl a partit de medical.ttl e dos csvs
Foi criado um script python chamado treatment.py que produz o output med_tratamentos.ttl a partit de med_doencas.ttl e do csv
Foi adicionada a data property hasName a medical.ttl
O ficheiro json foi editado, substituindo os espaços dos sintomas por underscores
Foi criado um script python chamado patient.py que produz o output med_doentes.ttl a partir de med_doencas.ttl e o json dos doentes
Os scripts foram corridos sequencialmente, produzindo os ficheiros ttl
O ficheiro ttl foi carregado no graphdb para testar as queries
Foi criado o ficheiro queries.txt com as queries desenvolvidas