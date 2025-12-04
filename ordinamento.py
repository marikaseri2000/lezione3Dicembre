#Creare una lista prezzi contenente: [45.5, 12.0, 78.3, 23.1, 56.7]
#Creare una copia ordinata della lista (usando sorted())
#Trovare il prezzo minimo e massimo
#Verificare se 23.1 è nella lista
#Contare quanti prezzi sono maggiori di 50

prezzi_u: list[float]=[45.5, 12.0, 78.3, 23.1, 56.7]
#SORTED restituisce una copia del valore originalre ma una copia e non sovrascrive, mentre SORT modifica la lista di partenza
prezzi_o: list[float]=sorted(prezzi_u)

print(prezzi_o)

#Occhio lo fa bene perchè sono ordinati gli elementi nella lista 
minimo=min(prezzi_o)
print(minimo)
massimo=max(prezzi_o)
print(massimo)

#i prossimi due print sono uguali ma metodi diversi
if 23.1 in prezzi_o:
    print (f"Il valore {23.1} è presente: True")

print(23.1 in prezzi_o)

contatore=0

for x in prezzi_o:
    if x > 50:
        contatore += 1
print(contatore)
