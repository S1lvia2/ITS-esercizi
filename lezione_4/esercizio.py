import matplotlib.pyplot  as plt

def collatz(n: float) -> list[float]: 

    numeri : list = [n]

    while n != 1: 

        if n % 2 == 0: 

            n = n / 2 

        else: 
            n = (3 * n ) + 1

        numeri.append(n)

        print(n)
    return numeri

numeri: list[float] = (collatz(8.0))
plt.plot(numeri)
plt.show()

        

