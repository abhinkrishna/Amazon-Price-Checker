import requests
import bs4
import smtplib

url = 'https://www.amazon.in/JBL-C100SI-Ear-Headphones-Black/dp/B01DEWVZ2C/ref=sr_1_3?crid=168N7S8O12VZ3&keywords=jbl+c100si+earphone+with+mic&qid=1561688806&s=gateway&sprefix=jbl+%2Caps%2C405&sr=8-3'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}

def check_price():
    res = requests.get(url)
    webContent = res.text
    soup = bs4.BeautifulSoup(webContent,'lxml')
    item = soup.find(id="productTitle").get_text()
    item = item.strip()
    price = soup.find(id="priceblock_ourprice").get_text()
    price = str(price.encode('utf8'))
    price = price[22:]
    price = float(price[:6])
    print('Item :' , item)
    print('Price :' , price)
    if(price < 600.0):
        send_mail()

def send_mail():
    print("initializing mail server...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('info.hark.in@gmail.com','prxgvibaoqfydwxu')
    subject = 'Price droped down (Test)'
    body = 'Link : https://www.amazon.in/JBL-C100SI-Ear-Headphones-Black/dp/B01DEWVZ2C/ref=sr_1_3?crid=168N7S8O12VZ3&keywords=jbl+c100si+earphone+with+mic&qid=1561688806&s=gateway&sprefix=jbl+%2Caps%2C405&sr=8-3'

    message  = """ Subject: %s \n\n %s """ % (subject , body)
    server.sendmail(
        'info.hark.in@gmail.com',
        'abhinkrishna.ka@gmail.com',
        message
    )
    print('Email has been send...')
    server.quit()

check_price()
