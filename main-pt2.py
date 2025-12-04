import sys


#print("Hllo, Quizzettone!")

def mostra_menu(domanda:str) -> None:
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
    if scelta.upper() == risposta_esatta:
        return True
    else:
        return False

def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione restitusce True. 
    """
    if is_corretta == True:
        return "             Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

def mostra_feedback(messaggio:str)->None:
    simbol: str = "*"*40
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

def estrai_index(content: str)-> int:
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
    return content [index+1:]

def estrai_lista_domande(file_path:str) -> list[str]:
    lista_domande:list[str] = []
    with open(file_path, "r") as f:
        for i in f:
            #print(i)
            lista_domande.append(i.strip())
    return lista_domande

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

def main():
    lista_domande:list[str]=[]
    risultato_finale:list[dict[str,str|bool]]=[]
    domanda_e_risposta: dict[str, str] = {"domanda" : None,"risposta" : None}
    lista_domande= estrai_lista_domande("domande.txt")
    counter_domanda_corrente:int=0
    lista_domande_lenght:int=len(lista_domande)
    #counter=len(domande_list)

    while counter_domanda_corrente < lista_domande_lenght:
        content: str = leggi_file(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index:int=estrai_index(content)
        domanda_e_risposta["domanda"] = estrai_domanda(content,index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)
        
        print (f"Domanda {counter_domanda_corrente+1} di {lista_domande_lenght}")
        print ("-"*30)

        mostra_menu(domanda_e_risposta["domanda"])
        risposta_utente:str= raccogli_risposta()
        is_risposta_valid: bool = valida_scelta(risposta_utente)

        feedback:str = ""

        if is_risposta_valid:
            risultato: dict[str, str|bool]={}
            is_risposta_corretta : bool= is_risposta_esatta(risposta_utente, domanda_e_risposta["risposta"])
            feedback=genera_feedback(is_risposta_corretta)
            risultato["domanda"] = lista_domande[counter_domanda_corrente]
            risultato["risposta_corretta"] = is_risposta_corretta
            risultato_finale.append(risultato)
            
        else:
            feedback="Inserisci solo la rispostra tra le opzioni."

        mostra_feedback(feedback)
        
        Possibility:str = input("Digita P per andare alla domanda precedente, altrimenti premi un altro carattere:").upper()
        
        if Possibility == "P":
            #Torna indietro
            if counter_domanda_corrente > 0:
                counter_domanda_corrente -= 1
            else:
                print("Sei già alla prima domanda, non puoi andare ulteriormente indietro.")
        else:
            #Va avanti
            if counter_domanda_corrente == lista_domande_lenght-1:
                print("Hai terminato le tue domande a disposizione.")
                break
            else:
                #aggiorno il contatore di andare alla domada successiva
                counter_domanda_corrente += 1
                print("Prosegui alla domanda Successiva.")
            
    print(risultato_finale)  
    statistiche:dict[str, int]=genera_statistiche(risultato_finale)
    print(statistiche["risposte_esatte"])
    print(statistiche["risposte_non_esatte"])


    """
    for q in range(counter):
    #with open(domande_list[0],"r") as f:
    #    for i in f:
    #        print(i)
        risultato: dict[str, str|bool]={}
        content: str = leggi_file(f"domande_risposte/{domande_list[q]}")
        index: int = estrai_index(content)
        qa["domanda"] = estrai_domanda(content,index)
        qa["risposta"] = estrai_risposta(content, index)
        mostra_menu(qa["domanda"])
        answer:str=raccogli_risposta()
        is_risposta_valid:bool = valida_scelta(answer)
        
        feedback: str = ""

        if is_risposta_valid == True:
            is_risposta_corretta : bool= is_risposta_esatta(answer, qa["risposta"])
            feedback=genera_feedback(is_risposta_corretta)
            risultato["domanda"] = domande_list[q]
            risultato["risposta_corretta"] = is_risposta_corretta
        else:
            feedback="Inserisci solo la rispo tra le opzioni"

        print(feedback)

    statistiche=genera_statistiche(risultato_finale)
    print(statistiche["risposte_esatte"])
    print(statistiche["risposte_non_esatte"])


    #print(domande_list)
            # print(i.strip()) 
            #lo strip mi toglie gli spazi tra i tue .txt


    """
main()