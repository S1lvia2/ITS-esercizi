nome:str = input("inserisci il tuo nome: ")
gender:str = input (" inserisci il tuo gender (m or f): ")

match gender: 
    case "m": 
        print(f"Nome:{nome}, gender:{gender}")
    case "f": 
        print(f"Nome:{nome}, gender:{gender}")
    case _: 
        print(f"impossibile generare un documento d'identità con questo gender '{gender}' ")
    