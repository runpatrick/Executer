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
  host = request.args.get('host')
  length = request.args.get('length')
  method = request.args.get('method')
  if host == None:
    print("Please fill out the required!");
  else:
    print(host);
    prehost = host;
  if method == None:
    print("Please fill out the required!");
  else:
    print(method);
    premethod = method;
  if length == None:
    print("Please fill out the required!");
  else:
    print(length)
    prelength = length;
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
    driver.get("https://katacoda.com/embed/runpatrick/courses/challenges/node-challenge-1/?v=2&embed=true&ui=inline&host=137.184.30.68&url=http%3A%2F%2F137.184.30.68%2Ftest%2F%3Fhost%3D1&target=katacoda-scenario-1&nonce=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWJlZCI6dHJ1ZSwiZG9tYWluIjoiaHR0cDovLzEzNy4xODQuMzAuNjgvIiwiaXAiOiIyNC4yMjguMTA5LjI1NSIsImlhdCI6MTYzMTg2NTgzMiwiZXhwIjoxNjMxODY1ODYyfQ.DA-Sa33cRPy1IrloJNxqvIs37wotHl6KdSgyzCNYNPg&color=004d7f")
    time.sleep(7)
    url = driver.execute_script("return document.getElementById('weburl').innerText;")
    print(url)
    #requests.post(url+"?host=137.184.30.68&method=udp&time=10")
    time.sleep(20)
    driver.quit();

