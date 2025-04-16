from persona import Persona 
from studente import Studente 

#creo un oggetto della classe Persona 
sp:Persona = Persona ( "Silvia"," Pesce", 21)

#visualizzare 1le informazioni relative all'oggetto sp
print(sp)

#creo un oggetto della classe Studente
studente1: Studente = ("Mario","Rossi",20, "0123456")

#visualizzare le informazioni relative all'oggetto studente1
print(studente1)

#controllo se studente1 sia istanza della classe Studente 
# sistance(obj, Class) -> controlla se l'oggetto obj sia un'istanza della classe Class.
#in caso affermativo -> True 
#in caso negativo -> False 
if isinstance (studente1, Studente): 
    print("\nstudente1 è istanza della classe Studente")

#controllo se studente1 è istanza della classe Persona 
if isinstance(studente1, Persona): 
    print("\nstudente1 è anche istanza della classe Persona")

#controllare se l'oggetto sp sia istanza dela classe Persona
if isinstance(sp, Persona): 
    print("\nl'oggetto sp è istanza della classe Persona")

#controllare se l'oggetto sp è anche istanza della classe Studente
if isinstance (sp, Studente): 
    print("\nl'oggetto sp è istanza della classe Persona ed è anche istanza della classe Studente")
else:
    print("\nl'oggetto sp è istanza della classe Persona ma non è anche istanza della classe Studente")

#controllare che la classe Studente sia sottoclasse della classe Persona
#issubclass (Class1,Class2) -> controlla se Class1 sia sottoclasse della classe Class2
#in caso affermativo -> True 
#in caso negativo -> False 
if issubclass(Studente, Persona):
    print("\nla classe Studente è sottoclasse della classe Personas")
