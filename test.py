from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import io
from PIL import Image
from datetime import datetime

start=datetime.now()
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.set_window_size(1920,1080)
print(datetime.now()-start)

start=datetime.now()
# driver = webdriver.Chrome(executable_path = './chromedriver.exe')
url = "http://127.0.0.1:8080/"
driver.get(url)
# driver.save_screenshot('screenie.png')
img = driver.find_element(By.ID, "container").screenshot_as_png
imageStream = io.BytesIO(img)
im = Image.open(imageStream)
im.save("aaaaa.png")
print(datetime.now()-start)

start=datetime.now()
url = "http://127.0.0.1:8080/"
driver.get(url)
# driver.save_screenshot('screenie.png')
img = driver.find_element(By.ID, "container").screenshot_as_png
imageStream = io.BytesIO(img)
im = Image.open(imageStream)
im.save("aaaaa2.png")
print(datetime.now()-start)

start=datetime.now()
url = "http://127.0.0.1:8080/"
driver.get(url)
# driver.save_screenshot('screenie.png')
img = driver.find_element(By.ID, "container").screenshot_as_png
imageStream = io.BytesIO(img)
im = Image.open(imageStream)
im.save("aaaaa3.png")
print(datetime.now()-start)
# screenshot = Image.open('screenie.png')
# w, h = screenshot.size
# print(w)
# print(h)
# im1 = screenshot.crop((10, 0, w-15, 300)) 
# im1.save('screenie.png')
