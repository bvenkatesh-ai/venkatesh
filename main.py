import streamlit as st
from apps import model, home, project, blog
from PIL import Image
image = Image.open('data/Boddu_Venkatesh1.jpg')

st.set_page_config(page_title = "Aspiring Data Scientist",page_icon = image,layout="wide")
model.hide_menu()
app = model.MultiPage('radio','sidebar')
app.add_page("Home", home.app)
app.add_page("Projects",project.app)
app.add_page("Blog", blog.app)


app.run()
