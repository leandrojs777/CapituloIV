import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cuencas | Cap. IV", page_icon="⛰️", layout="wide")
st.title("⛰️ Análisis por Cuencas")

if 'df_filtered' not in st.session_state:
    st.error("No se encontró el dataset. Por favor inicialice la aplicación desde main.py")
else:
    df_filtered = st.session_state['df_filtered']
    
    if df_filtered.empty:
        st.warning("No hay datos disponibles con los filtros actuales.")
    else:
        # Top Cuencas
        st.markdown("### Producción Agrupada por Cuenca")
        # Aseguramos el nombre de provincia esté para contextualizar 
        cuencas_agrupadas = df_filtered.groupby(['cuenca', 'provincia'])[['prod_pet', 'prod_gas']].sum().reset_index()
        
        # Ordenamos por petróleo descendente
        cuencas_agrupadas = cuencas_agrupadas.sort_values(by='prod_pet', ascending=False)
        
        st.dataframe(cuencas_agrupadas.style.format({'prod_pet': '{:,.2f}', 'prod_gas': '{:,.2f}'}), use_container_width=True)
        
        # Gráfico
        st.markdown("### Comparativa de Extracción por Cuenca")
        st.bar_chart(cuencas_agrupadas, x="cuenca", y=["prod_pet", "prod_gas"], height=500)
