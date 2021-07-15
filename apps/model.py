import streamlit as st

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

