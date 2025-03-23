import streamlit as st
import pathlib
from main import scrape_website


# function to load css from the assets folder
def load_css(file_path):
    with open(file_path) as f:
        st.html(f"<style>{f.read()}</style>")
        # Load the external CSS
    css_path = pathlib.Path("assets/style.css")
    if css_path.exists():
        load_css(css_path)
    st.title("AI Scraper")
    st.markdown(
        "Enter a website URL to scrape, clean the text content, and display the result in smaller chunks."
    )
    url = st.text_input(label= "", placeholder="Enter the URL of the website you want to scrape")
    if st.button("Scrape", key="scrape_button"):
        st.write("scraping the website…")
        result = scrape_website(url)
        st.write("Scraping complete.")
        st.write(result)
