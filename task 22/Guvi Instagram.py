from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time


class Piyush:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def followers_count(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(10)
        followers = self.driver.find_element(By.XPATH, "(//span[@class='_ac2a'])[2]")
        fol = followers.get_attribute("title")
        print("followers=", fol)

    def following_count(self):
        following = self.driver.find_element(By.XPATH,
                                             "//ul[@class='x78zum5 x1q0g3np xieb3on']/li[3]/button/span/span").text
        print("following=", following)


url = "https://www.instagram.com/guviofficial/"
p = Piyush(url)
p.followers_count()
p.following_count()
