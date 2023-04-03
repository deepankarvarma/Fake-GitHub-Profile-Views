from selenium import webdriver
import time

# Set the URL to be reloaded
url = "https://github.com/deepankarvarma"

# Set the number of times to reload the URL
n=int(input("Enter the number of profile views"))

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
    print(f"Reload {i+1}: Page Title - {driver.title}")

# Close the browser
driver.quit()
