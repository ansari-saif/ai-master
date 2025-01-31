import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def automate_locofyai():
    try:
        load_dotenv()

        driver = webdriver.Chrome()
        driver.maximize_window()

        driver.get("https://www.figma.com/login")
        time.sleep(5)
        
        LOCOFY_EMAIL = os.getenv('LOCOFY_EMAIL')
        LOCOFY_PASSWORD = os.getenv('LOCOFY_PASSWORD')
        
        
        FIGMA_EMAIL = os.getenv('FIGMA_EMAIL')
        FIGMA_PASSWORD = os.getenv('FIGMA_PASSWORD')
        
        FIGMA_FILE_URL = os.getenv('FIGMA_FILE_URL')

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
        time.sleep(20)

        iframe = driver.find_element(By.ID, 'plugin-iframe-in-modal')  
        driver.switch_to.frame(iframe)

        f1 = driver.find_element(By.NAME, "Network Plugin Iframe")
        driver.switch_to.frame(f1)
        
        # Switch to the inner iframe
        inner0_iframe = driver.find_element(By.ID, "plugin-iframe")
        driver.switch_to.frame(inner0_iframe)
        driver.execute_script('document.querySelector("._btn_1telm_80").click()')
        time.sleep(1)
        
        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)

        # Retrieve Locofy credentials from environment variables
        # Login to locofy

        # Locate the email and password fields within the iframe
        email_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/input')
        password_field = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[2]/input')

        # Enter the credentials
        email_field.send_keys(LOCOFY_EMAIL)
        password_field.send_keys(LOCOFY_PASSWORD)

        # Click the login button
        login_button = driver.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/button')
        login_button.click()

        # use google login instead
        # Wait for the login to complete
        time.sleep(10)
        driver.switch_to.window(driver.window_handles[0])
        # gen code button
        iframe = driver.find_element(By.ID, 'plugin-iframe-in-modal')
        driver.switch_to.frame(iframe)

        f1 = driver.find_element(By.NAME, "Network Plugin Iframe")
        driver.switch_to.frame(f1)
        time.sleep(5)
        # Switch to the inner iframe
        inner0_iframe = driver.find_element(By.ID, "plugin-iframe")
        time.sleep(2)
        driver.switch_to.frame(inner0_iframe)
        time.sleep(2)
        try:
            driver.execute_script('document.querySelectorAll(".font-medium")[1].click()')
            time.sleep(1)
        except Exception as e:
            print(e)
        driver.execute_script('document.querySelector("._shinyBtn_1lwba_6").click()')
        time.sleep(1)

        # select frame 1
        driver.execute_script('document.querySelector("._frameImage_1ip34_91").click()')
        time.sleep(2)
        # click to convert 1 frame _shinyBtn_1lwba_6
        driver.execute_script('document.querySelector("._shinyBtn_1lwba_6").click()')
        time.sleep(1)
        # sleep 60 seconds
        time.sleep(30)
        def wait_element(xpath, timeout=10):
            return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))

        wait_element('//*[@id="root-preview"]/div[1]/div[3]/div[5]/button').click()
        wait_element('//*[@id="portal"]/div[6]/div[2]/div/div/div[2]/div[1]/span/span/div/div').click()
        wait_element('//*[@id="portal"]/div[6]/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
        wait_element('//*[@id="portal"]/div[6]/div[2]/div/div[3]/div/div/span/span/button').click()
        time.sleep(5)
        wait_element('//*[@id="portal"]/div[6]/div[2]/div[2]/div[2]/button').click()
        driver.switch_to.window(driver.window_handles[2])
        wait_element('//*[@id="app"]/div[2]/div/div[3]/button[1]').click()
        try:
            wait_element('//*[@id="portal"]/div[20]/div/div[2]/div/div/img[3]').click()
            time.sleep(1)
        except Exception as e:
            print(e)
        wait_element('//*[@id="header"]/div[3]/div/div/button').click()
        wait_element('//*[@id="portal"]/div[21]/div/div[3]/div[3]').click()
        wait_element('//*[@id="portal"]/div[22]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div/button').click()


    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    automate_locofyai()
