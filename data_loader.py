import pandas as pd
import streamlit as st
import os

@st.cache_data
def load_and_clean_data(file_path="data/produccin-de-pozos-de-gas-y-petrleo-2026.csv"):
    """
    Carga y procesa el dataset Cap. IV asegurando tipos de datos listos para
    análisis usando pandas. Manejo optimizado para Streamlit Cloud.
    """
    if not os.path.exists(file_path):
        st.error(f"El archivo {file_path} no fue encontrado.")
        return pd.DataFrame()
        
    # Cargar CSV
    try:
        df = pd.read_csv(file_path, low_memory=False)
    except Exception as e:
        st.error(f"Error cargando los datos: {e}")
        return pd.DataFrame()
        
    # 1. Limpieza y Casteo estricto de valores volumétricos
    cols_to_numeric = ['prod_pet', 'prod_gas', 'prod_agua']
    for col in cols_to_numeric:
        if col in df.columns:
            # Reemplazar comas por puntos en caso de separadores europeos y forzar numérico
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', '.'), errors='coerce').fillna(0)

    # 2. Normalizar columnas de agrupamiento (rellenar nulos con "Sin Datos")
    cols_to_fill = [
        'tipopozo', 'tipoestado', 'tipoextraccion', 'provincia', 
        'tipo_de_recurso', 'cuenca', 'empresa', 'areayacimiento'
    ]
    for col in cols_to_fill:
        if col in df.columns:
            df[col] = df[col].fillna('Sin Datos')

    return df
