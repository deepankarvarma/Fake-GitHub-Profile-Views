import streamlit as st
from selenium import webdriver
import time

# Define the Streamlit app
def app():
    # Set the URL to be reloaded
    url = st.text_input("Enter the URL to reload:")

    # Set the number of times to reload the URL
    n = st.number_input("Enter the number of profile views:", min_value=1, step=1)

    # Set up the webdriver
    driver = webdriver.Chrome()  # Replace with the appropriate webdriver for your browser

    # Load the URL in the browser
    driver.get(url)

    # Loop through the reloads
    for i in range(n):
        # Reload the page
        driver.refresh()

        # Wait for the page to fully load
        time.sleep(1)  # Change the number of seconds as needed

        # Print the title of the page
        st.write(f"Reload {i+1}: Page Title - {driver.title}")

    # Close the browser
    driver.quit()

# Run the Streamlit app
if __name__ == "__main__":
    app()
