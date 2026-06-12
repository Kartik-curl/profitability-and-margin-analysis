
import numpy as np
from utils import calculate_kpis, cost_vs_sales, div_margin_chart, div_sales_chart, factory_analysis, filter_data, load_data, margin_risk, profit_pareto, profit_pareto_chart, revenue_pareto, revenue_pareto_chart, top_products_by_margin, top_products_by_profit
import streamlit as st
st.set_page_config(layout="wide",page_title="Product Line Profitability & Margin Performance Analysis",initial_sidebar_state="expanded") 

     
st.title("Product Line Profitability & Margin Performance Analysis")

with st.container(horizontal_alignment="center",vertical_alignment="center"):
        col1,col2,col3,col4 = st.columns(4)
        with col1:
                df = calculate_kpis(load_data())
                st.metric("Total Sales",np.round(df["Sales"].sum()))
        with col2:
                st.metric("Total Gross Profit",np.round(df["Gross Profit"].sum(),2))
       
        with col3:
                st.metric("Average Gross Margin",np.round((df["Gross Profit"]/df["Sales"]).sum(),2))
        with col4:
                st.metric("Total Units Sold",df["Units"].sum())



st.sidebar.header("Filters",)
order_date=  st.sidebar.date_input("Enter the order date: ").strftime(r"%d/%m/%Y")
ship_date =  st.sidebar.date_input("Enter the shipping date:  ").strftime(r"%d/%m/%Y")
division =  st.sidebar.selectbox("Enter the division: ",["Chocolate","Sugar","Other"])
margin=  st.sidebar.number_input("Select the margin percentage: ",0,100)
st.header("Product Level Performance") 
def charts(df):
        
        with st.container():
                
                col1,col2 = st.columns(2)
                with col1:
                        st.subheader("Top Products By Profit")
                        products= top_products_by_profit()
                        for i in range(1,11):
                                st.write(f"{i}.\t{products[i-1]}")
                with col2:
                        st.subheader("Top Products By Margin")
                        products= top_products_by_margin()
                        for i in range(1,11):
                                st.write(f"{i}.\t{products[i-1]}")
                        
        with st.container():
                st.header("\n\n\n\n\nDivision Level Performance")
                col1,col2 =st.columns([7,5])
                with col1:
                        fig = div_sales_chart(df)
                        st.pyplot(fig)
                        st.subheader("Division By Sales")
                with col2:
                        fig = div_margin_chart(df)
                        st.pyplot(fig)
                        st.subheader("Margin of Divions")
        with st.container():
                st.header("Cost Diagnostics")
                col1,col2= st.columns(2)
                with col1:
                        fig = cost_vs_sales(df)
                        st.pyplot(fig)
                        st.subheader("Cost vs Sales")
                with col2:
                        data = margin_risk()
                        st.table(data)
                        st.subheader("Margin Risk Table")
filter_chart= False
if st.sidebar.button("Search"):
        st.subheader("Product Table")
        ret,df = filter_data(order_date,ship_date,division,margin)
        if ret:
                df = df.drop("Row ID",axis=1)
                st.dataframe(df)
                charts(df)
                filter_chart = True
        else:
                st.error("No Record Found")
if filter_chart == False:
        charts(calculate_kpis(load_data()))


with st.container():
        st.header("Profit Concentration(Pareto) Analysis")
        st.subheader(r"Products Contributing 80% Revenue")
        col1,col2  = st.columns([1,2])
       
        with col1:
                st.text("Product List")
                data = revenue_pareto()
                st.table(data["Product Name"])
        with col2:
                st.text("Revenue Table")
                st.table(data)
        st.subheader(r"Products Contributing 80% Profit")
        col3,col4 = st.columns([1,2])
       
        with col3:
                st.text("Product List")
                data = profit_pareto()
                st.table(data["Product Name"])
        with col4:
                st.text("Profit Table")
                st.table(data)
with st.container():
        st.subheader("Revenue Pareto Charts")
        col1,col2 = st.columns(2)
        chart1,chart2 = revenue_pareto_chart()
        with col1:
                st.pyplot(chart1)
                st.text("Sales vs Products")
        with col2:
                st.pyplot(chart2)
                st.text("Revenue(%) vs Products")
        st.subheader("Profit Pareto Charts")
        col3,col4 = st.columns(2)
        chart3,chart4 = profit_pareto_chart()
        with col3:
                st.pyplot(chart3)
                st.text("Gross Profit vs Products")
        with col4:
                st.pyplot(chart4)
                st.text("Profit(%) vs Products")

st.header("Factory Wise Analysis")
st.subheader("Factory Table")
table,sales_chart,profit_chart,cost_chart,margin_chart = factory_analysis()
st.table(table)
st.subheader("Factory Charts")
with st.container():
        col1,col2 = st.columns(2)
        with col1:
                st.pyplot(sales_chart)
                st.text("Factory Sales")
        with col2:
                st.pyplot(profit_chart)
                st.text("Factory Profit")
        col3,col4 = st.columns(2)
        with col3:
                st.pyplot(cost_chart)
                st.text("Factory Cost")
        with col4:
                st.pyplot(margin_chart)
                st.text("Factory Margin")
                
                