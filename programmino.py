# -*- coding: utf-8 -*-
# Inizializzo la variabile somma a zero
somma = 0

# Chiedo all'utente di inserire numeri finché non inserisce zero
while True:
    numero = int(input("Inserisci un numero intero"))
    
    # Se l'utente inserisce 0, il programma termina
    if numero == 0:
        break
    
    # Aggiungo il numero alla somma
    somma += numero

# Stampo la somma totale
print(f"La somma di tutti i numeri inseriti è: {somma}")

 