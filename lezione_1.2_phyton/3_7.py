#esercizio 3.7

list_1 : list = ["Adele","Demi Moore","Jennifer Aniston"]

print ("new dinner table won’t arrive in time for the dinner")

print(f" Dear {list_1 [0]} im so sorry i can not invite you to dinner")

list_1.pop(0)

print(f"Dear {list_1[0]}, you are still invited to dinner!")
print(f"Dear {list_1[1]}, you are still invited to dinner!")

del list_1[0]
del list_1[0]

print (list_1)

