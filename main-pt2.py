import sys


#print("Hllo, Quizzettone!")

def mostra_menu(domanda:str)-> None:
    """
    Questa funzione restituisce la domanda e le opzioni della risposta
    """
    print(domanda)

def raccogli_risposta() -> str: 
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente.
    Il controllo di tale valore avverrà attraverso una funzione.
    """
    return input("Inserisci la tua scelta: ")
    
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
    if scelta.upper() == "A":
        return True
    else:
        return False

def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione restitusce True. 
    """
    if is_corretta == True:
        return "Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

def mostra_feedback(messaggio:str)->None:
    simbol: str = "*"*30
    print (f"""
          {simbol}
          {messaggio}
          {simbol}
          """)

def leggi_file(file_path:str)-> str:
    """
    Questa funzione si occupa di leggere il file delle domande e risposte
    """
    with open(file_path, "r") as file:
        content = file.read()
        return content    

        #question = content[0:85]
        ##answer=content[86:]
        #ci da la lunghezza di tutti i caratteri
        #print(len(content))
        #da questo segno fa la divisione tra domanda e risposta
        #print(content.index("£"))
        #stampa la domanda e la risposta che in precedenza ho differenziato con le due range
        #print(question)
        #print("------------------")
        #print(answer)

def estrai_index(content:str)-> int:
    """
    Questa funzione estrae l'indice di separazione tra domanda e risposta
    """
    return content.index("£")

def estrai_domanda(content:str, index:int)-> str:
    """
    Questa funzione estrae la domanda dal file
    """
    return content [0:index]

def estrai_risposta(content:str, index: int)-> str:
    """
    Questa funzione estrae le risposte dal file
    """
    answer: str= content[index+1:]
    return content [index+1:]

def estrai_liste_domanda(file_path:str) -> list[str]:
    lista_domande:list[str] = []
    with open(file_path, "r") as f:
        for i in f:
            #print(i)
            lista_domande.append(i.strip())
    return lista_domande

def main():
    domande_list:list[str]=[]
    qa: dict[str, str] = {
        "domanda" : None,
        "risposta" : None
    }

    domande_list = estrai_liste_domanda("domande.txt")
    
    #with open(domande_list[0],"r") as f:
    #    for i in f:
    #        print(i)
    content: str = leggi_file(f"domande_risposte/{domande_list[1]}")
    index: int = estrai_index(content)
    qa["domanda"] = estrai_domanda(content,index)
    qa["risposta"] = estrai_risposta(content, index)

    print(qa)
    
    #print(domande_list)
            # print(i.strip()) 
            #lo strip mi toglie gli spazi tra i tue .txt


main()