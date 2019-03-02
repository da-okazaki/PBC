### === === === === === === === === === === === === === === === ===
 # selenium_scraping.py
 # Web browser auto login processing.
 # Created by da.okazaki on 2019/03/01.
 # Copyright © 2019 daichi okazaki. All rights reserved.
 ## === === === === === === === === === === === === === === === ===

from selenium import webdriver

# ブラウザを開く
driver = webdriver.Safari()
driver.get('https://apple.com/')