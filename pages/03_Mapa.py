import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mapa Yacimientos | Cap. IV", page_icon="🗺️", layout="wide")
st.title("🗺️ Mapa de Yacimientos")
st.markdown("*Concentración productiva a nivel de área geográfica de concesión*")

if 'df_filtered' not in st.session_state:
    st.error("No se encontró el dataset. Por favor inicialice la aplicación desde main.py")
else:
    df_filtered = st.session_state['df_filtered']
    
    if df_filtered.empty:
        st.warning("No hay datos disponibles con los filtros actuales.")
    else:
        # Agrupación por área de yacimiento
        st.markdown("### Producción por Yacimiento Aportante")
        
        yacimientos = df_filtered.groupby(['areayacimiento', 'provincia'])[['prod_pet', 'prod_gas']].sum().reset_index()
        yacimientos = yacimientos.sort_values(by="prod_pet", ascending=False)
        
        st.dataframe(yacimientos.style.format({'prod_pet': '{:,.2f}', 'prod_gas': '{:,.2f}'}), use_container_width=True)
        
        # Visualización gráfica como heatmap alternativo en barras 
        st.markdown("### Rendimiento Top 15 Áreas")
        st.bar_chart(yacimientos.head(15), x='areayacimiento', y=['prod_pet', 'prod_gas'], height=500)
