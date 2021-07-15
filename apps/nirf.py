import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache
def load_data():
    data = pd.read_csv("data/nirf_2020.csv")
    data = data.drop(['Institute ID'],axis=1)
    return data

def app():
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    sel = st.radio("",("About Project","Explore Project"))
    if sel =="About Project":
        about_nirf="""
         The National Institutional Ranking Framework (NIRF) launched
         by Honourable Minister of Human Resource Development in 2019 to rank
         institutions across the country.<br>
         Data collected using pandas library from <a href="https://www.nirfindia.org/">NIRF website</a>
         Analysis of of variour factors making the institutions better than others.
         """
        st.markdown(about_nirf,unsafe_allow_html=True)
    if sel == "Explore Project":
        df = load_data()
        sel_cat=st.selectbox('Category',df['Category'].unique())
        df = df.query('Category==@sel_cat')
        df = df.drop(['Category'],axis=1)
        options = ["Top 10 institutions","Top 10 in state","City","Compare colleges","colleges"]
        sel = st.radio("",options)
        if sel==options[0]:
            st.table(df.head(10))
        if sel == options[1]:
            s=st.sidebar.selectbox("state",df['State'].unique())
            st.table(df[df['State']==s])
        if sel== options[2]:
            c=st.sidebar.selectbox("City",df['City'].unique())
            st.table(df[df['City']==c])
        if sel == options[3]:
            com=st.multiselect("Select Institutes",df['Name'].unique())
            if com:
                st.table(df[df['Name'].isin(com)])
            df_com=df[df['Name'].isin(com)]
        st_count=df["State"].value_counts()
        if sel==options[4]:
            st.bar_chart(st_count)
