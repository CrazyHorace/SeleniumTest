from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import *
import com_module
import time


class TestClass:
    def test1_Login(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.maximize_window()
        com_module.com_module().login(browser)
        com_module.com_module().logout(browser)
        print("PASS! Login/Logout")
        
    def test2_T02_004_account_lock(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[2]/div/div/span/input").send_keys(mail2)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/span/input").send_keys("111")
        time.sleep(1)
        for i in range(4, 0, -1):
            browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[5]/button").click()
            time.sleep(5)
        password_err_msg = browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/div").text
        assert password_err_msg == "For security, we had lock your account!"
        print(password_err_msg)
        browser.quit()
        
    def test3_T02_008_auto_logout(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        now_url = browser.current_url
        print("-----Url before login:-----")
        print(now_url)
        browser.maximize_window()
        com_module.com_module().login(browser)
        print("And login page Logo is presnet")
        now_url = browser.current_url
        print("-----Url after login:-----")
        print(now_url)
        browser.close()
        
        browser = webdriver.Chrome()
        browser.get(WiSVM_User_List)
        print("-----Url after relaunch browser:-----")
        now_url = browser.current_url
        print(now_url)
        assert now_url == WiSVM
        print("No auto login!PASS!")
        browser.quit()
        
    #使用者列表-搜詢 
    def test4_T02_021_search(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        #browser.maximize_window()
        com_module.com_module().login(browser)
        time.sleep(5)
        
        browser.find_element_by_xpath("html/body/div/div/article/aside/div[2]/div[2]/h3").click()
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/article/aside/div[2]/div[2]/div/div/button[1]").click()
        time.sleep(1)
        
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/input").send_keys("test")
        time.sleep(2)
        browser.find_element_by_xpath("//*[@id='userListPage']/div[3]/div[1]/span/span/button").click()
        time.sleep(5)
        #判斷蒐詢內容
        Search_list = browser.find_elements_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr/td[1]")
        total = 0
        for i in range(len(Search_list)):
            i = i+1
            result = browser.find_element_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr["+str(i)+"]/td[1]").text
            result = result.lower()
            assert "test" in result
            total = total + 1
        print("Pass! Search result all contain 'test'!\nTotal search items are:"+str(total))
        
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/input").clear()
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/input").send_keys("Horace")
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/span/button").click()
        time.sleep(5)
        Search_list = browser.find_elements_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr")
        total = 0
        for i in range(len(Search_list)):
            i = i+1
            result = browser.find_element_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr["+str(i)+"]/td[1]").text
            result = result.lower()
            assert "horace" in result
            total = total + 1
        print("Pass! Search result all contain 'horace'!\nTotal search items are:"+str(total))
        
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/input").clear()
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[1]/span/input").send_keys("t")
        browser.find_element_by_xpath("//*[@id='userListPage']/div[3]/div[1]/span/span/button/span").click()
        time.sleep(5)
        Search_Page = browser.find_elements_by_xpath('//*[@id="userListPage"]/div[4]/div/div/ul/li')
        total = 0
        for a in range(2, len(Search_Page), 1):
            browser.find_element_by_xpath('//*[@id="userListPage"]/div[4]/div/div/ul/li['+str(a)+']').click()
            time.sleep(3)
            Search_list = browser.find_elements_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr")
            for i in range(len(Search_list)):
                i = i+1
                result = browser.find_element_by_xpath("//*[@id='userListPage']/div[4]/div/div/div/div/div/table/tbody/tr["+str(i)+"]/td[1]").text
                result = result.lower()
                assert "t" in result
                total = total + 1
        print("PASS! Search result all contain 't'!\nTotal search items are:"+str(total))
        browser.quit()

    def test5_T02_010_011_change_phone(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.maximize_window()
        com_module.com_module().login(browser)
        
        #檢查電話錯誤訊息
        browser.find_element_by_xpath("html/body/div/div/header/div/div[2]/div/div[1]/a").click()
        time.sleep(1)
        browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[2]/div[2]/div[2]/div[2]").click()
        time.sleep(3)
        browser.find_element_by_xpath("//*[@id='profilePhone']").clear()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='profilePhone']").send_keys("a")
        time.sleep(1)
        phone_error = browser.find_element_by_xpath("//*[@class='ant-form-explain']").text
        assert phone_error == "The input is not valid Phone"
        print("PASS! The input is not valid Phone.")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='profilePhone']").send_keys(Keys.BACK_SPACE)
        phone_error = browser.find_element_by_xpath("//*[@class='ant-form-explain']").text
        assert phone_error == "Field can not be empty."
        print("PASS! Field can not be empty.")
        time.sleep(1)
        
        browser.find_element_by_xpath("//*[@id='profilePhone']").clear()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='profilePhone']").send_keys("12345678901234567890")
        time.sleep(1)
        browser.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[1]/div/div[2]/div[3]/div/div/div/button[2]/span").click()
        time.sleep(5)
        browser.quit()
            
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.maximize_window()
        com_module.com_module().login(browser)
        browser.find_element_by_xpath("html/body/div/div/header/div/div[2]/div/div[1]/a").click()
        time.sleep(5)
        phone_input_vlaue = browser.find_element_by_xpath("html/body/div[1]/div/article/section/div/div[3]/div[2]/div[2]/div[2]/div[1]").text#get_attribute("value")
        time.sleep(1)

        assert phone_input_vlaue == "12345678901234567890"
        print("PASS! Phone number is saved and correct")
        time.sleep(1)
        browser.quit()
        
    def test6_T02_012_013_014_change_password(self):
        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.maximize_window()
        com_module.com_module().login(browser)
        browser.find_element_by_xpath("html/body/div/div/header/div/div[2]/div/div[1]/a").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='userProfilePage']/div[3]/div[2]/div[4]/div[2]/div[2]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='oldPassword']").send_keys("123")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@id='confirm']").send_keys("1234567")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(5)
        password_er_msg = browser.find_element_by_xpath("//*[@class='danger svm-TS']").text
        assert password_er_msg == "Password Error"
        print(password_er_msg)

        browser.find_element_by_xpath("//*[@type='button']").click()#click cancel button
        time.sleep(3)


        browser.find_element_by_xpath("//*[@id='userProfilePage']/div[3]/div[2]/div[4]/div[2]/div[2]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='oldPassword']").send_keys("123456")
        browser.find_element_by_xpath("//*[@id='password']").send_keys("1234")
        browser.find_element_by_xpath("//*[@id='confirm']").send_keys("1234567")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(1)
        password_er_msg = browser.find_element_by_xpath("//*[@class='ant-form-explain']").text
        assert password_er_msg == "Two passwords that you enter is inconsistent!"
        print(password_er_msg)
        browser.find_element_by_xpath("//*[@type='button']").click()#click cancel button
        time.sleep(3)

        browser.find_element_by_xpath("//*[@id='userProfilePage']/div[3]/div[2]/div[4]/div[2]/div[2]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='oldPassword']").send_keys("123456")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@id='password']").send_keys("1234567")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@id='confirm']").send_keys("1234567")
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(5)
        password_chg_msg = browser.find_element_by_xpath("//*[@class='svm-TS']").text
        print(password_chg_msg)
        assert password_chg_msg == "Change Password Success"
        browser.find_element_by_xpath("//*[@type='button']").click()
        time.sleep(5)
        browser.quit()

        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[2]/div/div/span/input").send_keys(mail)
        #time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/span/input").send_keys(password)
        #time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[5]/button").click()
        time.sleep(5)
        password_er_msg = browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/div").text
        print("PASS!" + password_er_msg)
        #time.sleep(3)
        browser.quit()

        browser = webdriver.Chrome()
        browser.get(WiSVM)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[2]/div/div/span/input").send_keys(mail)
        #time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[3]/div/div/span/input").send_keys("1234567")
        #time.sleep(1)
        browser.find_element_by_xpath("html/body/div/div/div[3]/form/div[5]/button").click()
        WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, "menuLogoHeader")
                )
            )
        time.sleep(5)
        now_url = browser.current_url
        assert now_url == WiSVM_Dashboard
        print("PASS! Login success!!")

        browser.find_element_by_xpath("html/body/div/div/header/div/div[2]/div/div[1]/a").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='userProfilePage']/div[3]/div[2]/div[4]/div[2]/div[2]").click()
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='oldPassword']").send_keys("1234567")
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='password']").send_keys(password)
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@id='confirm']").send_keys(password)
        #time.sleep(1)
        browser.find_element_by_xpath("//*[@type='submit']").click()
        time.sleep(5)
        password_chg_msg = browser.find_element_by_xpath("//*[@class='svm-TS']").text
        assert password_chg_msg == "Change Password Success"
        print("PASS! Change back to original password")

        #time.sleep(3)
        browser.quit()