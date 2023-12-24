import requests
import smtplib
import stock_data
import json
import settings
import datetime
import time

portfolio = []
total_value = 0

def send_mail(text, server_mail, password, client_mail):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(server_mail, password)
    subject = 'Total value of stock portfolio'
    body = 'total portfolio price value on ' + datetime.today().strftime('%Y-%m-%d %H:%M:%S') + ' is: ' + text

    msg = f'subject: {subject} {body}'

    server.sendmail(
        client_mail,
        client_mail,
        msg
    )
    print('email is sent')
    server.quit()


def price_tracker(stock, api_key, api_url_pref):
    stock.url = api_url_pref + stock.name + '?apikey=' + api_key
    share_inf = requests.get(stock.url).json()
    stock.price = share_inf[0]['price']


def portfolio_init(file, api_key, api_url_pref):
    with open(file) as f:
        for jsonObj in f:
            share_position = json.loads(jsonObj, object_hook=stock_data.as_StockPos)
            price_tracker(share_position, api_key, api_url_pref)
            portfolio.append(share_position)


f = open('settings.json')
app_settings = json.loads(f.read(), object_hook=settings.as_AppSettings)
portfolio_init('portfolio_data.json', app_settings.api_key, app_settings.api_url_pref)

for share_pos in portfolio:
    pos_value = share_pos.price * share_pos.amount
    print(share_pos.name + ': ' + str(pos_value))
    total_value = total_value + pos_value
print('---------------------')
print('Total balance: ' + str(total_value))

if app_settings.sendmail > 0:
    send_mail(total_value, app_settings.server_mail, app_settings.server_mail_passw, app_settings.client_mail)

# time.sleep(600)
