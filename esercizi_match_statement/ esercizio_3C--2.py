voto_laurea: int= int(input("inserisci il voto di laurea "))

match voto_laurea: 
    case voto_laurea if voto_laurea >=106 and voto_laurea <= 110: 
        print(f"il voto di laurea americano è {4.0}") 
    case voto_laurea if voto_laurea >=105 and voto_laurea <= 101: 
        print(f"il voto di laurea americano è {3.7}") 
    case voto_laurea if voto_laurea >=96 and voto_laurea <= 100: 
        print(f"il voto di laurea americano è {3.3}") 
    case voto_laurea if voto_laurea >=91 and voto_laurea <= 95: 
        print(f"il voto di laurea americano è {3.0}") 
    case voto_laurea if voto_laurea >=86 and voto_laurea <= 90: 
        print(f"il voto di laurea americano è {2.7}") 
    case voto_laurea if voto_laurea >=81 and voto_laurea <= 85: 
        print(f"il voto di laurea americano è {2.3}")
    case voto_laurea if voto_laurea >=76 and voto_laurea <= 80: 
        print(f"il voto di laurea americano è {2.0}") 
    case voto_laurea if voto_laurea >=70 and voto_laurea <= 75: 
        print(f"il voto di laurea americano è {1.7}")
    case voto_laurea if voto_laurea >= 66 and voto_laurea <= 69: 
        print(f"il voto di laurea americano è {1.0}")  
    case _: 
        print(f"il tuo voto inserito non è valido {voto_laurea}")

    

 
    