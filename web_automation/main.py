import os
import traceback
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
def wait_element(driver, by, value, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))

def wait_for_script(driver, script, retries=10):
    def run_script(count=0):
        try:
            print(script)
            driver.execute_script(script)
        except Exception as e:
            if count < retries:
                time.sleep(0.5)
                run_script(count + 1)
            else:
                raise Exception(e)
    run_script()
def automate_locofyai():
    try:
        load_dotenv()
        options = webdriver.ChromeOptions()
        download_path = os.path.join(os.getcwd(), "downloads")
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        prefs = {"download.default_directory": download_path}
        options.add_experimental_option("prefs", prefs)
        
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://www.figma.com/login")


        LOCOFY_EMAIL = os.getenv('LOCOFY_EMAIL')
        LOCOFY_PASSWORD = os.getenv('LOCOFY_PASSWORD')


        FIGMA_EMAIL = os.getenv('FIGMA_EMAIL')
        FIGMA_PASSWORD = os.getenv('FIGMA_PASSWORD')

        FIGMA_FILE_URL = os.getenv('FIGMA_FILE_URL')

        # Enter email
        email_field = wait_element(driver, By.ID, "email")
        email_field.send_keys(FIGMA_EMAIL)
        email_field.send_keys(Keys.RETURN)

        # Enter password
        password_field = wait_element(driver, By.ID, "current-password")
        password_field.send_keys(FIGMA_PASSWORD)
        password_field.send_keys(Keys.RETURN)

        wait_element(driver, By.CLASS_NAME,'tab_group--tabSelectorOverrides--misNs')

        # Step 2: Open Figma File
        driver.get(FIGMA_FILE_URL)
        # check element with text "Search"
        wait_element(driver, By.CLASS_NAME,'gpu-view-content')
        time.sleep(2)
        # Step 3: Open the Locofy.ai Plugin
        # Simulate pressing `Alt` + `/` to open the plugin search
        ActionChains(driver).key_down(Keys.COMMAND).send_keys("/").key_up(Keys.COMMAND).perform()
        # Search for Locofy.ai
        search_field = wait_element(driver, By.XPATH, "//input[@placeholder='Search']")
        search_field.send_keys("Locofy.ai")
        time.sleep(1)
        # press enter
        search_field.send_keys(Keys.RETURN)
        time.sleep(1.5)
        # press enter
        search_field.send_keys(Keys.RETURN)


        # click on run button
        wait_for_script(driver, 'document.querySelector("#react-page > div > div > div > div.fullscreen_view--flexContainer--SBt2E > div:nth-child(1) > div > div > div.utils-module--contents--iP8Hi > div > div > div > div > div > div.cx_flex--2hUIC.cx_flexRow--QnXvr.cx_gap8--RCB1-.cx_justifyBetween--ihJXN.cx_pt8--kmTV-.cx_pb8--v4HS8.cx_bSolid--6-DiT.cx_colorBorder--W0gXm.cx_bt1--nb1cc.cx_itemsCenter--4Ybl3.cx_colorBg--XYMUF > div > button.button-reset-module--buttonReset--Njg3k.button-module--button--xiqeQ.utilities--bodyMedium--7-YGK.button-module--regularSize--Mmmf7.button-module--primary--pCfBo.button-module--solidStyle--mSysv").click()') 

        iframe = wait_element(driver, By.ID, "plugin-iframe-in-modal", timeout=30)
        driver.switch_to.frame(iframe)

        f1 = wait_element(driver, By.NAME, "Network Plugin Iframe")
        driver.switch_to.frame(f1)

        # Switch to the inner iframe
        inner0_iframe = wait_element(driver, By.ID, "plugin-iframe")
        driver.switch_to.frame(inner0_iframe)
        time.sleep(0.5)
        wait_for_script(driver, 'document.querySelector("._btn_1telm_80").click()')
        time.sleep(0.5)

        # Switch to the new tab
        driver.switch_to.window(driver.window_handles[1])

        # Retrieve Locofy credentials from environment variables
        # Login to locofy

        # Locate the email and password fields within the iframe
        email_field = wait_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[1]/input')
        password_field = wait_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/div[2]/input')

        # Enter the credentials
        email_field.send_keys(LOCOFY_EMAIL)
        password_field.send_keys(LOCOFY_PASSWORD)

        # Click the login button
        login_button = wait_element(driver, By.XPATH, '//*[@id="app"]/div/div/div/div/div/div[2]/button')
        login_button.click()

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        # gen code button
        iframe = wait_element(driver, By.ID, 'plugin-iframe-in-modal')
        driver.switch_to.frame(iframe)

        f1 = wait_element(driver, By.NAME, "Network Plugin Iframe")
        driver.switch_to.frame(f1)

        # Switch to the inner iframe
        inner0_iframe = wait_element(driver, By.ID, "plugin-iframe")
        driver.switch_to.frame(inner0_iframe)
        time.sleep(2)

        wait_for_script(driver, 'document.querySelectorAll(".font-medium")[1].click()')
        time.sleep(2)
        wait_for_script(driver, 'document.querySelector("._shinyBtn_1lwba_6").click()')
        time.sleep(2)
        # select frame 1
        wait_for_script(driver, 'document.querySelector("._frameImage_1ip34_91").click()')
        time.sleep(2)
        # click to convert 1 frame _shinyBtn_1lwba_6
        wait_for_script(driver, 'document.querySelector("._shinyBtn_1lwba_6").click()')
        time.sleep(2)
        # sleep 60 seconds
        time.sleep(10)
        wait_element(driver, By.XPATH, '//*[@id="root-preview"]/div[1]/div[3]/div[5]/button',timeout=50).click()
        wait_element(driver, By.XPATH, '//*[@id="portal"]/div[6]/div[2]/div/div/div[2]/div[1]/span/span/div/div').click()
        time.sleep(1)
        wait_element(driver, By.XPATH, '//*[@id="portal"]/div[6]/div[2]/div/div[2]/div/div[2]/div/div[1]').click()
        wait_element(driver, By.XPATH, '//*[@id="portal"]/div[6]/div[2]/div/div[3]/div/div/span/span/button').click()
        wait_element(driver, By.XPATH, '//*[@id="portal"]/div[6]/div[2]/div[2]/div[2]/button').click()
        driver.switch_to.window(driver.window_handles[2])
        time.sleep(1)
        wait_element(driver, By.XPATH, '//*[@id="app"]/div[2]/div/div[3]/button[1]').click()
        time.sleep(1)

        try:
            wait_element(driver, By.XPATH, '/html/body/div[2]/div[20]/div/div[2]/div/div/img[3]',timeout=5).click()   
            time.sleep(1)
        except Exception as e:
            print("Error in click on image x trying again ...")
            print(e)
            try:
                wait_element(driver, By.XPATH, '//*[@id="portal"]/div[19]/div/div[2]/div/div/img[3]',timeout=5).click()
                time.sleep(1)
                print('now successfully clicked on image x')
            except Exception as e:
                print("Error in click on image x")
                print(e)
        
        wait_element(driver, By.XPATH, '//*[@id="header"]/div[3]/div/div/button').click()
        time.sleep(1)
        wait_element(driver,By.XPATH, "//div[text()='Export Project']").click()
        time.sleep(1)
        wait_element(driver, By.XPATH, '//*[@id="portal"]/div[22]/div/div[2]/div/div/div[2]/div[3]/div[2]/div/div/div/button').click()
        time.sleep(2)
        os.system('python configure-frontend.py')
        
    except Exception as e:
        print("Error in automate_locofyai")
        print(traceback.format_exc())
        print(e)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    automate_locofyai()
