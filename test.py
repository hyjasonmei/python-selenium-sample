from selenium import webdriver
# from PIL import Image
#from Screenshot import Screenshot_clipping
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# driver = webdriver.Chrome(executable_path = './chromedriver.exe')
url = "https://playground.anychart.com/eYa2on5E/2/view"
driver.get(url)
driver.save_screenshot('screenie.png')
