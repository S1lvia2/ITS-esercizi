# # Legge la stringa da cifrare e il valore segreto XOR
# testo = input("Inserisci la stringa da cifrare: ")
# valore_xor = int(input("Inserisci il valore segreto per XOR: "))

# # Cifratura: applica XOR a ogni carattere della stringa
# lista_cifrata = [ord(c) ^ valore_xor for c in testo]

# # Stampa la lista dei numeri ottenuti
# print("\nLista cifrata (codici XOR):")
# print(lista_cifrata)

# # Decifratura: riapplica XOR per ottenere i caratteri originali
# testo_decifrato = ''.join([chr(n ^ valore_xor) for n in lista_cifrata])

# # Stampa la stringa decifrata
# print("\nStringa decifrata:")
# print(testo_decifrato)




`#include <iostre

int main(int argc, char * argv[]) {

        for (int i=0; i<100; ++i) {
        }

        int n=10;
        int m=10;

        cout << n++ << ", " << n++ << endl;
        cout << "Ora: " << n << endl;

        cout << ++m << ", " << ++m << endl;
        cout << "Ora: " << m << endl;
}
`