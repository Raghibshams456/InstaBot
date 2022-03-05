import itertools
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

#importing webdriver from selenium
from multiprocessing.sharedctypes import Value
from selenium import webdriver
from time import sleep
   #selecting Firefox as the browser
#in order to select Chrome 
# webdriver.Chrome() will be used
browser= webdriver.Firefox()
   
#URL of the website 
url = "https://www.instagram.com/"
   
#opening link in the browser
browser.get(url)

sleep(1)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("******")
password_input.send_keys("*******")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
sleep(20)

a_file = open("/home/i1614/insta/followees.txt")
lines = a_file.readlines()
users=[]
for line in lines:
   line.strip()
   users.append(line)

a_file = open("/home/i1614/insta/followers.txt")
lines = a_file.readlines()
users1=[]
for line in lines:
   line.strip()
   users1.append(line)
#print(users)
#print(users1)
#following=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a/div').click()
#name=browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[2]/div[1]/div/div/span/a").click()
final=set(users)-set(users1)
final=list(final)
for i in final:
   i=i.strip()
   try:
      browser.get("https://www.instagram.com/{}/".format(i))
      browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[2]/div/span/span[1]/button").click()
      browser.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click()
   except:
      pass
