personaggio1: dict[str, str]= {
    "nome" : "Pippo", 
    "tipo" : "cane",
    "email": "pippo@disney.com"
}

#print(personaggio1) stampa tutto il dizionario
print(personaggio1["email"])
personaggio1["telefono"] = "999777778"
print(personaggio1.get("telefono"))  #questo mi restituisce None 

#stampa le chiavi del mio dizionario
##for chiave, valore in personaggio1.items():
##    print(chiave)

for chiave, valore in personaggio1.items():
    print(f"{chiave} : {valore}")