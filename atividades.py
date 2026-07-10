from datetime import datetime


def cadastrar_atividade(lista, disciplina, descricao):
    """Cria uma nova atividade (dicionário) e adiciona na lista."""
    nova_atividade = {
        "disciplina": disciplina,
        "descricao": descricao,
        "concluida": False,
        "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    lista.append(nova_atividade)


def listar_pendentes(lista):
    """Retorna só as atividades que ainda não foram concluídas."""
    pendentes = []
    for atividade in lista:
        if not atividade["concluida"]:
            pendentes.append(atividade)
    return pendentes


def listar_concluidas(lista):
    """Retorna só as atividades já concluídas."""
    concluidas = []
    for atividade in lista:
        if atividade["concluida"]:
            concluidas.append(atividade)
    return concluidas


def marcar_concluida(lista, indice):
    """Marca a atividade de determinado índice como concluída."""
    if 0 <= indice < len(lista):
        lista[indice]["concluida"] = True
        return True
    return False


def editar_atividade(lista, indice, nova_disciplina, nova_descricao):
    """Edita disciplina e descrição de uma atividade existente."""
    if 0 <= indice < len(lista):
        lista[indice]["disciplina"] = nova_disciplina
        lista[indice]["descricao"] = nova_descricao
        return True
    return False


def remover_atividade(lista, indice):
    """Remove uma atividade da lista pelo índice."""
    if 0 <= indice < len(lista):
        lista.pop(indice)
        return True
    return False


def pesquisar_por_disciplina(lista, termo):
    """Retorna atividades cuja disciplina contém o termo pesquisado."""
    resultado = []
    for atividade in lista:
        if termo.lower() in atividade["disciplina"].lower():
            resultado.append(atividade)
    return resultado
