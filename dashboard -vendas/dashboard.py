#----------- DEPENDÊNCIAS ----------- #
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Dashboard Vendas",
                   page_icon=":bar_chart:",
                   layout='wide'
)

# ----------- LER A PLANILHA DO EXCEL ----------- #
@st.cache
def get_data_from_excel():
    df = pd.read_excel(
        io="supermarkt_sales.xlsx",
        engine="openpyxl",
        sheet_name="Sales",
        skiprows=3,
        usecols="B:R",
        nrows=1000,
    )
    # adicionando a coluna hora no dataframe
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df

df = get_data_from_excel()

# ----------- BARRA LATERAL ----------- #
st.sidebar.header("Filtre por aqui:")

city = st.sidebar.multiselect(
    "Escolha a cidade:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

customer_type = st.sidebar.multiselect(
    "Escolha o tipo de cliente:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)

gender = st.sidebar.multiselect(
    "Escolha o Gênero:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

df_selection = df.query(
    "City == @city & Customer_type == @customer_type & Gender == @gender"
)

st.dataframe(df_selection)

# ----------- PÁGINA PRÍNCIPAL ----------- #
st.title(":bar_chart: Painel de controle de vendas")
st.markdown("##")

#TOP KPI's
total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sale_by_transaction = round(df_selection["Total"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total de vendas:")
    st.subheader(f"US $ {total_sales:,}")
with middle_column:
    st.subheader("Classificação média")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Média de vendas por transação:")
    st.subheader(f"US $ {average_sale_by_transaction}")

st.markdown("---")

# ----------- VENDAS POR PRODUTO ----------- # 
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values(by="Total")
)

fig_product_sales = px.bar(
    sales_by_product_line,
    x="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Vendas por linha de produto</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

# ----------- VENDAS POR HORA (CÓDIGO DE BARRAS) ----------- #
sales_by_hour = df_selection.groupby(by=["hour"]).sum()[["Total"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x=sales_by_hour.index,
    y="Total",
    title="<b>Vendas por hora</b>",
    color_discrete_sequence=["#0083B8"] * len(sales_by_hour),
    template="plotly_white",
)

fig_hourly_sales.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_hourly_sales, use_container_width=True)
right_column.plotly_chart(fig_product_sales, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)