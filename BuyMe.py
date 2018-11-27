# ***** BuyMe sanity text *****

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:/temp/chromedriver.exe")

# Get BuyMe URL from file text
my_file = open("c:/temp/URL.txt",'r')
BuyMeUrl = my_file.read()
time.sleep(2)
my_file.close()
time.sleep(2)
driver.get(BuyMeUrl)
driver.maximize_window()
time.sleep(5)
# log in
driver.find_element_by_css_selector("span.seperator-link").click()
# enter first name
driver.find_element_by_id("ember960").send_keys("yaron.zlotolov@gmail.com")
# enter email address
driver.find_element_by_id("ember962").send_keys("1qaz!QAZ")
# remember me
driver.find_element_by_id("ember969-name").click()
# click enter
driver.find_element_by_css_selector(".orange").click()
time.sleep(5)
# pick a price point
dropbox = driver.find_elements_by_class_name("chosen-container")
dropbox[0].click()
result = driver.find_elements_by_class_name("active-result")
result[2].click()
# pick the area
dropbox = driver.find_elements_by_class_name("chosen-container")
dropbox[1].click()
result = driver.find_elements_by_class_name("active-result")
result[2].click()
# pick category
dropbox = driver.find_elements_by_class_name("chosen-container")
dropbox[2].click()
result = driver.find_elements_by_class_name("active-result")
result[2].click()
# press the search button
driver.find_element_by_id("ember709").click()

# Step C - choose business screen
# pick a business
time.sleep(3)
driver.find_element_by_class_name("thumbnail").click()
time.sleep(3)
# type a price
driver.find_element_by_id("ember1156").send_keys("150")
time.sleep(3)
btn = driver.find_elements_by_xpath("//button[@class='btn btn-theme']")
# for ii in btn:
#     print(ii.get_attribute('class'))
btn[1].click()
# Step D - sender & receiver information screen
# press radio button "for someone else"
time.sleep(3)
driver.find_element_by_xpath("//label[@class='selected']").click()
# enter receiver name
rcv_name = driver.find_elements_by_class_name("ember-text-field")
# for ii in rcv_name:
#     print(ii.get_attribute('class'))
rcv_name[2].clear()
rcv_name[2].send_keys("Ayelet")
# enter sender name
rcv_name[3].clear()
rcv_name[3].send_keys("Yaron Shay Amit Itay")
# enter a blessing
driver.find_element_by_xpath("//textarea").clear()
driver.find_element_by_xpath("//textarea").send_keys("Mazal Tov!")
# Upload a picture
time.sleep(3)
driver.find_element_by_id("ember1277").send_keys("c:\\temp\\mazaltov.jpg")
# pick the event - birthday
time.sleep(3)
events = driver.find_elements_by_class_name("chosen-container-single-nosearch")
# for ii in events:
#     print(ii.get_attribute('class'))
events[4].click()
result = driver.find_elements_by_class_name("active-result")
result[1].click()
# press radio button 'right after payment'
driver.find_element_by_class_name("send-now").click()
# pick email/sms option - sms
driver.find_element_by_xpath("//span[@class='icon icon-sms']").click()
# enter sender phone number
phone = driver.find_elements_by_class_name("ember-text-field")
# for ii in phone:
#     print(ii.get_attribute('class'))
phone[5].clear()
phone[5].send_keys("052-3776494")
# enter receiver phone number
driver.find_element_by_xpath("//input[@id='resendReciver']").clear()
driver.find_element_by_xpath("//input[@id='resendReciver']").send_keys("052-2475588")
# press the save button
driver.find_element_by_class_name("btn-save").click()
# press submit
submit = driver.find_elements_by_class_name("btn-theme")
submit[2].click()
# close driver
time.sleep(5)
driver.quit()



