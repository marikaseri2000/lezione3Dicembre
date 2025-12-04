prodotti: list[str: dict [str, str | int]]= [
    {"nome" : "Laptop", "prezzo" : 899.99, "quantità" : 5},
    {"nome" : "Mouse" , "prezzo" : 25.50, "quantità" : 50},
    {"nome" : "Tastiera" , "prezzo" : 75.00, "quantità" : 30},
    {"nome" : "Monitor" , "prezzo" : 299.99, "quantità" : 15}]

inventario:float=0

#OCCHIO qui devi tener conto che parli di x quindi il valore della chiave "prezzo"
for x in prodotti:
    inventario += x["prezzo"]*x["quantità"]
    print(x["prezzo"]) if x["prezzo"]>100 else None

print(inventario)