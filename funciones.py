import streamlit as st

def filtrar_datos(datos):
    filtrados = datos.copy()

    tipo_dia = st.session_state["tipo_dia"]
    horas = st.session_state["horas"]
    tipo_usuario = st.session_state["tipo_usuario"]

    if tipo_dia != "Todos":
        filtrados = filtrados[filtrados["tipo_dia"] == tipo_dia]

    filtrados = filtrados[
        (filtrados["hora"] >= horas[0]) &
        (filtrados["hora"] <= horas[1])
    ]

    filtrados = filtrados.copy()

    if tipo_usuario == "Ocasionales":
        filtrados["alquileres"] = filtrados["alquileres_ocasionales"]
    elif tipo_usuario == "Registrados":
        filtrados["alquileres"] = filtrados["alquileres_registrados"]
    else:
        filtrados["alquileres"] = filtrados["alquileres_total"]

    return filtrados
