from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://www.asu.edu/healthcheck/'
headers = {'User-Agent': 'Mozilla/5.0'}

account = 'slin97'
password = 'Letmefindajob2020'

wb = '/Users/michael/Desktop/Projects/automation/chromedriver'
driver = webdriver.Chrome(wb)

driver.get(url)
submit_check = driver.find_element_by_link_text('Complete daily health checks')
submit_check.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    print('ok')
    userId = driver.find_element_by_id("username").send_keys(account)
    pwd = driver.find_element_by_id("password").send_keys(password)

    driver.implicitly_wait(1.5)
    driver.find_element_by_name("submit").click()

    driver.implicitly_wait(5)
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[3]/button")))    
    driver.switch_to.default_content()

    driver.switch_to.frame(0)
    # None
    driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/button[4]").click()
    # Next
    driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[3]/div/div[3]").click()

    driver.implicitly_wait(5)

    # None
    driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[3]/div/div[3]/button/span[1]").click()

    # Submit
    driver.find_element_by_xpath("/html/body/div[1]/div/main/div/div/div[3]/div/div[4]/button/span[1]").click()



finally:
    driver.close()
    print('Done!')