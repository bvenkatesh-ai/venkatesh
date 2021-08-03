import streamlit as st
import base64
from io import BytesIO
import os
import streamlit.components.v1 as components

def cv():
    with open("data/cv.pdf","rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
        pdf_display = f"""<embed src="data:application/pdf;base64,{base64_pdf}" width="600" height="800" type="application/pdf">"""
        st.markdown(pdf_display, unsafe_allow_html=True)
def local_html(file_name):
    with open(file_name) as f:
        #st.markdown(f.read(), unsafe_allow_html=True)
        components.html(f"{f.read()}",height=800)
def app():
    local_html('skills.html')
