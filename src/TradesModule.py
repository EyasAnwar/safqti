import datetime

from StackCoinTradesManager import StackCoinTradesManager
from TradeManagerLogger import TradeManagerLogger
from Trade import Trade


class TradesModule:

    def __init__(self):
        self.coin_managers = {}
        self.total_profit = 0

    def add_coin(self, name):
        self.coin_managers[name] = TradeManagerLogger(
            StackCoinTradesManager(name))

    def get_coin(self, name):
        if name in self.coin_managers:
            return self.coin_managers[name]
        self.add_coin(name)
        return self.coin_managers[name]

    def swap(self, time, coin1, coin2, amount1, amount2):
        manager1 = self.get_coin(coin1)
        manager2 = self.get_coin(coin2)
        price = manager1.get_amount(time, amount1)
        price = price * float(amount1)/float(amount2)
        trade = Trade(time, amount2, price)
        manager2.add_trade(trade)

    def buy(self, coin, time, amount, price):
        manager = self.get_coin(coin)
        trade = Trade(time, amount, price)
        manager.add_trade(trade)

    def sell(self, coin, time, amount, price):
        manager = self.get_coin(coin)
        total_difference, difference, percentage, start_time = manager.sell(
            time, amount, price)
        self.total_profit += difference
        a = datetime.datetime.fromtimestamp(int(start_time / 1000))
        b = datetime.datetime.fromtimestamp(int(time / 1000))
        c = b - a
        if round(c.days, 0) > 0:
            duration = str(round(c.days, 0)) + ' Days'
        elif round(c.seconds / (60 * 60), 0) > 0:
            duration = str(round(c.seconds / (60 * 60), 0)) + ' Hours'
        else:
            duration = str(round(c.seconds / 60, 0)) + ' Minutes'
        amount_usdt = round(float(amount) * float(price) -
                            round(difference, 2), 1)
        fragment = str(float(price))
        fragment = fragment[fragment.find('.')+1:]
        try:
            avg_buy_price = round(
                float(price) / ((percentage/100) + 1), len(fragment))
        except:
            avg_buy_price = price
        print(datetime.datetime.fromtimestamp(time/1000), coin, float(amount), amount_usdt, avg_buy_price, float(price),
              round(difference, 2), str(round(percentage, 2)) + '%', duration, round(self.total_profit, 2))
        return total_difference, difference, percentage

    def commission(self, time, commission, commissionasset):
        manager = self.get_coin(commissionasset)
        manager.get_amount(time, commission)

    def extract_trades(self):
        all_trades = []
        for manager in self.coin_managers:
            coin_trades = self.coin_managers[manager].get_trades()
            for trade in coin_trades:
                all_trades.append(trade)
        all_trades.sort(key=lambda t: t['start_time'])
        return all_trades
