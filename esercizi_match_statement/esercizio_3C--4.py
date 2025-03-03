tipo_animale:str= input("inserisci l'animale: ")
match tipo_animale: 
    case "cane"|"gatto"| "cavallo"| "elefante"|"leone": 
        print(f"il {tipo_animale} è un mammifero")
    case "serpente"| "lucertola"| "tartaruga"| "coccodrillo": 
        print(f"il {tipo_animale} è un rettile")
    case "aquila"| "pappagallo"| "gufo"|"falco": 
        print(f"il {tipo_animale} è un uccello")
    case "squalo"| "trota"|"salmone"|"carpa": 
        print(f"il {tipo_animale} è un pesce")
    case _: 
        print(f"il programma non è in grado di identificare {tipo_animale}")



