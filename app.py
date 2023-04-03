import streamlit as st
from selenium import webdriver
import time

# Define a function to handle the page reloads
def reload_page(url, n):
    # Set up the webdriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Load the URL in the browser
    driver.get(url)

    # Loop through the reloads
    for i in range(n):
        try:
            # Reload the page
            driver.refresh()

            # Wait for the page to fully load
            time.sleep(0.2)  # Change the number of seconds as needed

            # Print the title of the page
            st.write(f"Reload {i+1}: Page Title - {driver.title}")
        except:
            st.write(f"An error occurred while reloading page {i+1}. Skipping...")

    # Close the browser
    driver.quit()

# Set the title of the Streamlit app
st.title("GitHub Profile Views")

# Add a text input for the URL
# url = st.text_input("Enter the URL to be reloaded")

# Add a number input for the number of reloads
n = st.number_input("Enter the number of reloads", min_value=1, step=1)

# Add a submit button to start the reloads
if st.button("Reload"):
    if not url:
        st.warning("Please enter a valid URL.")
    else:
        try:
            reload_page(url, n)
        except:
            st.error("An error occurred while processing the page reloads. Please try again.")
