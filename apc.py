import requests
import bs4
import smtplib
# create a myAccount.py file on same directory with content below
    ####################################################
    # username = <yourMailAddress@serviceProvider.com> #
    # password = <yourAccountPassword>                 #
    ####################################################
import myAccount # importing myAccount.py file.

def check_price():
    try:
        print("getting data please wait...")
        res = requests.get(url)
        webContent = res.text
        soup = bs4.BeautifulSoup(webContent,'lxml')
        item = soup.find(id="productTitle").getText()
        item = item.strip()
        price = soup.find(id="priceblock_ourprice").getText()
        price = str(price.encode('utf8'))
        price = price[22:]
        price = float(price[:6])
        print('Item :' , item)
        print('Price :' , price)
        if(price < des_price):
            print("Desired price is less than :)" , price)
            res = input("Do you want to mail information (y/n)")
            if(res == 'y' or res == 'Y'):
                send_mail()
            else:
                print('Okay... email service ignored')
        else:
            print("Price is higher... :(")
    except Exception as e:
        print("Somethig went wrong..." + str(e))
        res = input("Do you want to try again? (y/n) : ")
        if(res == 'y' or res == 'Y'):
            check_price()
        else:
            print("okay...")



def send_mail():
    to_mailaddress = input("e-mail address of recipient : ")
    print("Initializing mail services")
    print("Connection establishing....")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(myAccount.username,myAccount.password)
    print("Connection established")
    print("writing message...")
    subject = 'Test Email from python'
    body = 'Hi, price has droped! Checkout ' + url
    message  = """ Subject: %s \n\n %s """ % (subject , body)
    print("Sending e-mail to ",to_mailaddress)
    server.sendmail(
        myAccount.username,
        to_mailaddress,
        message
    )
    print('Success!')
    server.quit()

url = input("Product URL : ")
des_price = int(input("Desired price : "))
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
check_price()
input()
