from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager

options = webdriver.FirefoxOptions()
# add options to the FirefoxOptions object if necessary

driver = webdriver.Firefox(service=webdriver.service.Service(executable_path=GeckoDriverManager().install()), options=options)
driver.get("https://m.facebook.com/reg/?logger_id&cid=103&next=https%3A%2F%2Fm.facebook.com%2Fhome.php&refsrc=deprecated&soft=hjk")

driver.save_screenshot('0.png')
print(driver.title)
driver.close()
