from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from random import choice
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
driver.save_screenshot('11.png')
print(driver.title)

try:
    #button = driver.find_element(By.CSS_SELECTOR, "[data-testid='open-registration-form-button']").click()
    driver.implicitly_wait(10)
    driver.get("https://m.facebook.com/reg/?logger_id&cid=103&next=https%3A%2F%2Fm.facebook.com%2Fhome.php&refsrc=deprecated&soft=hjk")

    driver.save_screenshot('0.png')
    time.sleep(2)
    driver.find_element(By.NAME, "firstname").send_keys("mona")
    driver.save_screenshot('1.png')
    time.sleep(2)
    print('firstname')
    driver.find_element(By.NAME, "lastname").send_keys("ali")
    time.sleep(2)
    print('lastname')
    driver.find_element(By.XPATH, "//*[@data-sigil='touchable multi_step_next']").click()
    driver.save_screenshot('2.png')
    time.sleep(2)
    day_dropdown = driver.find_element(By.XPATH, "//select[@class='_8wou _8y5o _8y5q _6as5 _47ko _47kp'][@aria-label='Day']")
    # list of all days
    days = [str(i) for i in range(1, 32)]
    # select a random day
    random_day = random.choice(days)
    day_dropdown.send_keys(random_day)
    time.sleep(2)
    month_dropdown = driver.find_element(By.XPATH, "//select[@class='_8wou _8y5o _8y5q _6as5 _47ko _47kp'][@aria-label='Month']")
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    # select a random month name
    random_month = random.choice(month_names)
    month_dropdown.send_keys(random_month)
    year =  driver.find_element(By.XPATH, '//*[@id="year"]')
    # Generate a random number between 1985 and 2002
    random_year = str(random.randint(1985, 2002))

    # Enter the number
    year.send_keys(random_year)
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@data-sigil='touchable multi_step_next']").click()
    driver.save_screenshot('3.png')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[11]/div/a[1]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="contactpoint_step_input"]').send_keys('kjsndkfjn@gmail.com')
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@data-sigil='touchable multi_step_next']").click()
        
    gender_options = driver.find_elements(By.XPATH, "//div[@data-sigil='multi_step_input_area']")
    random_gender = choice(gender_options)
    #print(gender_options)
    input_element = random_gender.find_element(By.XPATH, "//input[@type='radio']")
    input_element.click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@data-sigil='touchable multi_step_next']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="password_step_input"]').send_keys('odfklgjgljgdfg')
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mobile-reg-form"]/div[9]/div[2]/button[4]').click()
    time.sleep(5)
    for a in range(20):
        time.sleep(5)
        driver.save_screenshot('finsh.png')
    #driver.close()
    print('ues')
    driver.close()
except Exception as s:
    print(s)
    driver.save_screenshot('erro.png')
    driver.close()
