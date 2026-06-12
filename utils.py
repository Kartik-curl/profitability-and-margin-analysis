
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd


def load_data():
    df = pd.read_csv("Nassau Candy Distributor.csv")
    return df

def data_info():
    df = load_data()
    print(df._data)
    print(df.columns)
    print(df.shape)
    print(type(df))
    print(df.notna().sum())
    print(df.describe())
    print(df.head())
    
def clean_data(df):
    #checking zero sales
    for i in df["Sales"]:
        if i <=0:
            print(i)
    else:
        print("Found No Sale less than or equal to 0")

    #finding the rows where cost is more than sales
    count = 0
    for i in range(10194):
        if df["Cost"][i]  > df["Sales"][i]:
            count+=1
    if count == 0 :
        print("Found no record where cose is more than sales")
    else:
        print(f"Found {count} records where cost is more than sales")

    #checking missing values
    if df.isnull().sum().sum() == 0:
        print("No missing values in the dataset")
    else:
        df.dropna()



    #checking duplicate records in dataset
    if df.duplicated().sum() == 0:
        print("There is no duplicate record in the dataset")
    else:
        df = df.drop_duplicates()
        
    #checking no. of divisions 
    print(df["Division"].value_counts())
    print(df["Product Name"].value_counts())
    print(df["Product ID"].value_counts())

def calculate_kpis(df):
    df["Gross Margin"] = (df["Gross Profit"]/df["Sales"])*100
    df["Profit Per Unit"] = df["Gross Margin"]/df["Units"]
    df["Revenue Contribution"] = (df["Sales"]/df["Sales"].sum())*100
    df["Profit Contribution"] = (df["Gross Profit"]/df["Gross Profit"].sum())*100
    return df

def filter_data(order_date=None,ship_date=None,division=None,margin=None):
    df = calculate_kpis(load_data()) 
    df["Order Date"] = df["Order Date"].astype(str).str.replace("-","/",regex=False)
    df["Ship Date"] = df["Ship Date"].astype(str).str.replace("-","/",regex=False)
  
    df = df[(df["Order Date"] == order_date) 
            & (df["Ship Date"] == ship_date)
            & (df["Division"] == division )
            |(df["Gross Margin"] == margin)]
   
    if not df.empty:
        return True,df
    else:
        return False,None
def top_products_by_profit():
    df = calculate_kpis(load_data())
    top_by_profit = dict(df.groupby("Product Name")["Profit Contribution"].sum())
    top_10 = dict(sorted(top_by_profit.items(),key= lambda x: x[1],reverse=True)[:10])
    return list(top_10.keys())

def top_products_by_margin():
    df = calculate_kpis(load_data())
    product_by_margin = dict(df.groupby("Product Name")["Gross Margin"].sum())
    top_10 = dict(sorted(product_by_margin.items(),key = lambda x: x[1],reverse=True)[:10])
    return list(top_10.keys())    

def div_sales_chart(df):
    
    div_df = df.groupby("Division")[["Sales","Gross Profit"]].sum()
    div_df.plot(kind="bar",figsize=(8,5))
    fig1 = plt.gcf()
    plt.xlabel("Divisions")
    plt.ylabel("Amount")
  

    return fig1
def div_margin_chart(df):
   
    div_df = dict(df.groupby("Division")["Gross Margin"].sum())
   
    fig2,ax = plt.subplots() 
    
    ax.pie(list(div_df.values()),autopct = "%1.1f%%",radius=0.7,labels = list(div_df.keys()))

    return fig2
def cost_vs_sales(df):
   
    x = df["Cost"]
    y = df["Sales"]
    fig3,ax = plt.subplots()
    ax.scatter(x,y,c="Red")
    ax.set_xlabel("Cost")
    ax.set_ylabel("Sales")
    return fig3
def margin_risk():
    df = calculate_kpis(load_data())
    products = dict(df.groupby("Product Name")["Gross Margin"].sum())
    risk=[]
    total= 0
    for i in products.values():
        total += i
    for i in products.values():
        risk.append(np.round((i/total)*100,2))
    risk_df = pd.DataFrame({"Product":list(products.keys()),"Margin(%)":risk})
   
    risk_df.loc[risk_df["Margin(%)"]>10, "Status"]  = "Good"
    risk_df.loc[risk_df["Margin(%)"]<10 ,"Status"]= "Risk"
    return risk_df
def revenue_pareto():
    df = calculate_kpis(load_data())
    revenue= df.groupby("Product Name")["Sales"].sum()
    revenue = revenue.sort_values(ascending=False)
    revenue = revenue.reset_index()
    revenue["cum_revenue"]=revenue["Sales"].cumsum()
    revenue["cum(%)"]= np.round((revenue["cum_revenue"]/revenue["Sales"].sum())*100,1)
    return revenue.loc[:3]

def profit_pareto():
    df = calculate_kpis(load_data())
    profit = df.groupby("Product Name")["Gross Profit"].sum()
    profit = profit.sort_values(ascending=False)
    profit = profit.reset_index()
    profit["cum_profit"]= profit["Gross Profit"].cumsum()
    profit["cum(%)"] = np.round((profit["cum_profit"]/profit["Gross Profit"].sum())*100,1)
    return profit.loc[:3]
def revenue_pareto_chart():
    df= revenue_pareto()
    x = ["Product1","Product2","Product3","Product4"]
    y = df["Sales"]
    fig1 ,ax = plt.subplots()
    ax.bar(x,y)
    y1= df["cum(%)"]
    fig2,ax =plt.subplots()
    ax.scatter(x,y1)
    return fig1,fig2
def profit_pareto_chart():
    df= profit_pareto()
    x = ["Product1","Product2","Product3","Product4"]
    y = df["Gross Profit"]
    fig1 ,ax = plt.subplots()
    ax.bar(x,y)
    y1= df["cum(%)"]
    fig2,ax =plt.subplots()
    ax.scatter(x,y1)
    return fig1,fig2

def factory_analysis():
    df = calculate_kpis(load_data())
    factory_map = {
        "Wonka Bar - Nutty Crunch Surprise":"Lot's O'Nuts",
        "Wonka Bar - Fudge Mallows":"Lot's O'Nuts",
        "Wonka Bar - Scrumdiddlyumptious":"Lot's O'Nuts",
        "Wonka Bar - Milk Chocolate":"Wicked Choccy's",
        "Wonka Bar - Triple Dazzle Caramel":"Wicked Choccy's",
        "Laffy Taffy":"Sugar Shack",
        "SweeTARTS":"Sugar Shack",
        "Nerds":"Sugar Shack",
        "Fun Dip":"Sugar Shack",
        "Fizzy Lifting Drinks":"Sugar Shack",
        "Everlasting Gobstopper":"Secret Factory",
        "Hair Toffee":"The Other Factory",
        "Lickable Wallpaper": "Secret Factory",
        "Wonka Gum":"Secret Factory",
        "Kazookies":"The Other Factory"
        
    }
    
    df["Factory"]= df["Product Name"].map(factory_map)
    grouped_data = df.groupby("Factory")[["Sales","Gross Profit","Cost","Gross Margin"]].sum().sort_values(by=["Sales"],ascending=False)
    grouped = list(df["Factory"].unique())
    grouped.pop(2)
    grouped = pd.Series(grouped)
    #sales chart,gross chart and margin chart and cost hart
    fig1,ax = plt.subplots()
    ax.bar(grouped,np.round(grouped_data["Sales"]))
    fig2,ax = plt.subplots()
    ax.bar(grouped,np.round(grouped_data["Gross Profit"]))
    fig3,ax = plt.subplots()
    ax.bar(grouped,grouped_data["Cost"])
    fig4,ax = plt.subplots()
    ax.bar(grouped,grouped_data["Gross Margin"])

    return grouped_data,fig1,fig2,fig3,fig4
