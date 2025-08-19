import streamlit as st
import requests
import pandas as pd
from calendar import month_name

API_URL='http://localhost:8000'

def analytics_month_tab():
    st.header('Expense Analytics By Month')

    response = requests.get(f"{API_URL}/analytics/")
    response=response.json()

    df=pd.DataFrame(response)

    df['month_name']=pd.to_datetime(df['month'], format='%Y/%m').dt.month
    df['month_name']=df['month_name'].apply(lambda x: month_name[x])

    df.sort_values(by="month")

    st.bar_chart(
        data=df.set_index('month_name')['total'],
        use_container_width=True
    )

    df["total"] = df["total"].map("{:,.2f}".format)

    df_reset=df.reset_index(drop=True)
    df_reset.index+=1

    st.table(df_reset[["month_name","total"]])
