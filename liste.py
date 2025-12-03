stringhe: list[str] = ["Pippo"]
#stringhe: list[str | int] = ["Pippo", 1]
#stringhe: list[str | list[str]]=["Pippo", ["a", "b"]]

#aggiungere alla lista un dato
stringhe.append("Pluto")

stringhe.append("Minnie")

#print(stringhe[1]) così stampo solo l'elemento che inserisco
#for x in stringhe:
#    print(stringhe[1])

#-----------POP------------
#print(stringhe.pop())

deleted_values: list[str]=[]

#pop elimina e restituisce l'ultimo elemento, me lo metto in uno spazio di memoria 
#              -----------
#deleted_value = stringhe.pop()

value_to_check_and_delete: str = "pluto"
is_value_in_the_list: bool = value_to_check_and_delete in stringhe 


if is_value_in_the_list == True:
    index_value_to_delete = stringhe.index(value_to_check_and_delete)
    
#print(index_value_to_delete)

#posso scegliere che valore elimino pop(0), voglio eliminare "Pluto" indice=1
#deleted_value=stringhe.pop(1)

#deleted_values.append(deleted_value)     
#rivedi questa riga

    deleted_value = stringhe.pop(index_value_to_delete)
    deleted_values.append(deleted_value)
else:
    print(f"{value_to_check_and_delete} non esiste nella lista {stringhe}")

print("*"*30)
print(stringhe)
print(deleted_values)
