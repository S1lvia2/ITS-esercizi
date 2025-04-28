from persona import Persona 

from alieno import Alieno

# creare un oggetto p della classe Persona 
p: Persona = Persona("Silvia","Pesce", 21)

#visualizzae le informazioni dell'oggetto p della Persona 
print(p)

#creare un oggetto et della classe Alieno

et:Alieno = Alieno ('Andromeda')

#visualizzare le informazioni dell'oggetto et

print ("\n", et)

#invocare il metodo speak() della classe persona 
p.speak()
print("\n")
#incocare il metodo speak() della classe alieno
et.speak()
