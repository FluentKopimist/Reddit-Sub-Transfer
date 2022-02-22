import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://old.reddit.com")
assert "Python" in driver.title
while userLogon != 1
    elem = driver.find_element_by_class_name("login-required login-link")
    userName = input('Reddit Username:')
    userPass = input('Reddit Password:')
    elemInput = driver.find_element_by_name("user")
    elem.send_keys(userName)
    elem.send_keys(Keys.RETURN)
    elemInput = driver.find_element_by_name("passwd")
    elem.send_keys(userPass)
    elem.send_keys(Keys.RETURN)
    elemWrong = driver.find_element_by_class_name("tooltip-inner") #Returns validity of password
    if elemWrong == "wrong password":
        print ("Wrong Username or Password, Please try again.")
    else userLogon = 1

    subList = driver.find_elements_by_id("srList")
    links = subList.find_elements_by_tag_name("a")
    for link in links:
        if links[0:3] != "/r/"
        out = out + links + "/" + link.get_attribute(href)
    
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

html = requests.get("https://old.reddit.com").text



soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all("a"):
    link = a.get("href")
    if link:
        print(link)
