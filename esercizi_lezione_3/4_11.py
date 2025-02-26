lista_pizza : list[str] = ["Boscaiola","margherita","crostino"]

friend_pizzas : list[str] = ["Boscaiola","margherita","crostino"]

lista_pizza.append("diavola")
friend_pizzas.append ("4 formaggi")

for i in lista_pizza: 
    print (f" le mie pizze preferite sono: {i}")
for i in friend_pizzas: 
    print (f"le pizze preferite dei miei amici sono: {i}")