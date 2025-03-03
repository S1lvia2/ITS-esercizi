lista_oggetti:list [any] =[]
for i in range (0,3): 
    oggetto:str = input("inserisci oggetto nella lista : ")
    lista_oggetti.append(oggetto)

match lista_oggetti: 
    case ["penna","matita","quaderno"]: 
        print("materiale scolastico")
    case ["pane","latte","uova"]: 
        print("prodotti alimentari")
    case ["sedia","tavolo","armadio"]: 
        print("mobili")
    case ["telefono","computer","tablet"]: 
        print("dispositivi elettronici")
    case _: 
        print("categoria sconosciuta")
