from flask import Flask, send_file, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import io
from PIL import Image
# from datetime import datetime
from uuid import uuid4
import time
import base64
import json

app = Flask(__name__)
app.debug = True

url_base = "http://127.0.0.1:5000/"

@app.route("/", methods=['POST'])
def get_image():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        #chrome_options.add_argument("--no-sandbox") # linux only
        chrome_options.add_argument("--headless")
        # chrome_options.headless = True # also works
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        driver.set_window_size(1920,1080)
        driver.set_page_load_timeout(5)
        encoded_data = base64.b64encode(json.dumps(request.json).encode('utf-8'))
        url = "{}?data={}".format(url_base, encoded_data.decode('utf-8'))
        # print(url)
        driver.get(url)
        img = driver.find_element(By.ID, "container").screenshot_as_png
        imageStream = io.BytesIO(img)
        # im = Image.open(imageStream)
        # path = "./files/{}.png".format(uuid4())
        # im.save(path)
        # time.sleep(3)
        return send_file(imageStream, as_attachment=True, mimetype='image/png', download_name='{}.png'.format(uuid4()))
    except Exception as e:
        print(e)
    finally:
        driver.close()
    
    return "Render failed", 400
    

if __name__ == '__main__':
      app.run(host='0.0.0.0', debug=False, port=5003)