giorno : int = int (input(f"inserisci il giorno: "))
mese: int = int (input(f"inserisci mese: "))  

date: tuple = (giorno,mese)
match date: 
    case (1,1): 
        print (f"Capodanno")
    case (14,2): 
        print (f"San Valentino")
    case (2,6): 
        print (f"Festa della Repubblica Italiana")
    case (15,8): 
        print (f"Ferragosto")
    case (31,10): 
        print (f"Halloween")
    case (25,12): 
        print (f"Natale")
    case _: 
        print (f"nessuna festività importante in questa data ")