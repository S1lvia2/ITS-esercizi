class Persona:
    def _init_(self,name:str,lastname:str, age:int):
        self.setName(name)
        self.setLastname(lastname)
        self.setAge(age)

     # metodo speciale che ritorna una stringa e che viene chiamata automaticamente quando si usa l'istruzione print(obj),
    # dove obj è un oggetto della classe Persona
    # funzione che mi mostri in output i dati relativi ad una persona 
    def _str_(self) -> str:
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    # il metodo _call_ mi consente di usare l'oggetto della classe Persona istanziato come una funzione.
    # Quindi, un oggetto della classe Persona si comporta come una funzione
    def _call_(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.lastname} e' una persona adulta!")
        else:
            print(f"{self.name} {self.lastname} e' una persona anziana!")

    # mi consente di impostare un valore per self.name
    def setName(self,name:str) ->None:
        self.name = name

    # mi consente di impostare un valore per self.lastname
    def setLastname(self,lastname:str) ->None:
        self.lastname = lastname

    # mi consente di impostare un valore per self.age
    def setAge(self,age:int) ->None:
        if age < 0 or age > 130:
            self.age = 0
        else:
            self.age = age

    # ritorna il valore di set.name
    def getName(self) ->str:
        return self.name
    
    # ritorna il valore di set.lastname
    def getLastname(self) ->str:
        return self.lastname
    
    # ritorna il valore di set.age
    def getAge(self) ->int:
        return self.age

