class MovieCatalog: 

    ''' 
    Attributi della classe MovieCatalog
    self.catalog: dict[str, list[str]]
    
    '''

    #inizializzare un oggetto della classe MovieCatalog
    def __init__(self) -> None:
        self.setCatalog()
    
    #metodo str per visualizzare un catalogo
    def __str__(self) -> str:
        string: str= ""
        for key, value in self.catalog.items():
            temp = "\n" + key + ": " + str( value) + "\n"
        
            string + temp
        return string        

    #metodi setter

    #metodo che imposta il valore dell'attributo self.catalog
    def setCatalog(self) -> None: 
        self.catalog: dict[str, list[str]] = {}

    # metodo getter 
    
    #metodo che ritorna il valore dell'atributo self.catalog
    def getCatalog(self) -> dict[str,list[str]]:
        return self.catalog
    
    #metodi della classe MovieCatalog 

    #metodo che aggiunge una lista di un film al catalogo

def add(self, director_name:str, movies: list[str]) -> None: 
    # check calore valido di director_name
    if not director_name: 
        print("Fornire un nome valido per il regista")
    # check valore valido di movies
    elif not movies: 
        print(" Fornire una lista di film che non sia vuota")
    #se i dati inseriti sono validi
    else: 
        
        # se il regista è presente nel catalogo, aggiungi i film
        if director_name in self.catalog:
            #aggiungere film al catalogo
            for movie in movies: 
                #controlliamo se i film della lista movies siano gia stati inseriti dentro il catalogo 
                #dizionario[key] -> ritorna il valore corrispondente della chiave key
                #self.catalog [director_name] è la lista dei film prodotti dal regista directo_name
                #dove self.catalog è un dizionario 
                #director_name è la chiave 
                #self.catalog[director_name] è il valore corrispondente alla chiave directory_name
                if movie in self.catalog[director_name]: 
                   print(f" il film {movie} è già presente nel catalogo")

                # un film della lista movies non è già presente nel catalogo 
                else: 
                    #aggiungere il film al catalogo 
                    self.catalog[director_name].append(movie)
            #se il regista non è presnete nel catalogo, creare un nuovo record
            #e come valore il nome della lista di film movies
            else: 
                self.catalog[director_name] = movies



    #metodo che rimuove un film dal catalogo 
    def remove_movie(self, director_name:str, movie:str) -> None: 
       if not director_name: 
        print("Fornire un nome valido per il regista")
    # check valore valido di movies
       elif not movies: 
        print(" Fornire una lista di film che non sia vuota")
    #se i dati inseriti sono validi
       else: 
        
        # se il regista è presente nel catalog, e il check se l film da rimuovere è presente nella lista dei film prodotti dal regista
        if director_name in self.catalog and movie in self.catalog[director_name]:
            
            #rimuovere il film dalla lista 
            self.catalog[director_name].remove(movie)

        #se la lista dei film è vuota, rimuovi il regista dal catalogo
        if not self.catalog[director_name]: 
            #rimuovere il resgista dal catalogo 
            del self.catalog[director_name]
