from strategy import strategyLogic
from candles import candleLogic
from vaules import userVals

from oandapyV20 import api
import oandapyV20
from oandapyV20.contrib.requests import MarketOrderRequest
from oandapyV20.contrib.requests import TakeProfitDetails, StopLossDetails
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.accounts as accounts

class trading():
    def __init__(self):
        self.resistance = 0
        self.support = 0
        self.status = "Not Trading"
        self.currentTrade = ""
        self.kill = False #kill switch change to false to kill

        s = strategyLogic()
        c = candleLogic()
        self.data = c.getData()

        self.currentClose = self.data[-1]
        self.lotSize = ()
        self.SMA1 = s.SMA(self.data, userVals.count, userVals.SMAbig)
        self.SMA1previous = s.SMAprev(self.data, userVals.count, userVals.SMAbig)
        self.SMA2 = s.SMA(self.data, userVals.count, userVals.SMAsmall)
        self.SMA2previous = s.SMAprev(self.data, userVals.count, userVals.SMAsmall)

    def enterLong(self):
        if(self.SMA1 < self.SMA2) and (self.SMA1previous < self.SMA2): return True
        return False

    def enterShort(self):
        if (self.SMA > self.SMA2) and (self.SMA1previous > self.SMA2): return True
        return False

    def getTrades(self):
        r = accounts.AccountDetails(userVals.accountID)
        client = api(access_token = userVals.key)
        rv = client.request(r)
        self.details = rv.get('account')
        return self.details.get('openTradeCount')

    def lots(self):
        r = accounts.AccountDetails(userVals.accountID)
        client = api(access_token=userVals.key)
        rv = client.request(r)
        self.details = rv.get('account')
        balance = self.details.get('NAV')
        size = 0

        if self.enterLong() == True:
            size = abs(int((float(balance) * float(userVals.risk))/(self.currentClose - self.support)))

        elif self.enterShort() == True:
            size = abs(int((float(balance) * float(userVals.risk)) / (self.currentClose - self.resistance)))

        return size

    def closePosition(self):
        if self.currentTrade == 'Long':
            data = {"longUnits":"ALL"}
            client = oandapyV20.api(access_token = userVals.key)
            r = positions.PositionClose(accountID = userVals.accountID, instrument = userVals.instrument, data=data)
            client.request(r)
        elif self.currentTrade == "Long":
            data = {'shortUnits':'ALL'}
            client = oandapyV20.api(access_token=userVals.key)
            r = positions.PositionClose(accountID=userVals.accountID, instrument = userVals.instrument,data=data)
            client.request(r)

    def main(self):
        self.resistance=max(self.data[(userVals.count - 6):userVals.count])
        self.support = min(self.data[(userVals.count-6):userVals.count])

        mktOrderLong = MarketOrderRequest(instrument = userVals.pair,
            units = self.lots(),
            takeProfitOnFill = TakeProfitDetails(price=self.resistance).data,
            stopLossOnFill=StopLossDetails(price=self.support).data)
        mktOrderShort = MarketOrderRequest(instrument=userVals.pair,
            units = (self.lots() *-1),
            takeProfitOnFill = TakeProfitDetails(price=self.support).data,
            stopLossOnFill = StopLossDetails(price = slef.resistance).data)

        if self.getTrades()==0:
            print("Looking for Trades")

            if self.enterLong() == True:
                api = oandapyV20.api(access_token=userVals.key)
                r = orders.OrderCreate(userVals.accountID,data=mktOrderLong.data)
                api.request(r)
                self.status == "Trading"
                self.currentTrade = "Long"
                print('Trade executed')

            elif self.enterShort() == True:
                api = oandapyV20.api(access_token=userVals.key())
                r = orders.OrderCreate(userVals.accountID, data=mktOrderShort.data)
                api.request(r)
                self.status =="Trading"
                self.currentTrade == "Short"
                print("trade executed")
            elif self.enterLong() and self.enterShort() == False:
                print("No trades open looking for entry")
        else:
            if self.currentTrade == "Short":
                if self.enterLong() == True:
                    self.closePosition()
                    self.status == "Not Trading"
                    print("Trade Exited")
                else:
                    print ("No exits looking")
            else:
                self.kill - True
                print("error closing down")

if __name__=="__main__":
    t =trading()
    while(t.kill == False):
        t.main()
