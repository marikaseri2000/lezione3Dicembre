from repository_layer import get_questions_from_file

def get_domanda(file_path: str) -> str:
    with get_questions_from_file(file_path) as file:
        content=file.read()
        return content

def get_lista_domande(file_path:str) -> list[str]:
    lista_domande:list[str] = []
    with get_questions_from_file(file_path) as f:
        for i in f:
            #print(i)
            lista_domande.append(i.strip())
    return lista_domande