# ESERCIZIO 1
#  import math
# a= int(input("inserire il valore di a:"))
# b= int(input("inserire il valore di b:"))

# if a > b: 
#     c:int = (math.sqrt)(a**2 - b**2)
#     print (c)
# else :
#     print("Errore")

# max:int = int (input("inserisci valore:"))
# cont:int = 1 

# while cont < 4: 
#     cont += 1 
#     n:int = int ("inserisci valore:")
    
# if n > max: 
#     max = n 

# print (f"questo il valore maggiore: {max}")

# esercizio 3

# sum: int= 0
# cont: int = 1
# while i<=5 :
#        n:int = int(input("inserisci un valore :")) 
#        if n > 0: 
#              sum += n
#     cont += 1 

# print (f"la somma ha valore:{sum}")


# ESERCIZIO 4
# n:int =int(input("inserisci un valore:"))
# if n %2 == 0:
#      print ("il numero è pari:")

# else: 
#      print ("il numero è dispari:")

# Esercizio 5




# esercizio 6
# def calcola_fattoriale(n): 
#     if n == 0 or n == 1: 
#         return 1 
#     else: 
#         fattoriale = 1 
#         for i in range (2, n + 1): 
#              fattoriale *= i 
#         return fattoriale 
    
# n:int =int(input("inserisci un valore:"))
# if n < 0 : 
#     print (" Per favore, inserisci un numero intero positivo") 
# else: 
#     risultato = calcola_fattoriale(n) 
#     print(f"il fattoriale di {n} è:{risultato}")

# esercizio 7
# pari = 0
# dispari = 0
# for i in range (10): 
#     n= int(input(f"inserisci il {i+1}numero:"))
#     if n % 2 == 0: 
#         pari += 1 
#     else: 
#         dispari += 1

# print(f"totale numeri pari:{pari}")
# print(f"totale numeri pari:{dispari}")

# esercizio 8
# soglia = int(input("inserisci la soglia:"))
# numeri_maggiori = []
# for i in range (7): 
#     n = int (input(f"inserisci il {i+1} numero:"))
#     if n > soglia: 
#         numeri_maggiori.append(n)

#   if numeri_maggiori: 
#     print(f"i numeri maggiori della soglia({soglia}) sono:{numeri_maggiori}")
#     else: 
#     print(f"nessun numero è maggiore della soglia({soglia}).")

# esercizio 9

# nome:str= input ("inserire il nome:")
# vendite :int= int(input("inserire il valore:"))
# max_nome:str = nome
# max:int= vendite
# min_nome:str=nome

# min:int=vendite
# i= 0

# while i != 4: 
#     new_nome: str = input("inserisci nuovo nome:")
#     new_vendite:int =int (input("inserisci nuovo valore: "))
#     i = i+1

#     if new_vendite > max: 
#         max_nome = new_nome 
#         max= new_vendite 

#         if new_vendite < min : 
#             min_nome = new_nome
#             min = new_vendite

# print(f"questo è il massimo:{max_nome} , {max}")
# print(f"questo è il minimo:{min_nome} , {min}")


# esercizio 10

# r: str =float(input("inserisci valore"))
# m: str = float(input("inserisci valore"))

# if r < 20000 and m > 27: 
#     print(f"borsa di studio approvata") 
# else: 
#     print(f"borsa di studio rifiutata")

# esercizio 11

# liberi:int = 20 

# while True: 
#     opzioni: str = input("inserisci opzioni tra: prenota, libera, visualizza,esci") 
#     if opzioni == "prenota":
#         if liberi > 0: 
#             liberi -= 1 
#         else: 
#             print("non ci son posti disponibili.") 
#     elif opzioni == "libera":
#         if liberi < 20: 
#             liberi += 1 
#             print("tutti i posti sono disponibili") 
#         elif opzioni == "visualizza": 
#             print(liberi) 
#             print( 20 - liberi) 
#         elif opzioni == "esci": 
#             break 
#         else: 
#             print("Errore, inserire una delle opzioni disponibili tra: prenota, libera, visualizza, esci")