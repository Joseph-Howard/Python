from selenium import webdriver
from selenium.webdriver.chrome.service import service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options


import time

website = 'https://rask-kma.paragonrels.com/ParagonLS/Default.mvc/Login'

#runs browser in back ground.
#options = Options()
#options.headless = True

loginName ='RA435500357'
password ='0523'

path = r"C:\Users\howaja\Desktop\Python\chromedriver.exe"
driver = webdriver.Chrome(path)#, options=options)

#open the website
driver.get(website)
time.sleep(3)

wait = WebDriverWait(driver,10)

wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//input[@id='LoginName']")))
loginInput = driver.find_element(by='xpath', value='//input[@id="LoginName"]')
loginInput.send_keys(loginName)

wait\
    .until(EC.visibility_of_element_located((By.XPATH, '//input[@id="Password"]')))
passwordInput = driver.find_element(by='xpath', value='//input[@id="Password"]')
passwordInput.send_keys(password)

wait\
    .until(EC.visibility_of_element_located((By.XPATH, '//input[@id="Enter"]')))
loginButton = driver.find_element(by='xpath', value= '//input[@id="Enter"]')

passwordInput.send_keys(Keys.ENTER)

time.sleep(2)

wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//span[@id='search-nav']")))
navSearchBtn = driver.find_element(by='xpath', value= "//span[@id='search-nav']")
navSearchBtn.click()

wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Saved Property Searches')]")))
svdPropSearchBtn = driver.find_element(by='xpath', value= "//a[contains(text(),'Saved Property Searches')]")
svdPropSearchBtn.click()

time.sleep(1)

driver.switch_to.frame("tab1")

wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'JH (TEST)')]")))
saved_search = driver.find_element(by='xpath', value="//a[contains(text(),'JH (TEST)')]")
saved_search.click()
driver.switch_to.default_content()
time.sleep(1)

driver.switch_to.frame("tab2_1_1")
time.sleep(.5)
wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//div[@id='MainContent']/div[2]/form/fieldset/div[2]/div[6]/div/input[3]")))
highPrice = driver.find_element(by='xpath', value="//div[@id='MainContent']/div[2]/form/fieldset/div[2]/div[6]/div/input[3]")
wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//div[@id='MainContent']/div[2]/form/fieldset/div[2]/div[6]/div/input")))
lowPrice = driver.find_element(by='xpath', value="//div[@id='MainContent']/div[2]/form/fieldset/div[2]/div[6]/div/input")
wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//div[@id='CountSearch']/button")))
countBtn = driver.find_element(by='xpath', value="//div[@id='CountSearch']/button")
time.sleep(.5)

highPrice.send_keys('0')
countBtn.click()
time.sleep(.25)
wait\
    .until(EC.visibility_of_element_located((By.XPATH, "//div[@id='CountSearch']/input")))
countValue = driver.find_element(by='xpath', value="//div[@id='CountSearch']/input").get_attribute("value")
print('countValue',countValue)
time.sleep(.25)

driver.switch_to.default_content()

time.sleep(10)
driver.quit()
print('worked')
#containers = driver.find_elements(by='xpath', value='//div[@id="content-inner"]/div')


#for container in containers:
    #Wod date
#    Data1 = container.find_element(by='xpath', value = './div/h2/a').text
    #Wod
#    data2 = container.find_element(by='xpath', value = './div[@class="entry"]').text

#    print('Data1', data1)
#    print('data2', data2, '\n\r\n\r')






