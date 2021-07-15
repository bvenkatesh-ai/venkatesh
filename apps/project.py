import streamlit as st
import nirf, iit
def app():
    st.markdown("<h2 color='red'>Projects</h2>")
    sel = st.radio("",["Nirf Analytics", "IIT seat predictor"])
    if sel == "Nirf Analytics":
        nirf.app()
    if sel == "IIT seat predictor":
        iit.app()
