class Persona: 
    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.age = 0 

    def displayData(self) -> None: 
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}") 


#mi consent di impostare un valore per self.name
    def setName(self, name: str) -> None: 
        self.name = name 
#mi consente di impostare un valore per self.lastname
    def setLastname(self, lastname: str) -> None: 
        self.lastname = lastname

    def setAge(self, age:int) -> None:
        if age < o or age > 130: 
            self.age = 0 
        else: 
            self.age = 0 




#crea un oggetto di tipo persona 
sp: Persona = Persona()

#stampa i dati della Persona creata
sp.displayData()

#impostare il nome di una persona 
sp.setName("Silvia")

#impostare il cognome di una persona 
sp.setLastname("Pesce")



