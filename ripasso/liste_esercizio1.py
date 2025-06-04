list_tuple = list[tuple] = [(1,"A"), (2, "B"), ( 3,"C")]

def convert (lista: list[tuple]) -> dict: 
    dizionario_1:dict [any,any]= {}
    for element in lista: 
        key, value = element [0], element [1] 
        if key in dizionario_1: 
            dizionario_1[key]
        else: 
            dizionario_1[key] = value
    return dizionario_1
