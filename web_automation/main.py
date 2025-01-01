from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

# Replace these with your credentials and file URL
FIGMA_EMAIL = "saifhussainansari6@gmail.com"
FIGMA_PASSWORD = "pQG&UEv;95ZbiG6"
FIGMA_FILE_URL = "https://www.figma.com/file/IFZdbkck0VDYqYeS6fRbNy"

def automate_locofyai():
    # Initialize WebDriver
    driver = webdriver.Chrome()  # Replace with your preferred WebDriver
    driver.maximize_window()

    try:
        # Step 1: Open Figma and Log In
        driver.get("https://www.figma.com/login")
        time.sleep(5)

        # Enter email
        email_field = driver.find_element(By.ID, "email")
        email_field.send_keys(FIGMA_EMAIL)

        # Enter password
        password_field = driver.find_element(By.ID, "current-password")
        password_field.send_keys(FIGMA_PASSWORD)
        password_field.send_keys(Keys.RETURN)
        time.sleep(10)  # Wait for login to complete

        # Step 2: Open Figma File
        driver.get(FIGMA_FILE_URL)
        time.sleep(10)  # Wait for the file to load

        # Step 3: Open the Locofy.ai Plugin
        # Simulate pressing `Alt` + `/` to open the plugin search
        ActionChains(driver).key_down(Keys.COMMAND).send_keys("/").key_up(Keys.COMMAND).perform()
        time.sleep(2)

        # Search for Locofy.ai
        search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys("Locofy.ai")
        time.sleep(2)

        # Select Locofy.ai plugin
        ActionChains(driver).key_down(Keys.COMMAND).send_keys("/").key_up(Keys.COMMAND).perform()
        time.sleep(2)
        # Select Locofy.ai plugin
        driver.execute_script('document.querySelector("#react-page > div > div > div > div.fullscreen_view--flexContainer--SBt2E > div:nth-child(1) > div > div > div.utils-module--contents--iP8Hi > div > div > div > div > div > div > div > div.cx_pl8--gxoGN.cx_pr8--CsQT3.cx_pb8--v4HS8 > div > div > fieldset > button:nth-child(3) > div > div.tabs--tabButton--QIg8n > label > i18n-text").click()')

        time.sleep(2)

        # Search for Locofy.ai
        search_field = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys("Locofy.ai")
        time.sleep(2)

        plugin_option = driver.find_element(By.XPATH, "//div[text()='Locofy Lightning - Figma to Code in a flash']")
        plugin_option.click()
        time.sleep(5)  # Wait for the plugin to load

        # here code will updated
        search_field.send_keys(Keys.RETURN)
        driver.execute_script('document.querySelector("body > div:nth-child(1) > div._login_1telm_1 > div._btnContainer_1telm_80 > div > button")')
        time.sleep(10)  # Wait for the plugin to load

        # Step 5: Download the Code
        # Locate the download link or interact with the UI to retrieve the code.
        # Example:
        download_button = driver.find_element(By.XPATH, "//a[text()='Download Code']")
        download_button.click()
        time.sleep(5)  # Wait for the download

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    automate_locofyai()
