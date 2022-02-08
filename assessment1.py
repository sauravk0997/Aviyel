from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://uitestingplayground.com/home")
links = driver.find_elements(By.TAG_NAME, "a")
for link in links:
    print(link.get_attribute('href'))
