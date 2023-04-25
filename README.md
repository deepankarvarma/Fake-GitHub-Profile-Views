# Fake Github Profile Views
This repository provides a Python script that allows you to simulate profile views on a GitHub profile by repeatedly reloading the profile page.
<br>
### How it works
The script uses the selenium and requests libraries to fetch the content of the profile page and then reloads the page in a headless Firefox browser. The number of reloads is specified by the user and each reload simulates a new view of the profile.<br>
1. The `get_page_content()` function uses the requests library to fetch the content of the URL passed to it as an argument. The content is returned as bytes and can be decoded using the decode() method before passing it to the browser.<br><br>

2. The `reload_page()` function uses the selenium library to launch a headless Firefox browser and load the page content obtained from get_page_content(). The `time.sleep()` method is used to give the page enough time to fully load before the next reload. The driver.title property is used to obtain the title of the page, which includes the name of the GitHub user whose profile is being simulated.<br><br>

3. The Streamlit app allows users to enter the URL of the GitHub profile they want to simulate views for and the number of views they want to simulate. The input fields are created using the `text_input()` and `number_input()` methods respectively. The app also includes a check to ensure that a valid URL is entered before the simulation begins.
<br><br>
4. The script can be further customized to include additional features, such as a delay between each reload or the ability to specify a different browser or driver. It can also be adapted to simulate views on other websites besides GitHub.<br>
<br>
### How to use
1. Clone the repository to your local machine.
2. Install the required libraries by running `pip install -r requirements.txt` in your terminal.<br>
3. Run the script by executing `streamlit run app.py` in your terminal.<br>
4. Enter the URL of the GitHub profile you want to simulate views for in the text input field.<br>
5. Enter the number of views you want to simulate in the number input field.<br>
5. Click the "Reload" button to start simulating the views.<br>
<br>
### Please note that this script is for educational purposes only and should not be used to manipulate or deceive others.
