def lista_numeri(lista):
    risultato = {
        "positivi": [],
        "negativi": []
    }
    
    for numero in lista:
        if numero >= 0:
            risultato["positivi"].append(numero)
        else:
            risultato["negativi"].append(numero)
    
    return risultato


numeri = [0,-1,2,-3,4,-5,6,-7]
print (lista_numeri(numeri))
