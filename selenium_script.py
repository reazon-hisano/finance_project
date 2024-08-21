from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time

def run_selenium_script(report_type, email, release_date, country, app_type, number_of_apps, rank_lower, rank_upper):
    # Path to your ChromeDriver
    # options = Options()
    # options.add_argument('--headless')  # Enable headless mode
    # driver = webdriver.Chrome(options=options)
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get("https://investment-ten-self.vercel.app")

    time.sleep(2)

    # Select Report Type
    report_type_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div")
    report_type_element.click()
    # time.sleep(2)
    report_type_option = driver.find_element(By.XPATH, "//*[@id=':r0:']/li[2]")
    report_type_option.click()
    # time.sleep(2)
    email_field = driver.find_element(By.XPATH, "//*[@id='root']/div/div[2]/div")
    email_field.click()
    driver.find_element(By.XPATH, "//*[@id=':r1:']").send_keys(email)
    # time.sleep(2)
    # Fill Release Date
    release_date_field = driver.find_element(By.XPATH, "//*[@id='root']/div/div[3]/div")
    release_date_field.click()
    driver.find_element(By.XPATH, "//*[@id=':r2:']").send_keys(release_date)
    # time.sleep(2)

    # Select Country
    country_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div")
    country_element.click()
    # country_option = driver.find_element(By.XPATH, "//*[@id=':r3:']/li[2]")
    country_option = driver.find_element(By.XPATH, "//*[@id=':r3:']").send_keys(country)
    # country_option.click()
    # time.sleep(2)

    # Select App Type
    app_type_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[5]/div")
    app_type_element.click()
    app_type_option = driver.find_element(By.XPATH, "//*[@id=':r4:']/li[2]")
    app_type_option.click()
    # time.sleep(2)

    # Number of Apps
    # num_apps_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[6]/div")
    # num_apps_element.click()
    # num_apps_option = driver.find_element(By.XPATH, "//*[@id=':r5:']/li[4]")
    # ActionChains(driver)\
    #     .scroll_to_element(num_apps_option)\
    #     .perform()
    # num_apps_option.click()
    # time.sleep(2)

    # Rank Lower Limit
    rank_lower_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[7]/div[1]")
    rank_lower_element.click()
    rank_lower_option = driver.find_element(By.XPATH, "//*[@id=':r6:']/li[5]")
    ActionChains(driver)\
        .scroll_to_element(rank_lower_option)\
        .perform()
    rank_lower_option.click()

    # Rank Upper Limit
    rank_upper_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[7]/div[2]")
    rank_upper_element.click()

    rank_upper_option = driver.find_element(By.XPATH, "//*[@id=':r7:']/li[150]")
    ActionChains(driver)\
        .scroll_to_element(rank_upper_option)\
        .perform()
    rank_upper_option.click()

    num_apps_element = driver.find_element(By.XPATH, "//*[@id='root']/div/div[6]")
    num_apps_element.click()
    num_apps_option = driver.find_element(By.XPATH, "//*[@id=':r5:']/li[20]")
    ActionChains(driver)\
        .scroll_to_element(num_apps_option)\
        .perform()
    num_apps_option.click()

    # Submit the form
    create_report_button = driver.find_element(By.XPATH, "//*[@id='root']/div/button")
    create_report_button.click()

    # Wait for the response
    time.sleep(10)
    delay = 3 # seconds
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "//*[@id='root']/div/a")))
    time.sleep(3)
    # Close the browser
    driver.quit()
