#dal modulo esercizio12_1.py importare la classe MovieCatalog
from esercizio12_1 import MovieCatalog

#creare un oggetto della MovieCatalog 
catalog: MovieCatalog = MovieCatalog()

#aggiungiamo un regista dei film al catalogo
catalog.add_movie('Steven Spielberg',['Casper', 'Ritorno al futuro'])



#aggiungere un altro film di steven spielberg al catalogo
catalog.add_movie('Steven Spielberg', ['ET'])

# print(catalog.getCatalog())

# aggiungere un nuovo regista 
catalog.add_movie('Quentin Tarantino',['Pulp Fiction', 'Kill Bill'])

print(catalog.getCatalog())