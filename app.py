from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from flask import Flask, render_template
from flask import request
import os

app = Flask(__name__)
@app.route('/')
def index():
  host = request.args.get('host')
  length = request.args.get('length')
  if host == None:
    print("Please fill out the required!");
  else:
  	print(host)
  if length == None:
    print("Please fill out the required!");
  else:
    print(length)
    execute();

def execute():
	host = request.args.get('host')
	length = request.args.get('length')
	options = webdriver.ChromeOptions()

  CHROMEDRIVER_PATH = os.environ.get('CHROMEDRIVER_PATH', '/usr/local/bin/chromedriver')
  GOOGLE_CHROME_BIN = os.environ.get('GOOGLE_CHROME_BIN', '/usr/bin/google-chrome')


  options = Options()
  options.binary_location = GOOGLE_CHROME_BIN
  options.add_argument('--disable-gpu')
  options.add_argument('--no-sandbox')
  options.headless = True

  driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH , options=options)
	driver.get("https://trinket.io/python3/980ef28a2b")
	#time.sleep(2)
	driver.execute_script('document.getElementById("trinket-iframe").contentWindow.document.getElementsByClassName("jqconsole-prompt-text")[0].innerText="'+host+'"')
	    #time.sleep(2)
	actions = ActionChains(driver)
	actions.send_keys(Keys.RETURN)
	actions.perform()
	time.sleep(int(length))
