from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time
#service = Service(r"C:\Users\...) 

#personal information
username=input("Username: ")
password=input("Password: ")

choice=input("1.Get followers\n2.Unfollow\n3.Follow\nMake your choice : ")



class Instagram:
    def __init__(self, username, password):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("intl.accept_languages", "en,en_US")  
        service = Service()  
        self.browser = webdriver.Firefox(service=service, options=firefox_options)
        self.username = username
        self.password = password

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
            followersList=[]
            for user in followers:
                link=user.get_attribute("href")
                followersList.append(link)

            with open("followers.txt","w",encoding="UTF-8") as file:
                for item in followersList:
                     file.write(item+"\n" )
    def followUser(self,usernameT):
            self.browser.get("https://www.instagram.com/"+usernameT)
            time.sleep(2)
            followButton=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div")
            if followButton.text !="Following":
                 followButton.click()
                 time.sleep(2)
            else:
                 print("You are already following them.")
     
    def unFollowUser(self,usernameT):
        self.browser.get("https://www.instagram.com/"+usernameT)
        time.sleep(2)

        followButton=self.browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[1]/div[2]/div/div[1]/button/div/div")
        if followButton.text =="Following":
                followButton.click()
                time.sleep(2)
                confirm = self.browser.find_element(By.XPATH, '/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div/div[8]/div[1]/div/div/div[1]/div/div/span/span')
                confirm.click()
        else:
                 print("You are not following them already.")

if choice == "1":
    instgrm = Instagram(username, password)
    instgrm.signIn()
    instgrm.getFollowers()  # Get followers
elif choice == "2":
    usernameT = input("Username to be processed: ")
    instgrm = Instagram(username, password)
    instgrm.signIn()
    instgrm.unFollowUser(usernameT)  # Unfollow
elif choice == "3":
    usernameT = input("Username to be processed: ")
    instgrm = Instagram(username, password)
    instgrm.signIn()
    instgrm.followUser(usernameT)  # Follow
else:
    print("Invalid choice, please enter 1, 2, or 3.")







#instgrm.getFollowers()


#instgrm.unFollowUser(usernameT)

#instgrm.followUser(usernameT)
#list = ["","",...]
 #for user in list :
        #instgrm.f(x)(user)
        #time.sleep(3)



