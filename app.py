
import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    return pd.read_excel("Estrategia_Torneos_Slowplay_OOP.xlsx", engine="openpyxl")

def main():
    st.title("Estrategia Postflop - José Luis Sernaque")
    df = cargar_datos()

    # Filtros principales
    posicion = st.selectbox("Tu posición", sorted(df['Tu posición'].dropna().unique()))
    tipo_rival = st.selectbox("Tipo de Rival", sorted(df['Tipo de Rival'].dropna().unique()))
    tipo_mano = st.selectbox("Tipo de Mano", sorted(df['Tipo de Mano'].dropna().unique()))
    textura = st.selectbox("Textura del Board", sorted(df['Textura del Board'].dropna().unique()))
    situacion = st.selectbox("Situación Preflop", sorted(df['Situación Preflop'].dropna().unique()))

    # Filtrar resultados
    resultado = df[
        (df['Tu posición'] == posicion) &
        (df['Tipo de Rival'] == tipo_rival) &
        (df['Tipo de Mano'] == tipo_mano) &
        (df['Textura del Board'] == textura) &
        (df['Situación Preflop'] == situacion)
    ]

    if resultado.empty:
        st.warning("No hay estrategia definida para esta combinación. Intenta con otra.")
    else:
        row = resultado.iloc[0]
        st.subheader("🎯 Estrategia Recomendada")
        st.markdown(f"**Rango Estimado del Rival:** {row['Rango Estimado Rival']}")
        st.markdown(f"**Equity Aproximada:** {row['Equity Aproximada']}")
        st.markdown(f"**Rango Defensa Preflop:** {row['Rango Defensa Preflop']}")
        st.markdown(f"**Acción en Flop:** {row['Acción Flop']}")
        st.markdown(f"**Acción en Turn:** {row['Acción Turn']}")
        st.markdown(f"**Acción en River:** {row['Acción River']}")
        st.markdown(f"**Si el Villano Resube:** {row['Si Villano Resube']}")
        st.markdown(f"**Sizing si Resubes:** {row['Sizing si Resubes']}")
        st.markdown(f"**Consejo Multiway:** {row['Consejo Multiway']}")
        st.markdown(f"**Estrategia OOP:** {row['Estrategia OOP']}")

if __name__ == "__main__":
    main()
