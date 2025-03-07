punto_x: int = (input(f"inserisci la coordinata: "))
punto_y: int = (input(f"inserisci la coordinata: "))

coordinate: tuple = (punto_x,punto_y)
match coordinate: 
    case coordinate if coordinate == 0: 
        print(f"il punto si trova nell'origine ")
    case coordinate if punto_y == 0: 
        print(f"il punto si trova sull'asse x")
    case coordinate if punto_x == 0: 
        print(f"il punto si trova sull'asse x")
    case coordinate if punto_x > 0 and punto_y > 0: 
        print(f"il punto si trova nel primo quadrante")
    case coordinate if punto_x < 0 and punto_y > 0: 
        print(f"il punto si trova nel primo quadrante")
    case coordinate if punto_x < 0 and punto_y < 0: 
        print(f"il punto si trova nel primo quadrante")
    case coordinate if punto_x > 0 and punto_y < 0: 
        print(f"il punto si trova nel primo quadrante") 