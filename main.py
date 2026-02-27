import streamlit as st
import data_loader

# Configuración de página global
st.set_page_config(
    page_title="Sistema Analítico Cap. IV | Antigravity",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título y Descripción Header
st.title("⚡ Dashboard Analítico de Energía - Cap. IV")
st.markdown("Plataforma interactiva para visualizar producción de pozos basada en el dataset procesado.")

# Carga de datos desde utilitario caché de Streamlit
df = data_loader.load_and_clean_data()

# ----------------- SIDEBAR GLOBAL ----------------- #
st.sidebar.header("Filtros Globales")

# Multiselectores enlazados interactivos
if not df.empty:
    tipo_pozo_sel = st.sidebar.multiselect("Tipo de Pozo", options=df['tipopozo'].unique())
    tipo_estado_sel = st.sidebar.multiselect("Estado", options=df['tipoestado'].unique())
    tipo_ext_sel = st.sidebar.multiselect("Sistema de Extracción", options=df['tipoextraccion'].unique())
    prov_sel = st.sidebar.multiselect("Provincia", options=df['provincia'].unique())
    tipo_rec_sel = st.sidebar.multiselect("Tipo de Recurso", options=df['tipo_de_recurso'].unique())
    
    # Aplicar Filtros (Lógica)
    df_filtered = df.copy()
    if tipo_pozo_sel:
        df_filtered = df_filtered[df_filtered['tipopozo'].isin(tipo_pozo_sel)]
    if tipo_estado_sel:
        df_filtered = df_filtered[df_filtered['tipoestado'].isin(tipo_estado_sel)]
    if tipo_ext_sel:
        df_filtered = df_filtered[df_filtered['tipoextraccion'].isin(tipo_ext_sel)]
    if prov_sel:
        df_filtered = df_filtered[df_filtered['provincia'].isin(prov_sel)]
    if tipo_rec_sel:
        df_filtered = df_filtered[df_filtered['tipo_de_recurso'].isin(tipo_rec_sel)]
    
    # Compartir datos filtrados con las subpáginas a través de Session State
    st.session_state['df_filtered'] = df_filtered

    # ----------------- KPIs PRINCIPALES (MAIN VIEW) ----------------- #
    st.markdown("### Indicadores Clave de Producción (Filtrados)")
    
    # Totales redondeados
    total_petroleo = df_filtered['prod_pet'].sum()
    total_gas = df_filtered['prod_gas'].sum()
    total_agua = df_filtered['prod_agua'].sum()
    total_pozos = len(df_filtered)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Pozos Procesados", f"{total_pozos:,}")
    with col2:
        st.metric("Prod. Petróleo (m³)", f"{total_petroleo:,.2f}")
    with col3:
        st.metric("Prod. Gas (miles m³)", f"{total_gas:,.2f}")
    with col4:
        st.metric("Prod. Agua (m³)", f"{total_agua:,.2f}")
    
    # Breve visualización gráfica global
    st.markdown("### Resumen Rápido por Provincia")
    
    if not df_filtered.empty:
        df_prov = df_filtered.groupby('provincia')[['prod_pet', 'prod_gas']].sum().reset_index()
        st.bar_chart(data=df_prov, x='provincia', y=['prod_pet', 'prod_gas'], height=400)
    else:
        st.warning("Los filtros actuales no devuelven datos.")

else:
    st.warning("El dataset no pudo cargarse correctamente o está vacío.")
