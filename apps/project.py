import streamlit as st
from . import nirf, iit, pcm, model
def app():
    st.markdown("<h2 color='red'>Projects</h2>",unsafe_allow_html=True)
    project_app = model.MultiMenu()
    project_app.add_page("NIRF Analytics",nirf.app)
    project_app.add_page("JEE Seat Prediction",iit.app)
    project_app.add_page("PCM",pcm.app)
    project_app.run()
