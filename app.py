import streamlit as st
import pandas as pd

st.title("Manejo de Dataframes")
st.sidebar.title("Herramientas")

archivo = st.sidebar.file_uploader("Selecciona tu archivo a cargar")
if archivo in not None:
  sr.write("Su archivo fue cargado exitosamente")
  if archivo.name.endswith(".csv"):
    datos = pd.read_csv(archivo)
  if archivo.name.endswith(".xls"):
    datos = pd.read_excel(archivo)
  st.write(datos)
else:
  sr.write("Cargue su archivo")
