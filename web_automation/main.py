from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Replace these with your credentials and file URL

# TODO: RESET THIS
FIGMA_EMAIL = "saifhussainansari6@gmail.com"
FIGMA_PASSWORD = "pQG&UEv;95ZbiG6"
FIGMA_FILE_URL = "https://www.figma.com/file/IFZdbkck0VDYqYeS6fRbNy"

def automate_locofyai():
    # Initialize WebDriver
    driver = webdriver.Chrome()  
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
        
        # press enter
        driver.execute_script('document.querySelector("#react-page > div > div > div > div.fullscreen_view--flexContainer--SBt2E > div:nth-child(1) > div > div > div.utils-module--contents--iP8Hi > div > div > div > div > div > div > div > div.cx_pl8--gxoGN.cx_pr8--CsQT3.cx_pb8--v4HS8 > div > div > fieldset > button:nth-child(3) > div > div.tabs--tabButton--QIg8n > label > i18n-text").click()')
        time.sleep(2)

        # Search for Locofy.ai
        
        plugin_option = driver.find_element(By.XPATH, "//div[text()='Locofy Lightning - Figma to Code in a flash']")
        plugin_option.click()
        time.sleep(5)  # Wait for the plugin to load

        # click on run button
        driver.execute_script('document.querySelector("#react-page > div > div > div > div.fullscreen_view--flexContainer--SBt2E > div:nth-child(1) > div > div > div.utils-module--contents--iP8Hi > div > div > div > div > div > div.cx_flex--2hUIC.cx_flexRow--QnXvr.cx_gap8--RCB1-.cx_justifyBetween--ihJXN.cx_pt8--kmTV-.cx_pb8--v4HS8.cx_bSolid--6-DiT.cx_colorBorder--W0gXm.cx_bt1--nb1cc.cx_itemsCenter--4Ybl3.cx_colorBg--XYMUF > div > button.button-reset-module--buttonReset--Njg3k.button-module--button--xiqeQ.utilities--bodyMedium--7-YGK.button-module--regularSize--Mmmf7.button-module--primary--pCfBo.button-module--solidStyle--mSysv").click()')
        time.sleep(10)  # Wait for the plugin to load
        
        iframe = driver.find_element(By.ID, 'plugin-iframe-in-modal')  # Use ID or another suitable locator
        driver.switch_to.frame(iframe)

        f1 = driver.find_element(By.NAME, "Network Plugin Iframe")
        driver.switch_to.frame(f1)
        # Switch to the inner iframe
        inner0_iframe = driver.find_element(By.ID, "plugin-iframe")
        driver.switch_to.frame(inner0_iframe)
        driver.execute_script('document.querySelector("._btn_1telm_80").click()')

        # # Step 5: Download the Code
        # # Locate the download link or interact with the UI to retrieve the code.
        # # Example:
        # download_button = driver.find_element(By.XPATH, "//a[text()='Download Code']")
        # download_button.click()
        # time.sleep(5)  # Wait for the download

    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    automate_locofyai()
