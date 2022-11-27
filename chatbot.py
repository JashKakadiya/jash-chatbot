from crypt import methods
from urllib.request import Request
from flask import Flask,request,jsonify
import requests
app = Flask(__name__)
@app.route('/',methods = ['POST'])
def index():
    
    data = request.get_json()
    # print(data)
    S_c = data['queryResult']['parameters']['unit-currency']['currency']
    S_a = data['queryResult']['parameters']['unit-currency']['amount']
    T_c = data['queryResult']['parameters']['currency-name']
    url = "https://api.apilayer.com/exchangerates_data/convert?to={}&from={}&amount={}".format(T_c,S_c,S_a)

    payload = {}
    headers= {
    "apikey": "yMdO66EkPIHhTccZVAAlS0s8pZFpkWMw"
    }

    responsee = requests.request("GET", url, headers=headers, data = payload)


    status_code = responsee.status_code
    resultt = responsee.json()
    # re = resultt['info']['result']
    re = resultt['result']
    response = {
        'fulfillmentText':"{} {} is {} {}".format(S_a,S_c,re,T_c)
    }
    print(response)
    return jsonify(response)
  

if __name__ == "__main__":
    app.run(debug = True)