from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from flask import Flask, render_template
from flask import request
import requests
from requests.structures import CaseInsensitiveDict
import time
import os

app = Flask(__name__)


@app.route('/')
def index():
  quizid = request.args.get('quizid')
  if quizid == None:
    print("invalid args");
  else:
    print(quizid);
    execute();
    return '{Executer: Online}'


def execute():
    CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
    GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')
    options = Options()
    options.binary_location = GOOGLE_CHROME_BIN
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless")
    options.add_argument(f'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36')
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , chrome_options=options)
    driver.get("https://quizizz.com/join?gc=155785&source=liveDashboard")
    time.sleep(5)
    driver.find_element_by_xpath("//div[@id='root']/div/div/div/div/div/div[2]/div[2]/div/div/form/div/div[2]/div[2]/i").click()
    time.sleep(5)
    driver.quit();
    
if __name__=='__main__':
    app.run(debug=True)
