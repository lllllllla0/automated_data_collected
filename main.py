# Course URL: https://www.udemy.com/course/automate-everything-with-python/
import requests as re
from datetime import datetime
import time

url = 'https://www.udemy.com/course/automate-everything-with-python/'
headers = {
  "User-Agent":
  "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
}
content = re.get(url, headers=headers).content
#print(content)

# with open('data.csv', 'wb') as file:
#   file.write(content)

# automated process:
ticker = input("Enter the ticker symbol: ")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')
from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int()
to_epoch = int()
