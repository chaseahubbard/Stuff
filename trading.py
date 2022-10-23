
import queue
import threading
import time

import pandas as pd
import oandapyV20
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing

import configparser
ENVIRONMENTS = {
    "streaming": {
        "real": "stream-fxtrade.oanda.com",
        "practice": "stream-fxpractice.oanda.com",
        "sandbox": "stream-sandbox.oanda.com"
    },
    "api": {
        "real": "api-fxtrade.oanda.com",
        "practice": "api-fxpractice.oanda.com",
        "sandbox": "api-sandbox.oanda.com"
    }
}

DOMAIN = "practice"
STREAM_DOMAIN = ENVIRONMENTS["streaming"][DOMAIN]
API_DOMAIN = ENVIRONMENTS["api"][DOMAIN]

access_token = "6fae1591adc367882839af4895195806-ccf49852cd961c9bf095638334611262"
accountID = "101-001-11257927-001"
api = API(access_token=access_token)


from exe import Execution
from strat import TestRandom
from stream import StreamingForexPrices

def trade(events, strategy, execution):

    while True:
        try:
            event = events.get(False)
        except queue.Empty:
            pass
        else:
            if event is not None:
                if event.type == "TICK":
                    strategy.calculate_signals(event)
                elif event.type == "ORDER":
                    print("Executing order!")
                    execution.execute_order(event)

        time.sleep(heartbeat)

if __name__=="__main__":
    heartbeat = 0.5
    events = queue.Queue()

    instrument = 'EUR_USD'
    units = 10000

    prices = StreamingForexPrices(
        STREAM_DOMAIN, access_token, accountID,
        instrument,events
        )

    execution = Execution(API_DOMAIN,access_token,accountID)

    strategy = TestRandom(instrument,units,events)

    trade_thread = threading.Thread(target=trade, args=(events, strategy, execution))
    price_thread = threading.Thread(target = prices.stream_to_queue, args=[])

    trade_thread.start()
    price_thread.start()
