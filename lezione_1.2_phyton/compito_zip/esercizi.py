# esercizio 1
while True:
   
    parola:str = input(f"Inserisci una parola : ")

    if parola == "fine":
        print("Programma terminato.")
        break
    
    if parola[0] == parola[-1]:
        print(f"La parola '{parola}' ha il primo e l'ultimo carattere uguali.")
    else:
        print(f"La parola '{parola}' non ha il primo e l'ultimo carattere uguali.")

# esercizio 2
stringa: str= input(f"Inserisci una stringa: ")

numero_spazi = str.count(" ")

print(f"Il numero di spazi nella stringa è: {numero_spazi}") 

#esercizio 3

stringa:str = (input("Inserisci una stringa: "))
for i in stringa[::-1]: 
    print(stringa[::-1]) 
    break

#esercizio 4
somma_interi = 0
i = 0
numero_massimo = 0
numero_minimo = 100000000000000000

while True:

    n: float=(input("Inserisci un numero reale (un numero negativo per terminare): "))
    
    if n < 0:
        break
    
    if n.is_integer() == True:
        somma_interi += n
        i += 1 
        m = somma/i 
    if n > numero_massimo: 
        numero_massimo = n 
    if n < numero_minimo: 
        numero_minimo = n

    print(f"La media tra i numeri interi inseriti è: {m}")
    print(f"Il numero più grande inserito è: {numero_massimo}")
    print(f"Il numero più piccolo inserito è: {numero_minimo}")

#esercizio 5

n:int = int(input("Inserisci soldi posseduti: "))

if n%6==0:
    print(f"Hai sei buoni hai ottenuto una baretta gratuita, il numero di barrette totali è {n+n/6}")
    print(f"Questi sono i buoni che ti avanzano {n%6}")
else:
    print(f"Questi sono i buoni che ti avanzano {n%6}")

#esercizio 6
n1: int =int(input("Inserisci il primo numero n1: "))
n2: int =int(input("Inserisci il secondo numero n2: "))

p = 1
for i in range(n1, n2 + 1):
    p *= i
    
if n1 >= n2:
    p= n1 * n2
print(f"Il prodotto dei numeri tra {n1} e {n2} è: {p}")

#esercizio 7

n:int = int(input("Inserisci la lunghezza delle liste: "))
lista_a:list[int] = []
lista_b:list[int] = []
lista_c:list[int] = []
for i in range(1 ,n+1):
    lista_a.append(i)
    lista_b.append(i)

for i in range(n):
    somma = lista_a[i] + lista_b[n-1]
    i +=1
    n -=1
    lista_c.append(somma)
print(lista_a)
print(lista_b)
print(lista_c)

#esercizio 8

i= 1
while i<=5:
    n:int = int(input("Inserisci 5 numeri: "))
    if n >=1 and n<=30:
        print(n * '*')
    i +=1
#esercizio 9

pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.14:
    pi_greco = pi_greco + 4/i - 4/(i+2) # ... +4/9 - 4/11 + 4/13
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.2f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.141
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.141:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.3f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.1415
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.1415:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.4f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")

#metodo 3.14159
pi_greco:float = 4 - 4/3 + 4/5 - 4/7
term = 4
i = 9
while pi_greco < 3.14159:
    pi_greco = pi_greco + 4/i - 4/(i+2)
    term += 2
    i+=4
print(f"pi greco vale {pi_greco:.5f}")
print(f"I termini neccesari per arrivare all'appossimazione di pi greco sono {term}")
#esercizio 10

lista_numeri:list[int] = []
somma = 0
num_dispari:int = 0
somma_dispari = 0
while True:
    n:int = int(input("Inserisci un numero (0 per terminare): "))
    if n == 0:
        break
    else:
        lista_numeri.append(n)
    if n%2==0:
        somma = somma + n
    elif n%2==1:
        num_dispari +=1
        somma_dispari = somma_dispari + n
        med = somma_dispari/num_dispari

    count = 0
    freq = 0
    for i in lista_numeri:
        if lista_numeri.count(i) > count:
            count = lista_numeri.count(i)
            freq = i

    freq_common = 0
    for i in lista_numeri:
        if lista_numeri.count(i) > count:
            count = lista_numeri.most_common(i)
            freq_common = lista_numeri.most_common(i)

print(lista_numeri)
print(f"La somma dei numeri pari è {somma}")
print(f"La media dei numeri dispari è {med}")
print(f"Il numero più frequente della lista è {freq}")
print(f"I numeri più frequenti sono {freq}: {freq_common}")





