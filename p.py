from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
options = webdriver.FirefoxOptions()
options.add_argument("--headless")

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=options)
driver.get("https://m.facebook.com/reg/?logger_id&cid=103&next=https%3A%2F%2Fm.facebook.com%2Fhome.php&refsrc=deprecated&soft=hjk")

driver.save_screenshot('11.png')
print(driver.title)
driver.close()
