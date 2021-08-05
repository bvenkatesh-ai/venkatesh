import streamlit as st
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///blog.db", echo=True)
Base = declarative_base()

class BlogData(Base):
    __tablename__ = "blogdata"
    blog_id = Column(Integer, primary_key=True)
    blog_title = Column(String)
    blog_desc = Column(Text)
    blog_content = Column(Text)
    blog_cat = Column(String)
    #blog_post_date = Column(Date)

Base.metadata.create_all(engine)
