import streamlit as st
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .modeldb import BlogData
from sqlalchemy.orm import load_only

def app():
    engine = create_engine("sqlite:///blog.db", echo=True)
    session = sessionmaker(bind=engine)
    sess = session()

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
    #local_css("style1.css")
    def full_blog(item):
        #st.markdown(f"Category:<h6>%s</h6>" % item.blog_cat,unsafe_allow_html=True)
        st.markdown(item.blog_content, unsafe_allow_html=True)
    results = sess.query(BlogData).all()
    def get_cat(results):
        cat = []
        for item in results:
            if not item.blog_cat in cat:
                cat.append(item.blog_cat)
        return cat
    def get_title(category):
        ti_li = []
        for item in results:
            if item.blog_cat == category:
                if not item.blog_title in ti_li:
                    ti_li.append(item.blog_title)
        return ti_li
    cate = get_cat(results)
    col = st.beta_columns([3,1])
    st.sidebar.markdown("<h4>Blog Category</h4>", unsafe_allow_html=True)
    fil = st.sidebar.radio("label", cate, key="label")
    cat_tit = get_title(fil)
    col[1].markdown("<h4>Blog Title</h4>", unsafe_allow_html=True)
    sel_title = col[1].radio("",cat_tit)

    with col[0]:
        for item in results:
            if item.blog_title==sel_title:
                st.markdown(f"<h2>%s</h2" % item.blog_title, unsafe_allow_html=True)
                st.markdown(f"<p>%s</p>" % item.blog_desc, unsafe_allow_html=True)
                if st.button("Read"):
                    full_blog(item)
