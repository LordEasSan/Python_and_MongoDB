#!/usr/bin/python3

import pymongo

# eseguo la connessione con mongodb
client = pymongo.MongoClient('localhost', 27017)

# creo un database e lo chiamo testdb
db = client.testdb

# creo la collection persone
persone_coll = db.persone

# creo degli indici all'interno del database, il metodo create_index richiede una lista di campi
# (proprietà) sui cui noi vogliamo assegnare un indice per ogni singole elemento che compone un 
# singolo indice dato che l'indice potrebbe essere anche multiproprietà, dobbiamo generare quindi 
# una lista e all'interno della lista usare delle tuple che contengono il nome della proprietà.
persone_coll.create_index([('nome',pymongo.ASCENDING)])
persone_coll.create_index([('cognome',pymongo.ASCENDING)])
persone_coll.create_index([('computer',pymongo.ASCENDING)])

# creo un documento, quanod noi vogliamo rappresentare un documento in Python dobbiamo usare la 
# sintassi dei dizionari, che è quella che più si avvicina alla forma BSON di documento in MongoDB.
p1 = {'nome': 'Mario', 'cognome': 'Rossi', 'età': 30, 'computer': ['asus', 'apple']}

#inseriamo il documento in mongodb
persone_coll.insert_one(p1)

p2 = {'nome': 'Giuseppe', 'cognome': 'Verdi', 'età': 45, 'computer': ['apple']}

#inseriamo il documento in mongodb
persone_coll.insert_one(p2)
