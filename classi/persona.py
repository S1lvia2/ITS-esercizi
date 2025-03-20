class Persona: 
    '''
    di una persona dobbiamo sapere delle informazioni. 
    Queste informazioni vengono chiamatebattributi ( della classe persona)
    Le informazioni saranno: 
    - nome
    - cognome
    - età

    come li rappresento in Pyhton? 

    self.name: str ( attributo di tipo stringa)
    self.lastname: str ( attributo di tipo stringa)
    self.age:int ( attributo di tipo integer)

    '''
    #  costruttore della classe Persona
    def __init__(self, name:str, lastname:str, age:int): 
        self.name = name 
        self.lastname = lastname 
        self.age = age
    
    # funzione che mosrti in output tutti i dati di una persona
    def displayData(self) -> None: 
        print(f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}")


sp: Persona = Persona("Silvia", "Pesce", 21)

print (sp)

#mostra i dati di una persona 
sp.displayData()