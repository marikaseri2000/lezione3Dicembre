lista_temperature:list[int]=[15, 18, 22, 25, 28, 30, 27, 24, 20]
print(f"Prima temepratura: {lista_temperature[0]}")
print(f"Ultime temperatura: {lista_temperature[-1:]}")
#occhio che l'indice iniziale viene considerato quello finale viene escluso
print(f"Temperature [2:5]: {lista_temperature[2:5]}")
#leggere ogni due valori 
print(f"Ogni due: {lista_temperature[::2]}")