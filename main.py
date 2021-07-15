import streamlit as st
from apps import model, home, nirf, iit
from PIL import Image
image = Image.open('data/Boddu_Venkatesh1.jpg')

st.set_page_config(page_title = "Aspiring Data Scientist",page_icon = image,layout="wide")
model.hide_menu()
app = model.MultiPage()
app.add_page("Home", home.app)
app.add_page("NIRF Analytics",nirf.app)
app.add_page("IIT Seat Prediction",iit.app)
app.run()
style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """
st.markdown(style, unsafe_allow_html=True)
#ft = model.CustomFooter()
#ft.add_text("Linkedin",h_link="https://www.linkedin.com/in/bvenkatesh-ai/")
#ft.add_text("Github",h_link="https://github.com/bvenkatesh-ai")
#ft.generate_footer()
