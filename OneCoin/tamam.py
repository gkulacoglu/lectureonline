import http.client
import requests
import json
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
from lxml import html
import threading

app = Flask(__name__)

res = requests.get('https://www.paribu.com/ticker')
data = res.json()
btc = data['BTC_TL']['highestBid']
eth = data['ETH_TL']['highestBid']
ltc = data['LTC_TL']['highestBid'] 

page = requests.get('https://www.bloomberght.com/doviz/euro')
tree = html.fromstring(page.content)
prices = tree.xpath('//*[@id="euro"]/span/small[2]/text()')
pricesf=prices[0].replace(",", ".")
eur= float(pricesf)
one2 = eur * 42.43
    
one ='{:.2f}'.format(one2)
btc ='{:.2f}'.format(btc)
eth ='{:.2f}'.format(eth)
ltc ='{:.2f}'.format(ltc)




@app.route('/') 
def index():
    return render_template('index.html',one=one, btc=btc, eth=eth, ltc=ltc)

if __name__ == "__main__":

    app.run(debug=True)  
    
