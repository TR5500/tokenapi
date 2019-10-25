from flask import Flask, redirect, url_for
import requests
import json
from string import Template
import time
import re
import operator
from pprint import pprint



app = Flask(__name__)
print("initiated the app! with a name of:", __name__)



@app.route('/', methods=['GET', 'POST'])
def fetchREPkraken():
    base_url='https://api.kraken.com/0/public/Ticker'
    payload = {'pair':'XREPXETH'}
    resp = requests.post(base_url,json=payload)
    AugurEthPrice = resp.json()['result']['XREPXETH']['a'][0]
    return AugurEthPrice




@app.route('/p', methods=['GET', 'POST'])
def fetchEOSkraken():
    b_url = 'https://api.kraken.com/0/public/Ticker'
    load = {'pair':'XEOSXETH'}
    resn = requests.get(b_url, json=load)
    EOSEthPrice = resn.json()["result"]['XEOSXETH']['a'][0]

    return EOSEthPrice




@app.route('/kraken_all')
def fetchallkraken():
    ETH_REP = fetchREPkraken()
    ETH_USD = fetchcryptocompare()

    rep_USD = float(ETH_REP) * float(ETH_USD)

    return ''.join(['--REP_USD ' + str(rep_USD)])


@app.route('/btrx_a')
def fetchREPbtrx():
    url= 'https://bittrex.com/api/v1.1/public/getticker'
    currencyPair = ['ETH-REP']
    load = {'market' : currencyPair}
    response = requests.get(url, params=load)
    result = response.json()["result"]["Ask"]


    return str(result)


@app.route('/btrx_b')
def fetchBATbtrx():
    d_url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-BAT']
    load = {'market' : Pair}
    response = requests.get(d_url, params=load)
    my_result = response.json()['result']['Ask']

    return str(my_result)

@app.route('/btrx_c')
def fetchXRPbtrx():
    e_url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-XRP']
    load = {'market': Pair}
    response = requests.get(e_url, params=load)
    my_result = response.json()['result']['Ask']


    return str(my_result)



@app.route('/btrx_d')
def fetchOMGbtrx():
    f_url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-OMG']
    load = {'market': Pair}
    response = requests.get(f_url, params=load)
    my_result = response.json()['result']['Ask']

    return str(my_result)

@app.route('/btrx_e')
def fetchXLMbtrx():
    f_url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-XLM']
    load = {'market': Pair}
    response = requests.get(f_url, params=load)
    my_result = response.json()['result']['Ask']

    return str(my_result)



@app.route('/btrx_f')
def fetchBNTbtrx():
    f_url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-BNT']
    load = {'market': Pair}
    response = requests.get(f_url, params=load)
    my_result = response.json()['result']['Ask']

    return str(my_result)

@app.route('/btrx_g')
def fetchARKbtrx():
    url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['BTC-ARK']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)

@app.route('/btrx_h')
def fetchZECbtrx():
        url = 'https://bittrex.com/api/v1.1/public/getticker'
        Pair = ['ETH-ZEC']
        load = {'market': Pair}
        response = requests.get(url, params=load)
        result = response.json()['result']['Ask']

        return str(result)

@app.route('/btrx_i')
def fetchXMRbtrx():
    url ='https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-XMR']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)

@app.route('/btrx_j')
def fetchDCRbtrx():
    url ='https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['BTC-DCR']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)

@app.route('/btrx_k')
def fetchADAbtrx():
    url ='https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-ADA']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)

#app.route('/btrx_l')
#def fetchADTbtrx():
#    url ='https://bittrex.com/api/v1.1/public/getticker'
#    Pair = ['ETH-ADT']
#    load = {'market': Pair}
#    response = requests.get(url, params=load)
#    result = response.json()['result']['Ask']

#    return str(result)

@app.route('/btrx_m')
def fetchZRXbtrx():
    url ='https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-ZRX']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)
# something is wrong with /btrx_n. price from route is too high
@app.route('/btrx_n')
def fetchDNTbtrx():
    url ='https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['BTC-DNT']
    load = {'market': Pair}
    response = requests.get(url, params=load)
    result = response.json()['result']['Ask']

    return str(result)





@app.route('/etherprice')
def fetchcryptocompare():

    url = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'

    response = requests.get(url)
    results = response.json()

    return str(results['USD'])

@app.route('/btcprice')
def fetchblockchaininfo():
    url = 'https://blockchain.info/ticker'
    Pair = ['USD']
    response = requests.get(url, params=Pair)
    results = response.json()['last']

    return str(results)

@app.route('/salt_price')
def fetchSALTbtrx():
    url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-SALT']
    load = {'market': Pair}
    response = requests.get(url, params = load)
    results = response.json()['result']['Ask']

    return str(results)

@app.route('/gno_price')
def fetchGNOTbtrx():
    url = 'https://bittrex.com/api/v1.1/public/getticker'
    Pair = ['ETH-GNO']
    load = {'market': Pair}
    response = requests.get(url, params = load)
    results = response.json()['result']['Ask']

    return str(results)


@app.route('/btrx_all')
def fetchAllBittrex():
    eth_REP = fetchREPbtrx()
    eth_BAT = fetchBATbtrx()
    eth_XRP = fetchXRPbtrx()
    eth_OMG = fetchOMGbtrx()
    eth_XLM = fetchXLMbtrx()
    eth_BNT = fetchBNTbtrx()
    btc_ARK = fetchARKbtrx()
    eth_ZEC = fetchZECbtrx()
    eth_XMR = fetchXMRbtrx()
    eth_USD = fetchcryptocompare()
    btc_DCR = fetchDCRbtrx()
    eth_ADA = fetchADAbtrx()
    #eth_ADT = fetchADTbtrx()
    eth_ZRX = fetchZRXbtrx()
#    eth_SALT = fetchSALTbtrx()
    #eth_GNO = fetchGNObtrx()



    rep_USD = float(eth_REP) * float(eth_USD)
    bat_USD = float(eth_BAT) * float(eth_USD)
    xrp_USD = float(eth_XRP) * float(eth_USD)
    omg_USD = float(eth_OMG) * float(eth_USD)
    xlm_USD = float(eth_XLM) * float(eth_USD)
    bnt_USD = float(eth_BNT) * float(eth_USD)
    ark_USD = float(btc_ARK) * float(9200)
    zec_USD = float(eth_ZEC) * float(eth_USD)
    xmr_USD = float(eth_XMR) * float(eth_USD)
    dcr_USD = float(btc_DCR) * float(9200)
    ada_USD = float(eth_ADA) * float(eth_USD)
    #adt_USD = float(eth_ADT) * float(eth_USD)
    zrx_USD = float(eth_ZRX) * float(eth_USD)
    #salt_USD = float(eth_SALT) * float(eth_USD)
    #gno_USD = float(eth_GNO) * float(eth_USD)


    #return str(rep_USD)
    return ''.join(['--REP_USD: '+ str(rep_USD), '--BAT_USD '+ str(bat_USD), '--XRP_USD '+ str(xrp_USD), '--OMG_USD '+ str(omg_USD), '__XLM_USD '+ str(xlm_USD), '--BNT_USD-- '+ str(bnt_USD), '--ARK_USD '+ str(ark_USD), '--ZEC_USD '+ str(zec_USD), '--ETH_USD '+ str(eth_USD), '--XMR_USD '+ str(xmr_USD), '--DCR_USD---'+ str(dcr_USD), '--ADA_USD--', str(ada_USD), '--ZRX_USD--', str(zrx_USD)])







@app.route('/polnx')
def fetchREPpoloniex():
    e_url = 'https://poloniex.com/public?command=returnTicker'
    moneyPair = ['ETH_REP']
    #:{'last':,'lowestASk':,'highestBid':,'percent change':,'baseVolume':,'quoteVolume':}]
    load = {'ticker' : moneyPair}
    response = requests.get(e_url, params = load)
    result = response.json()["ETH_REP"]["last"]

    return str (result)

#@app.route('/polnx_y')
#def fetchGNOpoloniex():
#    f_url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ["ETH_GNO"]
#    load = {'ticker': moneyPair}
#    response = requests.get(f_url, params = load)
#    result = response.json()["ETH_GNO"]['last']

#    return str(result)

#@app.route('/polnx!')
#def fetchOMGpoloniex():
#    g_url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ['ETH_OMG']
#    load = {'ticker': moneyPair}
#    response = requests.get(g_url, params = load)
#    result = response.json()['ETH_OMG']['last']


#    return str(result)

@app.route('/polnx#')
def fetchXRPpoloniex():
    url = 'https://poloniex.com/public?command=returnTicker'
    moneyPair = ['ETH_ZEC']
    load = {'ticker': moneyPair}
    response = requests.get(url, params=load)
    result = response.json()['ETH_ZEC']['last']

    return str(result)

@app.route('/polnx_p')
def fetchZRXpoloniex():
    url = 'https://poloniex.com/public?command=returnTicker'
    moneyPair = ['ETH_ZRX']
    load = {'ticker': moneyPair}
    response = requests.get(url, params=load)
    result = response.json()['ETH_ZRX']['last']

    return str(result)

@app.route('/polnx_q')
def fetchBATpoloniex():
    url = 'https://poloniex.com/public?command=returnTicker'
    moneyPair = ['ETH_BAT']
    load = {'ticker': moneyPair}
    response = requests.get(url, params=load)
    result = response.json()['ETH_BAT']['last']

    return str(result)

@app.route('/polnx_r')
def fetchZECpoloniex():
    url = 'https://poloniex.com/public?command=returnTicker'
    moneyPair = ['ETH_ZEC']
    load = {'ticker': moneyPair}
    response = requests.get(url, params=load)
    result = response.json()['ETH_ZEC']['last']

    return str(result)
#@app.route('/polnx_t')
#def fetchBCHpoloniex():
#    url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ['ETH_BCH']
#    load = {'ticker': moneyPair}
#    response = requests.get(url, params=load)
#    result = response.json()['ETH_BCH']['last']

#    return str(result)


#@app.route('/polnx_u')
#def fetchLSKpoloniex():
#    url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ['ETH_LSK']
#    load = {'ticker': moneyPair}
#    response = requests.get(url, params=load)
#    result = response.json()['ETH_LSK']['last']

#    return str(result)

#@app.route('/polnx_v')
#def fetchGASpoloniex():
#    url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ['ETH_GAS']
#    load = {'ticker': moneyPair}
#    response = requests.get(url, params=load)
#    result = response.json()['ETH_GAS']['last']

#    return str(result)

#@app.route('/polnx_w')
#def fetchGNTpoloniex():
#    url = 'https://poloniex.com/public?command=returnTicker'
#    moneyPair = ['ETH_GNT']
#    load = {'ticker': moneyPair}
#    response = requests.get(url, params=load)
#    result = response.json()['ETH_GNT']['last']

#    return str(result)




@app.route('/polnx_all')
def fetchAllPoloniex():
    #REP_USDD = 10
    eth_REP = fetchREPpoloniex()
    #eth_GNO = fetchGNOpoloniex()
    #eth_OMG = fetchOMGpoloniex()
    eth_ZRX = fetchZRXpoloniex()
    eth_USD = fetchcryptocompare()
    eth_BAT = fetchBATpoloniex()
    eth_ZEC = fetchZECpoloniex()
    #eth_BCH = fetchBCHpoloniex()
#    eth_LSK = fetchLSKpoloniex()
#    eth_GAS = fetchGASpoloniex()
#    eth_GNT = fetchGNTpoloniex()

    rep_USD = float(eth_REP) * float(eth_USD)
#    omg_USD = float(eth_OMG) * float(eth_USD)
#    gno_USD = float(eth_GNO) * float(eth_USD)
    zrx_USD = float(eth_ZRX) * float(eth_USD)
    BAT_USD = float(eth_BAT) * float(eth_USD)
    ZEC_USD = float(eth_ZEC) * float(eth_USD)
    #bch_USD = float(eth_BCH) * float(eth_USD)
#    lsk_USD = float(eth_LSK) * float(eth_USD)
#    gas_USD = float(eth_GAS) * float(eth_USD)
#    gnt_USD = float(eth_GNT) * float(eth_USD)
    #omg_USD = float(eth_OMG) * float(eth_USD)
    return ''.join(['--REP_USD ' + str(rep_USD), '--eth_ZRX ' + str(zrx_USD), '--eth_USD ' + str(eth_USD), '--BAT_USD ' + str(BAT_USD), '--ZEC_USD' + str(ZEC_USD)])














#time.sleep(5)

#print("5 second updated price is...")



if __name__ == '__main__':
    print('app is sarting...I think?')
    print('no idea how this message will be seen...')


    #while True:
        #krakenUSDLive = float(val())

        #print 'Kraken Price in USD=', kraken USDLive
    app.run(use_reloader=True)
