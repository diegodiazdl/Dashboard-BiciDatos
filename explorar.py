import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from funciones import filtrar_datos

st.title("Explorar los datos")

archivo = st.file_uploader("Selecciona bicicletas_listas.csv", type="csv")

if st.button("Cargar datos"):
    if archivo is not None:
        datos = pd.read_csv(archivo, encoding="utf-8-sig", parse_dates=["fecha"])
        st.session_state["datos"] = datos
    else:
        st.warning("Primero selecciona el archivo bicicletas_listas.csv.")

if "datos" not in st.session_state:
    st.info("Para comenzar, selecciona bicicletas_listas.csv y haz clic en Cargar datos.")
else:
    datos = st.session_state["datos"]
    st.success(f"{len(datos):,} registros cargados.")

    filtrados = filtrar_datos(datos)
    total = filtrados["alquileres"].sum()
    promedio = filtrados["alquileres"].mean()

    st.metric("Total de alquileres", f"{total:,.0f}".replace(",", "."))
    st.metric("Promedio por hora observada", f"{promedio:.1f}".replace(".", ","))

    pestana_grafico, pestana_datos = st.tabs(["Gráfico diario", "Datos"])

    with pestana_grafico:
        diario = filtrados.groupby("fecha")["alquileres"].sum()

        fig, ax = plt.subplots()
        ax.plot(diario.index, diario.values)
        ax.set_xlabel("Fecha")
        ax.set_ylabel("Alquileres por día")
        fig.autofmt_xdate()
        st.write(fig)
        plt.close(fig)
        st.write("Cada total incluye las horas que conservan los filtros.")

    with pestana_datos:
        st.dataframe(filtrados)

        csv_filtrado = filtrados.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "Descargar datos filtrados",
            data=csv_filtrado,
            file_name="bicicletas_filtradas.csv",
            mime="text/csv"
        )

        st.write(
            "Fanaee-T, H. (2013). Bike Sharing [Conjunto de datos]. "
            "UCI Machine Learning Repository. "
            "https://doi.org/10.24432/C5W894. Licencia CC BY 4.0."
        )
        st.link_button(
            "Consultar la fuente en UCI",
            "https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset"
        )
