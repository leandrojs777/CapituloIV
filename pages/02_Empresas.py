import streamlit as st
import pandas as pd

st.set_page_config(page_title="Empresas | Cap. IV", page_icon="🏢", layout="wide")
st.title("🏢 Rendimiento por Empresa")

if 'df_filtered' not in st.session_state:
    st.error("No se encontró el dataset. Por favor inicialice la aplicación desde main.py")
else:
    df_filtered = st.session_state['df_filtered']
    
    if df_filtered.empty:
        st.warning("No hay datos disponibles con los filtros actuales.")
    else:
        st.markdown("### Top Empresas Extractoras")
        empresas_agrupa = df_filtered.groupby(['empresa'])[['prod_pet', 'prod_gas', 'prod_agua']].sum().reset_index()
        
        # Top 10 Productoras de Petróleo 
        st.markdown("##### Ranking Productoras Petróleo")
        top_petroleo = empresas_agrupa.sort_values(by='prod_pet', ascending=False)
        st.bar_chart(top_petroleo.head(10), x='empresa', y='prod_pet', height=400, color="#FF4B4B")
        
        # Tabla exhaustiva agregada
        st.markdown("##### Consolidado por Compañía")
        st.dataframe(top_petroleo.style.format({
            'prod_pet': '{:,.2f}', 
            'prod_gas': '{:,.2f}', 
            'prod_agua': '{:,.2f}'
        }), use_container_width=True)
