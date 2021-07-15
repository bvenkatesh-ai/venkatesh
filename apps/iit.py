import streamlit as st
import numpy as np
from st_aggrid import AgGrid,DataReturnMode, GridUpdateMode, GridOptionsBuilder
import pandas as pd
import base64
from io import BytesIO

@st.cache
def load_data():
    #load round 6 for the year 2020
    data = pd.read_excel("data/2020.xlsx",sheet_name=5)
    inst = pd.read_excel("data/institutes.xlsx")
    return data, inst

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')
    df.to_excel(writer, index = False, sheet_name='Sheet1',float_format="%.2f")
    writer.save()
    processed_data = output.getvalue()
    b64 = base64.b64encode(processed_data)  # val looks like b'...'
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="Your_File.xlsx">Download Excel file</a>' # decode b'abc' => abc

def app():
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
    sel = st.radio("",("About Project","Explore Project"))
    if sel =="About Project":
        about_iit="""
        The Joint Seat Allocation Authority (JoSAA) 2020 has been
        set up by the Ministry of Education to manage and regulate the joint
        seat allocation for admissions to 110 institutes (23 IITs,  31 NITs,
        IIEST Shibpur, 26 IIITs and 29 Other-Government Funded Technical Institutes
        (Other-GFTIs)).<br>
        Data source: <a href="https://josaa.nic.in/">JOSAA</a><br>
        Retrieving the possible college seat difficult from the website. Here you
        can get the possible seats by entering your details.
                  """
        st.markdown(about_iit,unsafe_allow_html=True)
    if sel == "Explore Project":
        df1, df2 = load_data()
        gen_mapping = {"Male":["Gender-Neutral"],"Female":["Gender-Neutral", "Female-only (including Supernumerary)"]}
        cat_mapping = {"General":["OPEN"],"General-EWS":["OPEN","EWS"],
            "General-PWD":["OPEN","OPEN (PwD)"],"General-EWS-PWD":["OPEN","EWS",
            "OPEN (PwD)","EWS (PwD)"],"OBC-NCL":["OPEN","OBC-NCL"],"OBC-NCL-PWD"
            :["OPEN","OBC-NCL","OBC-NCL-PWD","OBC-NCL-PWD"],"SC":["OPEN","SC"],
            "SC-PWD":["OPEN","OPEN-PWD","SC","SC-PWD"],"ST":["OPEN","SC"],"ST-PWD"
            :["OPEN","OPEN-PWD","ST","ST-PWD"]}
        inst_mapping = {"All":0,"IIT":1,"NIT":2,"IIIT":3,"GFTI":4}
        prog =["All"]+list(df1['AcademicProgramName'].unique())
        with st.form("Rank Input"):
            cols = st.beta_columns(6)
            rank = int(cols[0].number_input("Rank"))
            gender = cols[1].selectbox("Gender",list(gen_mapping.keys()))
            inst_type = cols[4].selectbox("Institute Type",["All","IIT","NIT","IIIT","GFTI"])
            state = cols[2].selectbox("State",(df2['State'].unique()))
            a_p = cols[5].selectbox("Program",prog)
            category = cols[3].selectbox("Category",list(cat_mapping.keys()))
            submitted = st.form_submit_button("Submit")
        if submitted:
            #df_filter = df[df["Gender"].isin(["Gender-Neutral"])]]
            fil1 = gen_mapping[gender]
            fil2 = cat_mapping[category]
            fil3 = list(df2[df2['State']==state]['Institute Name'])
            if inst_type!="All":
                fil4 = list(df2[df2['Institute Code']//100==inst_mapping[inst_type]]['Institute Name'])
            else:
                fil4 = list(df2["Institute Name"].unique())
            if a_p!="All":
                fil5 = a_p
            else:
                fil5 =list(df1['AcademicProgramName'].unique())
            #and (Quota=="AI" or Institute in @fil3)
            df_rank = df1.query('ClosingRank>@rank and Gender in @fil1 and SeatType in @fil2 and Institute in @fil4 and AcademicProgramName in @fil5')
            #st.table(df_rank)
            #utility.st_table(df_rank)
            st.markdown(get_table_download_link(df_rank), unsafe_allow_html=True)

            AgGrid(df_rank)
