from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import time

class com_module():
    def login(self, browser):
        #browser.maximize_window()
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[2]/div/div/span/input").send_keys(mail)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/span/input").send_keys(password)
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[5]/button").click()
        element = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "menuLogoHeader")
                )
            )
        time.sleep(5)
        
    def logout(self, browser):
        browser.find_element_by_xpath("html/body/div[1]/div/header/div/div[2]/div/div[2]/div").click()
        time.sleep(3)
        browser.find_element_by_xpath("html/body/div[2]/div/div/ul/li[1]/button").click()
        time.sleep(3)
        browser.quit()