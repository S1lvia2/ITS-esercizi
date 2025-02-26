lista_pizza : list[str] = [                                         # lista delle mie pizze preferite
    "Boscaiola","margherita","crostino"
    ]                                                     

friend_pizzas : list[str] = [                         #lista delle pizze preferite dei miei amici
    "Boscaiola","margherita","crostino"
    ]  

lista_pizza.append("diavola")    #ho aggiunto una nuova piazza nella lista delle mie pizze preferite con append
friend_pizzas.append ("4 formaggi")     #ho aggiunto una nuova piazza nella lista delle pizze preferite dei miei amici con append

# ho utilizzato il ciclo for per iterare ogni elemento della lista e stampare le frasi con il print

for i in lista_pizza: 
    print (f" le mie pizze preferite sono: {i}")
for i in friend_pizzas: 
    print (f"le pizze preferite dei miei amici sono: {i}") 


#######################


lista_animali : list = [               #lista dei miei animali preferiti
    "quokka","lemure","criceto"
    ]
for i in lista_animali:                    #ho utilizzato un ciclo for per iterare ogni elemento della lista e stampare la lista con il print 
    print(i)

for i in lista_animali: 
    print(f"il {i} è un animale piccolo")

print("il criceto è un ottimo animale domestico") 


######################

