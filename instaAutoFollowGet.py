from instagramUserInfo import username,password #personal information
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time


#service = Service(r"C:\Users\...) 

class Instagram:
    def __init__(self,username,password):
        self.browser=webdriver.Firefox()
        self.username=username
        self.password=password

        #sign f(x)
    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")

        time.sleep(2)
        usernameInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        passwordInput=self.browser.find_element(By.XPATH,'//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)
        passkey=self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div/div')
        passkey.click()
        time.sleep(2)
        #followers f(x)
    def getFollowers(self):
            self.browser.get(f"https://www.instagram.com/{self.username}")
            time.sleep(3)
            # Find the followers link and click it
            followers=self.browser.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[2]/div/a')
            followers.click()
        

            time.sleep(5)

        # Locate the opened followers window
            dialog = self.browser.find_element(By.XPATH,"/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]")
            new_height=len(dialog.find_elements(By.CSS_SELECTOR, "a[role='link']"))
            print(f"Initial number of followers: {new_height}")

            action = webdriver.ActionChains(self.browser)
            last_height = 0
            while True:
                action.send_keys(Keys.END).perform()
                time.sleep(2)
                new_height = len(dialog.find_elements(By.CSS_SELECTOR, "a[role='link']"))
                if new_height == last_height:
                    break
                last_height = new_height

            print(f"Total number of followers: {last_height}")

            followers = dialog.find_elements(By.CSS_SELECTOR, "a[role='link']")
            for user in followers:
                print(user.get_attribute("href"))



instgrm=Instagram(username,password)


instgrm.signIn()

instgrm.getFollowers()






