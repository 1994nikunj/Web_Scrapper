import datetime
import time
import winsound

import requests
from bs4 import BeautifulSoup

url = 'https://www.flipkart.com/google-pixel-4a-just-black-128-gb/p/itm023b9677aa45d?pid=MOBFUSBNAZGY7HQU&lid=LSTMOBFUSBNAZGY7HQUWHTF0C'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
           "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "DNT": "1",
           "Connection": "close",
           "Upgrade-Insecure-Requests": "1"}

if __name__ == '__main__':
    r = requests.get(url, headers=headers)
    content = r.content
    soup = BeautifulSoup(content, features="html.parser")

    while True:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        if soup.find(text='NOTIFY ME'):
            print('OUT OF STOCK| {}'.format(now))
        elif soup.find(text='BUY NOW') and soup.find(text='ADD TO CART'):
            winsound.Beep(frequency=700, duration=2000)
            print('ITEM FOUND| Time: {}'.format(now))
        time.sleep(5)
