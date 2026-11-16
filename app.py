import streamlit as st

st.sidebar.title("BiciDatos")

tipo_usuario = st.sidebar.selectbox(
    "Tipo de usuario", ["Todos", "Ocasionales", "Registrados"]
)
tipo_dia = st.sidebar.radio(
    "Tipo de día", ["Todos", "Laborable", "No laborable"]
)
horas = st.sidebar.slider("Horas del día", 0, 23, (0, 23))

st.session_state["tipo_usuario"] = tipo_usuario
st.session_state["tipo_dia"] = tipo_dia
st.session_state["horas"] = horas

pagina_1 = st.Page("explorar.py", title="Explorar los datos")
pagina_2 = st.Page("comparar.py", title="Comparar horarios")

navegacion = st.navigation([pagina_1, pagina_2])
navegacion.run()
