import streamlit as st

def hide_menu(hamburger_menu=False):
    hide_hamburger = """
    	<style>
    	/* This is to hide hamburger menu completely */
    	#MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
    	</style>
        """
    if not hamburger_menu:
        st.markdown(hide_hamburger, unsafe_allow_html=True)


class MultiPage:
    """
    This class is useful for the creation of multipage app with menu
    """
    def __init__(self,menu_type='button',menu_location='body'):
        self.pages = []
        self.menu_type = menu_type
        self.menu_location = menu_location

    def add_page(self, title, task):
            self.pages.append({
            "title": title,
            "function": task
        })

    def run(self):
        # app = st.sidebar.radio(
        if self.menu_location == 'body' and self.menu_type == 'button':
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
        if self.menu_location == 'sidebar' and self.menu_type == 'button':
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
        if self.menu_location == 'sidebar' and self.menu_type == 'radio':
            st.sidebar.markdown("## Menu")
            page = st.sidebar.radio(
            '',
            self.pages,
            format_func=lambda page: page['title'])
            page['function']()
        if self.menu_location == 'body' and self.menu_type == 'radio':
            page = st.radio(
            'Menu',
            self.pages,
            format_func=lambda page: page['title'])
            page['function']()
        if self.menu_location == 'sidebar' and self.menu_type == 'dropdown':
            page = st.sidebar.selectbox(
            'Menu',
            self.pages,
            format_func=lambda page: page['title'])
            page['function']()
        if self.menu_location == 'body' and self.menu_type == 'dropdown':
            page = st.selectbox(
            'Menu',
            self.pages,
            format_func=lambda page: page['title'])
            page['function']()


class MultiMenu:
    """
    This class is useful for the creation of multimenu app with menu
    """
    def __init__(self):
        self.menu = []

    def add_page(self, title, task):
            self.menu.append({
            "title": title,
            "function": task
        })
    #def cur_page(self):
    #    self.cpage=0
    def run(self):
        # app = st.sidebar.radio(
        tot_pages = len(self.menu)
        cols = st.beta_columns(tot_pages)
        but_values = [cols[i].button(self.menu[i]['title'],key=self.menu[i]['title']) for i in range(tot_pages)]
        if "cmenu" not in st.session_state:
            st.session_state.cmenu=0
        if True in but_values:
            st.session_state.cmenu=but_values.index(True)
        #st.markdown("---",unsafe_allow_html=True)
        self.menu[st.session_state.cmenu]['function']()
        return self.menu[st.session_state.cmenu]['title']
