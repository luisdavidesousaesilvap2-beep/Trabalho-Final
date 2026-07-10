import streamlit as st
from atividades import (
    cadastrar_atividade,
    listar_pendentes,
    listar_concluidas,
    marcar_concluida,
    editar_atividade,
    remover_atividade,
    pesquisar_por_disciplina
)
from dados import salvar_atividades, carregar_atividades

st.set_page_config(page_title="Organizador de Atividades", page_icon="📚")

if "atividades" not in st.session_state:
    st.session_state.atividades = carregar_atividades()

st.title("📚 Organizador de Atividades Escolares")
st.write("Bem-vindo! Use o menu na barra lateral para navegar.")

menu = st.sidebar.selectbox(
    "Menu",
    ["Cadastrar", "Listar Todas", "Pendentes", "Concluídas", "Editar", "Remover", "Pesquisar"]
)

if menu == "Cadastrar":
    st.subheader("Cadastrar nova atividade")

    disciplina = st.text_input("Disciplina")
    descricao = st.text_input("Descrição da atividade")

    if st.button("Cadastrar"):
        if disciplina and descricao:
            cadastrar_atividade(st.session_state.atividades, disciplina, descricao)
            salvar_atividades(st.session_state.atividades)
            st.success("Atividade cadastrada com sucesso!")
        else:
            st.warning("Preencha disciplina e descrição antes de cadastrar.")

elif menu == "Listar Todas":
    st.subheader("Todas as atividades")

    if len(st.session_state.atividades) == 0:
        st.info("Nenhuma atividade cadastrada ainda.")
    else:
        for indice, atividade in enumerate(st.session_state.atividades):
            status = "✅ Concluída" if atividade["concluida"] else "⏳ Pendente"
            st.write(f"**{indice}. {atividade['disciplina']}** - {atividade['descricao']}")
            st.write(f"{status} | Cadastrada em: {atividade['data_cadastro']}")

            if not atividade["concluida"]:
                if st.button("Marcar como concluída", key=f"concluir_{indice}"):
                    marcar_concluida(st.session_state.atividades, indice)
                    salvar_atividades(st.session_state.atividades)
                    st.rerun()

            st.divider()

elif menu == "Pendentes":
    st.subheader("Atividades pendentes")

    pendentes = listar_pendentes(st.session_state.atividades)

    if len(pendentes) == 0:
        st.info("Nenhuma atividade pendente. 🎉")
    else:
        for atividade in pendentes:
            st.write(f"**{atividade['disciplina']}** - {atividade['descricao']}")
            st.write(f"Cadastrada em: {atividade['data_cadastro']}")
            st.divider()

elif menu == "Concluídas":
    st.subheader("Atividades concluídas")

    concluidas = listar_concluidas(st.session_state.atividades)

    if len(concluidas) == 0:
        st.info("Nenhuma atividade concluída ainda.")
    else:
        for atividade in concluidas:
            st.write(f"**{atividade['disciplina']}** - {atividade['descricao']}")
            st.write(f"Cadastrada em: {atividade['data_cadastro']}")
            st.divider()

elif menu == "Editar":
    st.subheader("Editar atividade")

    if len(st.session_state.atividades) == 0:
        st.info("Nenhuma atividade cadastrada ainda.")
    else:
        opcoes = []
        for indice, atividade in enumerate(st.session_state.atividades):
            opcoes.append(f"{indice} - {atividade['disciplina']} - {atividade['descricao']}")

        escolha = st.selectbox("Escolha a atividade para editar", opcoes)
        indice_escolhido = int(escolha.split(" - ")[0])

        atividade_atual = st.session_state.atividades[indice_escolhido]

        nova_disciplina = st.text_input("Nova disciplina", value=atividade_atual["disciplina"])
        nova_descricao = st.text_input("Nova descrição", value=atividade_atual["descricao"])

        if st.button("Salvar alterações"):
            editar_atividade(st.session_state.atividades, indice_escolhido, nova_disciplina, nova_descricao)
            salvar_atividades(st.session_state.atividades)
            st.success("Atividade atualizada com sucesso!")
            st.rerun()

elif menu == "Remover":
    st.subheader("Remover atividade")

    if len(st.session_state.atividades) == 0:
        st.info("Nenhuma atividade cadastrada ainda.")
    else:
        opcoes = []
        for indice, atividade in enumerate(st.session_state.atividades):
            opcoes.append(f"{indice} - {atividade['disciplina']} - {atividade['descricao']}")

        escolha = st.selectbox("Escolha a atividade para remover", opcoes)
        indice_escolhido = int(escolha.split(" - ")[0])

        if st.button("Remover"):
            remover_atividade(st.session_state.atividades, indice_escolhido)
            salvar_atividades(st.session_state.atividades)
            st.success("Atividade removida com sucesso!")
            st.rerun()

elif menu == "Pesquisar":
    st.subheader("Pesquisar atividades por disciplina")

    termo = st.text_input("Digite o nome (ou parte do nome) da disciplina")

    if termo:
        resultados = pesquisar_por_disciplina(st.session_state.atividades, termo)

        if len(resultados) == 0:
            st.info("Nenhuma atividade encontrada para essa disciplina.")
        else:
            for atividade in resultados:
                status = "✅ Concluída" if atividade["concluida"] else "⏳ Pendente"
                st.write(f"**{atividade['disciplina']}** - {atividade['descricao']}")
                st.write(f"{status} | Cadastrada em: {atividade['data_cadastro']}")
                st.divider()
    else:
        st.write("Digite algo acima para pesquisar.")
