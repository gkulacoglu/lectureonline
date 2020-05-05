import http.client
import requests
import json
from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime

app = Flask(__name__)

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 5KKw1hX17j46HskkFKHLcw:1SUlqw7qVhc8IqZXfQYuht"
    }



conn.request("GET", "/economy/exchange?int=10&to=TRY&base=EUR", headers=headers)
res = conn.getresponse()
data = res.read()
y = json.loads(data.decode('utf-8')) 
kur = float(y["result"]["data"][0]["rate"])
one  = kur * 42.43

@app.route('/') 
def index():
    return render_template('index.html',one=one)

if __name__ == "__main__":

    app.run(debug=True)  