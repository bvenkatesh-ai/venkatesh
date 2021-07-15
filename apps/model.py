import streamlit as st
from htbuilder import HtmlElement, div, ul, li, br, hr, a, p, img, styles, classes, fonts
from htbuilder.units import percent, px
from htbuilder.funcs import rgba, rgb

def hide_menu(hamburger_menu=False):
    hide_hamburger = """
    	<style>
    	/* This is to hide hamburger menu completely */
    	#MainMenu {visibility: hidden;}
    	</style>
        """
    if not hamburger_menu:
        st.markdown(hide_hamburger, unsafe_allow_html=True)


class MultiPage:
    """
    This class is useful for the creation of multipage app with menu
    """
    def __init__(self):
        self.pages = []

    def add_page(self, title, task):
            self.pages.append({
            "title": title,
            "function": task
        })
    #def cur_page(self):
    #    self.cpage=0
    def run(self):
        # app = st.sidebar.radio(
        tot_pages = len(self.pages)
        cols = st.beta_columns(tot_pages)
        but_values = [cols[i].button(self.pages[i]['title']) for i in range(tot_pages)]
        if "cpage" not in st.session_state:
            st.session_state.cpage=0
        if True in but_values:
            st.session_state.cpage=but_values.index(True)
        #st.markdown("---",unsafe_allow_html=True)
        self.pages[st.session_state.cpage]['function']()
        return self.pages[st.session_state.cpage]['title']

#Footer section
def image(src_as_string, **style):
    return img(src=src_as_string, style=styles(**style))


def link(link, text, **style):
    return a(_href=link, _target="_blank", style=styles(**style))(text)


def layout(*args):

    style = """
    <style>
      # MainMenu {visibility: hidden;}
      footer {visibility: hidden;}
     .stApp { bottom: 105px; }
    </style>
    """

    style_div = styles(
        position="fixed",
        left=0,
        bottom=0,
        margin=px(0, 0, 0, 0),
        width=percent(100),
        color="black",
        text_align="center",
        height="auto",
        opacity=1

    )

    style_hr = styles(
        display="block",
        margin=px(8, 8, "auto", "auto"),
        border_style="inset",
        border_width=px(2)
    )

    body = p()
    foot = div(
        style=style_div
    )(
        #Uncomment below to make a horizontal line
        #hr(style=style_hr),
        body
    )

    st.markdown(style, unsafe_allow_html=True)

    for arg in args:
        if isinstance(arg, str):
            body(arg)

        elif isinstance(arg, HtmlElement):
            body(arg)

    st.markdown(str(foot), unsafe_allow_html=True)

class CustomFooter():
    """
    This class is useful for the creation of footer
    """
    def __init__(self):
        self.items = []
    def add_text(self, text=None, h_link=None):
        if h_link:
            self.items.append(link(h_link,text))
            self.items.append(" ")
        else:
            self.items.append(text)
            self.items.append(" ")
    def add_newline(self):
        self.items.append(br())

    def add_img(self, img_link=None, img_w=25, img_h=25,h_link=None):
        self.items.append(link(h_link, image(img_link, width=px(img_w), height=px(img_h))))
        self.items.append(" ")
    def generate_footer(self):
        layout(*self.items)
