import streamlit as st
import webbrowser

def open_in_new_tab(url):
    webbrowser.open_new_tab(url)

st.set_page_config(page_title="Open URL in New Tab")

st.title("Open URL in New Tab")
url = st.text_input("Enter a URL:")
if st.button("Open in New Tab"):
    open_in_new_tab(url)
