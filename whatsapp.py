from selenium import webdriver
import time

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get('http://web.whatsapp.com')

name = str(input('Enter the name of user or group: '))
msg = str(input('Enter message: '))
count = int(input('Enter how many times to send the message: '))

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_1Plpp')

for i in range(count):
    msg_box.send_keys(str(i + 1) + '. ' + msg)
    driver.find_element_by_class_name('weEq5').click()
    time.sleep(0.2)