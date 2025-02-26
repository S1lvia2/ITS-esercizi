cars: str = input (f"inserisci modello macchina")
predict: bool

if cars == "audi": 
    predict = True 
    print(f"{cars} == macchine? {predict} ")
elif cars == "fiat": 
    predict = True 
    print(f"{cars} == macchine? {predict} ")
elif cars == "mercedes": 
    predict = True 
    print(f"{cars} == macchine? {predict} ")
elif cars == "BMW": 
    predict = True 
    print(f"{cars} == macchine? {predict} ")
elif cars == "Ducati": 
    predict = False
    print(f"{cars} == macchine? {predict} ")
elif cars == "BMX": 
    predict ==False
    print(f"{cars} == macchine? {predict} ")
elif cars == "Aprilia": 
    predict = False
    print(f"{cars} == macchine? {predict} ")
else: 
    print(f"la macchina che hai inserito è {cars}")

