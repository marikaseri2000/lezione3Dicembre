from data.repository import get_file

def get_domanda(file_path: str) -> str:
    with get_file(file_path) as file:
        content=file.read()
        return content

def get_lista_domande(file_path:str) -> list[str]:
    lista_domande:list[str] = []
    with get_file(file_path) as f:
        for i in f:
            #print(i)
            lista_domande.append(i.strip())
    return lista_domande

def estrai_domanda(content:str, index:int)-> str:
    """
    Questa funzione estrae la domanda dal file
    """
    return content [0:index]

def estrai_risposta(content:str, index: int)-> str:
    """
    Questa funzione estrae le risposte dal file
    """
    return content [index+1:]

def estrai_index(content: str)-> int:
    """
    Questa funzione estrae l'indice di separazione tra domanda e risposta
    """
    return content.index("£")

def valida_scelta(scelta: str)->bool:
    """
    Questa funzione prende un valore di tipo stringa e verifica che la risposta sia una delle opzioni tra A,B,C e D. 
    Se la risposta è una stringa vuota, restituisce false, idem se la risposta non è una di quelle sopra elencate.
    """
    #scelta temporanea la definiamo con scelta_tmp
    scelta_tmp = scelta.upper()
    if scelta_tmp == "A" or scelta_tmp =="B" or scelta_tmp == "C" or scelta_tmp == "D":
        return True
    else:
        return False

def is_risposta_esatta(scelta: str, risposta_esatta: str) -> bool:
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False
    
def calcola_percentuale(parte: int, totale: int) -> float:
    """Calcola la percentuale (0-100) date due quantità."""
    if totale == 0:
        return 0.0
    return (parte / totale) * 100

def verifica_superamento(percentuale: float, soglia: float = 60.0) -> bool:
    """Restituisce True se la percentuale è maggiore o uguale alla soglia."""
    return percentuale >= soglia

def genera_statistiche(risultato_finale: list[dict [str, str | bool]]) -> dict[str, int]:
    statistica: dict[str, int]={}

    risposte_esatte:int=0
    risposte_non_esatte:int=0

    for i in risultato_finale:
        if i["risposta_corretta"]:
            risposte_esatte += 1
        else:
            risposte_non_esatte += 1
        
    statistica["risposte_esatte"]  = risposte_esatte
    statistica["risposte_non_esatte"]  = risposte_non_esatte    
    return statistica