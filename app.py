import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    return pd.read_excel("Estrategia_Torneos_Slowplay_OOP.xlsx", engine="openpyxl")

def main():
    st.title("Estrategia de Poker - José Luis Sernaque")
    df = cargar_datos()

    posicion = st.selectbox("Tu posición", sorted(df['Tu posición'].dropna().unique()))
    stack = st.selectbox("Stack (BB)", sorted(df['Tu stack'].dropna().unique()))
    vs_accion = st.selectbox("Acción previa", sorted(df['Acción previa'].dropna().unique()))
    tipo_rival = st.selectbox("Tipo de jugador rival", sorted(df['Tipo de jugador'].dropna().unique()))

    filtrado = df[
        (df['Tu posición'] == posicion) &
        (df['Tu stack'] == stack) &
        (df['Acción previa'] == vs_accion) &
        (df['Tipo de jugador'] == tipo_rival)
    ]

    st.write("📊 Resultado filtrado:")
    st.dataframe(filtrado)

if __name__ == "__main__":
    main()
