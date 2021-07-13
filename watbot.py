import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='e:/aicult/venv/drivers/chromedriver.exe')
driver.get('https://www.instagram.com/')
time.sleep(10)
username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
username.send_keys('')#give your username
password = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input')
password.send_keys('')
time.sleep(2)
login_btn = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div')
login_btn.click()
contact=driver.find_element_by_xpath('//*[@title=""]')#give usename to search
contact=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[3]')
contact.click()
for i in range(1,101):
    time.sleep(0.1)
    msg=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    msg.send_keys('nen kad')
    sendbtn=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button/span')
    sendbtn.click()





