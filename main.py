# Course URL: https://www.udemy.com/course/automate-everything-with-python/
import requests as re
from datetime import datetime
import time
###############################
###############################
# beautifulsoup dirty version: collect stock price
url = 'https://www.udemy.com/course/automate-everything-with-python/'
headers = {
  "User-Agent":
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}
content = re.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)
###############################
###############################
# automated process:
# Author: Ardit Sulce, Automate Everything with Python, Udemy
# Course URL: https://www.udemy.com/course/automate-everything-with-python/

import requests
from datetime import datetime
import time

ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {
  "User-Agent":
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}

content = requests.get(url, headers=headers).content
print(content)

with open('data.csv', 'wb') as file:
  file.write(content)

###############################
###############################
#extract currency rate from the web: x-rate
from bs4 import BeautifulSoup


def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from ={in_currency}&to={out_currency}&amount = 1'
  #print(url)
  content = re.get(url).text
  result = BeautifulSoup(content, 'html.parser')
  currency = result.find('span', class_='ccOutputRslt').get_text()
  currency = currency[0:-4]


get_currency('INR', 'USD')
