#----------- DEPENDÊNCIAS ----------- #
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard Vendas",
                   page_icon=":bar_chart:",
                   layout='wide'
)

#Leitura do quadro de dados, mapeamento da planilha, definir um nome, pular linhas, coluna 'A' até a 'X', numero de linhas.

@st.cache
def get_data_from_excel():
    df = pd.read_excel(
            io="vendas_varejo.xlsx", 
            engine="openpyxl",
            sheet_name="Vendas",
            usecols="A:X",
            nrows=8400,
    )
    return df
df = get_data_from_excel()

# ----------- BARRA LATERAL ----------- #
st.sidebar.header("Filtre por aqui:")

prioridade = st.sidebar.multiselect(
    "Escolha qual a prioridade:",
    options=df["Prioridade"].unique(),
    default=df["Prioridade"].unique()
)

envio = st.sidebar.multiselect(
    "Escolha qual a forma de envio:",
    options=df["Envio"].unique(),
    default=df["Envio"].unique()
)

regiao = st.sidebar.multiselect(
    "Escolha qual a Região:",
    options=df["Região"].unique(),
    default=df["Região"].unique()
)

segmento = st.sidebar.multiselect(
    "Escolha qual o Segmento:",
    options=df["Segmento"].unique(),
    default=df["Segmento"].unique()
)

embalagem = st.sidebar.multiselect(
    "Escolha qual a Embalagem:",
    options=df["Embalagem"].unique(),
    default=df["Embalagem"].unique()
)


df_selection = df.query(
    "Prioridade == @prioridade & Região == @regiao & Segmento == @segmento & Envio == @envio & Embalagem == @embalagem"
)

st.dataframe(df_selection)

# ----------- PÁGINA PRÍNCIPAL ----------- #
st.title(":bar_chart: Painel de controle do varejo")
st.markdown("##")

#TOP KPI's
quantidade = int(df_selection["Quantidade"].sum())
desconto = int(df_selection["Desconto"].sum())
lucro = round(df_selection["Lucro"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Produtos vendidos:")
    st.subheader(f"{quantidade}")
    
with middle_column:
    st.subheader("Descontos")
    st.subheader(f"R$ {desconto}")
with right_column:
    st.subheader("Lucro")
    st.subheader(f"R$ {lucro}")

st.markdown("---")

# ----------- VENDAS POR PRODUTO ----------- # 
vendasSegmento = (
    df_selection.groupby(by=["Segmento"]).sum()[{quantidade}].sort_values(by={quantidade})
)



fig_vendasSegmento = px.bar(
    vendasSegmento,
    x="quantidade",
    y=vendasSegmento.index,
    orientation="h",
    title="<b>Vendas por linha de produto</b>",
    color_discrete_sequence=["#0083B8"] * len(vendasSegmento),
    template="plotly_white",
)

fig_vendasSegmento.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)






































# ---- ESTILO ESCONDIDO DO STREAMLIT ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)