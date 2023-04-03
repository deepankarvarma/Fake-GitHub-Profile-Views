import streamlit as st
from selenium import webdriver
import time

# Define a function to reload the given URL for the specified number of times
def reload_url(url, num_views):
    # Set up the webdriver in headless mode
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    # Load the URL in the browser
    driver.get(url)

    # Loop through the reloads
    for i in range(num_views):
        # Reload the page
        driver.refresh()

        # Wait for the page to fully load
        time.sleep(0.2)  # Change the number of seconds as needed

        # Print the title of the page
        st.write(f"Reload {i+1}: Page Title - {driver.title}")

    # Close the browser
    driver.quit()

# Set up the streamlit app
st.title("Reload a Webpage")
url = st.text_input("Enter the URL:")
num_views = st.number_input("Enter the number of views:", value=1, min_value=1, max_value=1000, step=1)

if st.button("Submit"):
    reload_url(url, num_views)
