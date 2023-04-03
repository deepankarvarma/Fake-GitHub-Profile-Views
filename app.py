import streamlit as st
import webbrowser

def open_in_new_window(url):
    webbrowser.open_new(url)

st.title("Open URL in New Window")
url = st.text_input("Enter a URL:")
if st.button("Open in New Window"):
    open_in_new_window(url)
