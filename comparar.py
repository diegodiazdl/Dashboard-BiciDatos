import streamlit as st
import matplotlib.pyplot as plt
from funciones import filtrar_datos

st.title("Comparar horarios")

if "datos" not in st.session_state:
    st.info("Primero entra a Explorar los datos y carga bicicletas_listas.csv.")
else:
    filtrados = filtrar_datos(st.session_state["datos"])

    promedios = filtrados.groupby("hora")["alquileres"].mean()

    color = st.color_picker("Color de las barras", "#197A8D")

    fig, ax = plt.subplots()
    ax.bar(promedios.index, promedios.values, color=color)
    ax.set_xlabel("Hora del día")
    ax.set_ylabel("Alquileres por hora observada")
    ax.set_xticks(promedios.index)
    st.write(fig)
    plt.close(fig)

    if st.checkbox("Mostrar tabla de promedios"):
        st.dataframe(promedios.reset_index(name="Promedio de alquileres"))

    limite = st.number_input(
        "Límite de alquileres por hora", min_value=0, value=250, step=1
    )

    superiores = promedios[promedios > limite]
    st.write("Horarios con promedio mayor que el límite")
    st.metric("Horas que superan el límite", f"{len(superiores)}/{len(promedios)}")

    if len(superiores) > 0:
        horarios = [f"{hora:02d}:00" for hora in superiores.index]
        st.write("Horarios: " + ", ".join(horarios) + ".")
    else:
        st.write("Ninguna hora supera el límite indicado.")
