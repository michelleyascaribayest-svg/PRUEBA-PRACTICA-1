import streamlit as st
import pandas as pd
import sweetviz as sv



# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="PRUEBA UNIDAD 1",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# ENCABEZADO
# =========================================================

st.image("logo.png", width=350)

st.markdown("""
<div style='text-align:center'>

<h1 style='color:#0B5394'>
ECU 911 INCIDENTES DICIEMBRE 2025
</h1>

<h3>
Aplicación Web Interactiva con Streamlit
</h3>

<hr>

<h4>
Instituto Superior Tecnológico del Azuay
</h4>

<h4>
Carrera de Tecnología Superior en Big Data
</h4>

</div>
""", unsafe_allow_html=True)

# =========================================================
# DATOS DEL ESTUDIANTE
# =========================================================

st.info("""
### Información Académica

**Nombre:** Michelle Yascaribay

**Asignatura:** Minería de Datos 

**Paralelo:** Big Data 
""")

# =========================================================
# INSTRUCCIONES
# =========================================================

st.success("""
### Instrucciones de Uso

1. Visualice el dataset.
2. Identifique los tipos de datos.
3. Explore las estadísticas descriptivas.
4. Analice los gráficos generados.
5. Ejecute el reporte EDA automático.
""")
import streamlit as st
import pandas as pd
import sweetviz as sv

st.title("Análisis Automático de Datos")

archivo = st.file_uploader(
    "Suba un archivo",
    type=["csv", "xlsx"]
)

if archivo is not None:

    if archivo.name.endswith(".csv"):
        df = pd.read_csv(archivo, delimiter=";")

    else:
        df = pd.read_excel(archivo)

    st.dataframe(df)

    reporte = sv.analyze(df)

    reporte.show_html(
        "reporte.html",
        open_browser=False
    )

    with open("reporte.html", "r", encoding="utf-8") as f:
        html = f.read()

    st.components.v1.html(
        html,
        width=1000,
        height=1000,
        scrolling=True
    )