
import streamlit as st
import app1
import app2
import app3


PAGES = {
    "View Users & Workers": app1,
    "Remove Users & Workers": app2,
    "Service": app3,
}

html_string1 = "<h2>EXPERTEASE</h2>"
html_string = "<h4>AN EXPERT AT EASE</h4>"

st.sidebar.markdown(html_string1, unsafe_allow_html=True)
st.sidebar.image('4.png')
st.sidebar.markdown(html_string, unsafe_allow_html=True)
selection = st.sidebar.radio("Select: ", list(PAGES.keys()))
page = PAGES[selection]
page.app(selection)
