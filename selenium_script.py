from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def run_selenium_script(report_type, release_date, country, app_type, number_of_apps, rank_lower, rank_upper):
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

    driver.get("https://investment-ten-self.vercel.app/")

    # Wait for the page to load
    time.sleep(2)

    # Fill out the form fields
    # Select Report Type (Example: Top Chart or Keyword Top Chart)
    report_type_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Report Type']"))
    report_type_select.select_by_value(report_type)  # "1" for Top Chart, "2" for Keyword Top Chart

    # Fill Release Date
    release_date_field = driver.find_element(By.XPATH, "//input[@label='Release Date']")
    release_date_field.send_keys(release_date)

    # Select Country
    country_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Country']"))
    country_select.select_by_value(country)

    # Select App Type (free or paid)
    app_type_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='App Type']"))
    app_type_select.select_by_value(app_type)

    # Number of Apps
    num_apps_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Number of Apps']"))
    num_apps_select.select_by_value(str(number_of_apps))

    # Rank Lower Limit
    rank_lower_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Rank Lower Limit']"))
    rank_lower_select.select_by_value(str(rank_lower))

    # Rank Upper Limit
    rank_upper_select = Select(driver.find_element(By.XPATH, "//select[@aria-label='Rank Upper Limit']"))
    rank_upper_select.select_by_value(str(rank_upper))

    # Submit the form by clicking the 'Create Report' button
    create_report_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Create Report')]")
    create_report_button.click()

    # Wait for the response (this could vary depending on the site)
    time.sleep(100)

    # Close the browser
    driver.quit()
