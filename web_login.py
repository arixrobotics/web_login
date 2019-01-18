from selenium import webdriver
from selenium.webdriver.common.keys import Keys


url = "https://www.facebook.com"
driver = webdriver.Chrome()
driver.get(url)

u = driver.find_element_by_name('email')
u.clear()
u.send_keys('myemail@gmail.com')

p = driver.find_element_by_name('pass')
p.clear()
p.send_keys('mypassword')
p.send_keys(Keys.RETURN)

#t = driver.find_element_by_name('visitor_accept_terms')
#t.send_keys(Keys.SPACE)
#t.send_keys(Keys.RETURN)
