import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("talk")
sns.set_style("darkgrid")
@st.cache
def load_data():
    data = pd.read_csv("data/nirf_2020.csv")
    data = data.drop(['Institute ID'],axis=1)
    return data

def app():
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    sel = st.radio("",("About Project","Statistics","Explore Project"))
    if sel =="About Project":
        about_nirf="""
         The National Institutional Ranking Framework (NIRF) launched
         by Honourable Minister of Human Resource Development in 2019 to rank
         institutions across the country.<br>
         Data collected using pandas library from <a href="https://www.nirfindia.org/">NIRF website</a>
         Analysis of of variour factors making the institutions better than others.
         """
        st.markdown(about_nirf,unsafe_allow_html=True)

    #Load data
    df = load_data()
    # Melt the dataframe
    dfm = df.melt(id_vars=['Name', 'City', 'State','Category','Rank'],var_name="Parameter", value_name="Parameter_score")
    dfm

    #para is sel_state,var is cat
    def plot_count(para,var,tp):
        """This function plot institutes count and score in the selected state"""
        col3,col4 = st.beta_columns(2)
        para_values = ["All"]+list(df[para].unique())
        sel_para = col3.selectbox("",para_values)
        if sel_para =="All":
            df_filter = df
        else:
            df_filter = df[df[para]==sel_para]


        fig1, ax1 = plt.subplots(figsize=tp)
        #if st.button("Show data",key=var):
        #    st.write(df_filter)
        ax1 = sns.countplot(y=var,data=df_filter)
        ax1.set_title("Number of institutes alloted score",fontdict={'fontsize': 18,'color':'red'})
        #col3.markdown("<br>",unsafe_allow_html=True)
        col3.pyplot(fig1)

        fig2, ax2 = plt.subplots(figsize=tp)
        st.write('<style>div.row-widget.stRadio > div{flex-direction:column;}</style>', unsafe_allow_html=True)

        p_type =col4.radio("Graph type",["Bar","Box"],key=var)
        if p_type=="Box":
            ax2 = sns.boxplot(x="Score", y=var, data=df_filter)
            ax2.set_title("Box plot for the institutes",fontdict={'fontsize': 18,'color':'red'})
        else:
            ax2 = sns.barplot(x="Score", y=var, data=df_filter)
            ax2.set_title("Bar plot for the institutes",fontdict={'fontsize': 18,'color':'red'})
        col4.pyplot(fig2)
    if sel == "Statistics":
        st.markdown("<h4>Statistics of the institute scores<h4>",unsafe_allow_html=True)
        with st.beta_expander("State wise"):
            plot_count("State","Category",(4,6))
        with st.beta_expander("Category wise"):
            plot_count("Category","State",(8,14))
        st.markdown("<h4>Factors effecting Score<h4>",unsafe_allow_html=True)
        

    if sel == "Explore Project":

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
