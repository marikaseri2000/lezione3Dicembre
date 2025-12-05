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