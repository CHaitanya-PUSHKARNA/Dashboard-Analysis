import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(page_title="RCMS error dashboard",
                   page_icon=":potted_plant:",
                   layout="wide"
)
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
         io='supermarkt_sales.xlsx',
         engine='openpyxl',
         sheet_name='Sales',
         skiprows=3,
         usecols='B:R',
         nrows=1000,
    )
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df
df = get_data_from_excel()
#st.dataframe(df)

st.sidebar.header("Please Filter Here:")
city = st.sidebar.multiselect(
    "Select The City:",
    options= df["City"].unique(),
    default= df["City"].unique()
)
customer_type =st.sidebar.multiselect(
    "Select The Customer Type:",
    options=df["Customer_type"].unique(),
    default=df["Customer_type"].unique()
)
gender =st.sidebar.multiselect(
    "Select The Gender:",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)
df_selection = df.query(
    "City ==@city & Customer_type == @customer_type & Gender == @gender"
)
#st.dataframe(df_selection)

st.title(":bar_chart: Sales Dashboard")
st.markdown('##')

total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(),1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sales_by_transaction = round (df_selection["Total"].mean(),2)

left_column, middle_column, right_column = st.columns(3)
with left_column :
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")

with middle_column :
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating}{star_rating}")
with right_column:
    st.subheader("Average Sales Per Transaction:")
    st.subheader(f"US $ {average_sales_by_transaction }")

st.markdown("---")
sales_by_product_line = df_selection.groupby("Product line")["Total"].sum().sort_values(ascending=False)

fig_product_sales = px.bar(
    sales_by_product_line,
    x ="Total",
    y=sales_by_product_line.index,
    orientation="h",
    title="<b>Sales By Product Line</b>",
    color_discrete_sequence=["#0083B8"]*len(sales_by_product_line),
    template = "plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)



fig_line = px.line(
    sales_by_product_line,
    x=sales_by_product_line.index,
    y="Total",
    title="Sales By Product Line (Line Chart)"

)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_product_sales , use_container_width=True)
right_column.plotly_chart(fig_line , use_container_width=True)


fig_area = px.area(
    sales_by_product_line,
    x=sales_by_product_line.index,
    y="Total",
    title="Sales By Product Line (Area Chart)"
)



fig_pie = px.pie(
    sales_by_product_line,
    values="Total",
    names=sales_by_product_line.index,
    title="Sales By Product Line (Pie Chart)"
)

left_column, right_column = st.columns(2)
left_column.plotly_chart( fig_pie, use_container_width=True)
right_column.plotly_chart(fig_area , use_container_width=True)

## to run streamlit file ("python -m streamlit run file_name.py")

