def mostra_feedback(messaggio:str)->None:
    simbol: str = "*"*40
    print (f"""
          {simbol}
          {messaggio}
          {simbol}
          """)

def mostra_menu(domanda:str) -> None:
    """
    Questa funzione restituisce la domanda e le opzioni della risposta
    """
    print(domanda)

def genera_feedback(is_corretta: bool) -> str:
    """
    Restituisce il messaggio che indica all'utente se ha indovinato la risposta oppure no.
    Questa funzione viene eseguita solo se la funzione restitusce True. 
    """
    if is_corretta == True:
        return "             Hai indovinato!"
    else:
        return "Non hai indovinato. Ritenta!"

def raccogli_risposta() -> str: 
    """
    Questa funzione si occupa solamente di prendere l'input dell'utente.
    Il controllo di tale valore avverrà attraverso una funzione.
    """
    return input("Inserisci la tua scelta: ")