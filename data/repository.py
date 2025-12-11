from typing import TextIO

def get_file(file_path:str) -> TextIO:  #IO sta per input e output
    """Recupera un oggetto IO di tipo testuale da un file specifico"""
    return open(file_path, "r")

def send_questions(file_path:str)-> TextIO:
    return open(file_path, "r")

import requests

def get_data(URL: str)-> str:
    if URL is None:
        raise ValueError ("L'URL non può essere una stringa vuota.")
    try:
        response = response=requests.get(URL)
        response.raise_for_status()
        return response.text
    
    except requests.exceptions.HTTPError as e:
        raise requests.exceptions.HTTPError(f"Errore HTTP {requests.status_codes} su {URL}:{response.reason}") from e
    
    except requests.exceptions.ConnectionError:
        raise requests.ConnectionError(f"Impossibile connettersi a {URL}")

    except requests.exceptions.Timeout:
        raise requests.Timeout(f"Timeout nella richiesta a {URL}")
    
    except requests.exceptions.RequestException as e:
        raise requests.RequestException(f"Errore di rete imprevisto: {e}") from e
