#!/usr/bin/python3

import pymongo


# eseguo la connessione con mongodb
client = pymongo.MongoClient('localhost', 27017)

# accedo ad un database 
db = client.testdb

# accedo la collection persone
persone_coll = db.persone

p = persone_coll.find_one()
print(p)


print('***')
# eseguo una query con un parametro in particolare
persone = persone_coll.find({'computer': 'apple'})
# abbiamo specificato come argomento del metodo find un dizionario in python che dice trova tutti 
# i documenti nella collection persone.coll che hanno come chiave computer e all'interno di questa 
# proprietà il valore 'apple'.
for persona in persone:
    print(persona)

print('***')
# utilizziamo un metodo che serve ad aggiornare un solo documento, questo metodo richiede come 
# minimo due argomenti: una query che serve a prelevare il documento che noi vogliamo andare a 
# modificare e come secondo argomento l'operazione
res = persone_coll.update_one({'nome': 'Giuseppe'}, {'$set': {'età': '50'}})
p = persone_coll.find_one({'nome': 'Giuseppe'})
print(p)

print('***')
# utilizziamo una fase di interrogazione che utilizza un filtro
persona = persone_coll.find_one({'nome': {'$gt': 'Giuseppe'}})
print(persona)
