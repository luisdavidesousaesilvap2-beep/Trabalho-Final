import json
import os

ARQUIVO = "atividades.json"


def salvar_atividades(lista):
    """Salva a lista de atividades no arquivo JSON."""
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=4)


def carregar_atividades():
    """Carrega a lista de atividades do arquivo JSON, se ele existir."""
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []
