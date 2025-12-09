from typing import TextIO

def get_questions_from_file(file_path:str) -> TextIO:  #IO sta per input e output
    """Recupera un oggetto IO di tipo testuale da un file specifico"""
    return open(file_path, "r")

def send_questions(file_path:str)-> TextIO:
    return open(file_path, "r")