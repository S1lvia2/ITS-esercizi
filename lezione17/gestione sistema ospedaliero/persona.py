class Persona: 

    def __init__(self,first_name: str, last_name: str): 
        
        if isinstance (first_name, str): 
            self.__First_name = first_name
        else: 
            print("il nome inserito non è una stringa")
            self.__First_name = None

        if isinstance (last_name, str): 
            self.__Last_name = last_name
        else: 
            print ("il cognome inserito non è una stringa")
            self.__Last_name = None

        if self.__First_name is not None and self.__Last_name is not None: 
            self.__age = 0
        else: 
            self.__age = None 

    def setName (self, first_name):
        if isinstance (first_name, str): 
            self.__First_name = first_name
        else: 
            print("il nome inserito non è una stringa")

    def setLastName (self, last_name): 
        if isinstance (last_name, str): 
            self.__Last_name = last_name
        else: 
            print("il cognome inserito non è una stringa")

    def setAge (self, age): 
        if isinstance (age, int): 
            self.__age = age
        else: 
            print("l'età inserita deve essere un numero intero")

    def getName(self):
        return self.__first_name

    def getLastname(self):
        return self.__last_name

    def getAge(self):
        return self.__age

    def greet(self):
        if self.__first_name and self.__last_name and self.__age is not None:
            print(f"Ciao, sono {self.__first_name} {self.__last_name}! Ho {self.__age} anni!")
        else:
            print("Dati insufficienti per il saluto.")
    


