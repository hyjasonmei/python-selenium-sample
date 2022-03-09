from selenium import webdriver
# from PIL import Image
#from Screenshot import Screenshot_clipping
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1920,600)
# driver = webdriver.Chrome(executable_path = './chromedriver.exe')
url = "http://127.0.0.1:8080/"
driver.get(url)
driver.save_screenshot('screenie.png')
screenshot = Image.open('screenie.png')
w, h = screenshot.size
im1 = screenshot.crop((10, 150, w-15, h-150)) 
im1.save('screenie.png')
