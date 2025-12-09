import sys
from data.services import (
    get_domanda,
    get_lista_domande,
    estrai_domanda,
    estrai_index,
    estrai_risposta, 
    valida_scelta, 
    is_risposta_esatta, 
    genera_statistiche,
    calcola_percentuale,
    verifica_superamento
)
from ui.console import (
    mostra_feedback, 
    mostra_menu, 
    genera_feedback, 
    raccogli_risposta
    )


def main():
    lista_domande:list[str]=[]
    risultato_finale:list[dict[str,str|bool]]=[]
    domanda_e_risposta: dict[str, str] = {"domanda" : None,"risposta" : None}
    lista_domande= get_lista_domande("domande.txt")
    counter_domanda_corrente:int=0
    lista_domande_lenght:int=len(lista_domande)
    #counter=len(domande_list)

    while counter_domanda_corrente < lista_domande_lenght:
        content: str = get_lista_domande(f"domande_risposte/{lista_domande[counter_domanda_corrente]}")
        index:int=estrai_index(content)
        domanda_e_risposta["domanda"] = get_domanda(content,index)
        domanda_e_risposta["risposta"] = estrai_risposta(content, index)
        
        #Restituisce l'indice della domanda corrente +1 per l'utente
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
            
            #LIVELLO 3 
            risultato_finale_len=len(risultato_finale)
            if counter_domanda_corrente < risultato_finale_len:
                risultato_finale[counter_domanda_corrente]=risultato
            else:
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

    print("*"*30)    
    print("Gioco terminato. Ecco i risultati.")
    print("*"*30)

    esatte=statistiche["risposte_esatte"]
    errate=statistiche["risposte_non_esatte"]

    totale_domande_fatte=esatte+errate
    perc=calcola_percentuale(esatte, totale_domande_fatte)
    is_superato = verifica_superamento(perc)
    
    print(esatte, errate, totale_domande_fatte, perc, is_superato)


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

if __name__=="__main__":
    main()


