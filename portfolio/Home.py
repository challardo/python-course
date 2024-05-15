import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images/photo.png")

with column2:
    st.title("here goes the name")
    content = """ some large text
    with a lot of content as a small description of you
    """

    st.write(content)

st.write("Below you can find some python apps.")


col3, col4 = st.columns(2, gap="small")
proyects = pd.read_csv("data.csv", sep=";")

with col3:
    for IndexError, proyect in proyects[:10].iterrows():
        st.header(proyect["title"])
        st.write(proyect["description"])
        st.image("images/" + proyect["image"])
        st.write(f"[Source Code]({proyect['url']})")

with col4:
    for IndexError, proyect in proyects[10:].iterrows():
        st.header(proyect["title"])
        st.write(proyect["description"])
        st.image("images/" + proyect["image"])
        st.write(f"[Source Code]({proyect['url']})")
