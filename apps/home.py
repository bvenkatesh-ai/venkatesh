import streamlit as st
import base64
from io import BytesIO
import os
def app():
    st.header("Venkatesh Boddu")
    st.write("CV uploaded soon")
    cv="Not done"
    if cv=="done":
        with open("data/cv.pdf","rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode('utf-8')
            pdf_display = f"""<embed src="data:application/pdf;base64,{base64_pdf}" width="600" height="800" type="application/pdf">"""
            st.markdown(pdf_display, unsafe_allow_html=True)
