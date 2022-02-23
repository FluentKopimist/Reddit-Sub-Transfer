import pwinput
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
def logonReddit(driver):
    userLogon = 0
    while userLogon != 1:
        driver.get("https://old.reddit.com")
        elemInput = driver.find_element_by_name("user")
        userName = input('Reddit Username:')
        elemInput.send_keys(userName)
        elemInput = driver.find_element_by_name("passwd")
        elemInput.clear()
        userPass = pwinput.pwinput()
        elemInput.send_keys(userPass)
        elemWrong = driver.find_element_by_class_name("submit").click
        driver.find_element_by_link_text("https://old.reddit.com/user/Someonespants/")
        if logonCheck == userName:
            print("gay boobs")
        else:
            userLogon = 1
            elemInput.clear()
            print ("stray boobs")
def gatherSubList(driver):
        subList = driver.find_elements_by_id("srList")
        links = subList.find_elements_by_tag_name("a")
        for link in links:
            if links[0:3] == "/r/":
                out.append(link.get_attribute(href) + "/" )
                print(out)
            else:
                next (link)

def rejoinsubReddits(driver):
    driver.find_element_by_class_name("option remove login-required active")
    driver.find_element_by_class_name("option add active")
logonReddit(driver)
gatherSubList

