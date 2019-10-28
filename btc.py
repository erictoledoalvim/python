# Importando as bibliotecas utilizadas:
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
from pandas import DataFrame


def btc_poloniex():
    request = requests.get('https://poloniex.com/public?command=returnTicker')
    return request.json()

size = 1000
ask = np.zeros(size)
bid = np.zeros(size)
i = np.zeros(size)
counter = 0
while counter < size:
    # Criando um DataFrame através de um API da Poloniex
    df: DataFrame = pd.DataFrame(btc_poloniex())
    # Gerando os vetores com os valores já convertidos em float
    ask[counter] = float("{0:.2f}".format(pd.to_numeric(df['USDT_BTC']['lowestAsk'])))
    bid[counter] = float("{0:.2f}".format(pd.to_numeric(df['USDT_BTC']['highestBid'])))
    # Pegando o tempo do pc
    time = datetime.datetime.now()
    i[counter] = counter
    # Plotando as informações
    plt.subplot(2, 1, 1)
    if counter > 0:
        if bid[counter] >= bid[counter-1]:
            plt.plot(time, bid[counter], '.g-')
        else:
            plt.plot(time, bid[counter], '.r-')
    plt.ylabel('BID')
    plt.subplot(2, 1, 2)
    if counter > 0:
        if ask[counter] >= ask[counter-1]:
            plt.plot(time, ask[counter], '.g-')
        else:
            plt.plot(time, ask[counter], '.r-')
    plt.ylabel('ASK')
    plt.pause(0.00000001)
    counter += 1
plt.show()