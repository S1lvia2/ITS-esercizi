frase:str = input("Inserisci un frase: ")

match frase[-1]:
    case '?' if len(frase)%2 == 0:
        print("Si")
    case '?' if len(frase) != 0:
        print("No")
    case "!":
        print("Wow!")
    case _:
        print(f"Tu dici {frase}")