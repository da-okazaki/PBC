### === === === === === === === === === === === === === === === ===
 # selenium_scraping.py
 # Web browser auto login processing.
 # Created by da.okazaki on 2019/03/01.
 # Copyright © 2019 daichi okazaki. All rights reserved.
 ## === === === === === === === === === === === === === === === ===

# webdriver (chrome) 読み込み
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# ブラウザを開く
driver.get("https://qiita.com/")

# login画面へ遷移 (github)
driver.find_element_by_css_selector("a.nl-SocialSignup.nl-SocialSignup-github").click()

# addlessを入力
driver.find_element_by_id('login_field').send_keys("da-okazaki@outlook.com")

# password入力
driver.find_element_by_id('password').send_keys("transD0@")

# singninボタン クリック
driver.find_element_by_css_selector("input.btn.btn-primary.btn-block").click()