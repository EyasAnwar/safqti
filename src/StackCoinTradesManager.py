from CoinTradesManager import CoinTradesManager


class StackCoinTradesManager(CoinTradesManager):

    def __init__(self, in_coin_name):
        self.coin_name = in_coin_name
        self.trades_stack = []
        self.total_difference = 0

    def add_trade(self, in_trade):
        self.trades_stack.append(in_trade)
        return len(self.trades_stack)

    def sell(self, time, amount, price):
        exist_amount = 0
        trade = None
        difference = 0
        i = 0
        percentage = 0
        start_time = 0
        _amount = amount
        while True:
            if len(self.trades_stack) == 0:
                break
            trade = self.trades_stack.pop()
            exist_amount, _amount, trade_difference = trade.sell(_amount, price)
            start_time = trade.time
            i += 1
            difference += trade_difference
            if _amount == 0:
                break
        if exist_amount > 0 and trade is not None:
            self.trades_stack.append(trade)
        self.total_difference += difference
        sell_amount_usdt = float(amount) * float(price)
        buy_amount_usdt = sell_amount_usdt - difference
        if buy_amount_usdt > 0:
            percentage = (sell_amount_usdt / buy_amount_usdt) - 1
            percentage = round(percentage * 100, 2)
        return self.total_difference, difference, percentage, start_time

    def get_amount(self, time, amount):
        exist_amount = 0
        trade = None
        avg_price = 0
        comulative_amount = 0
        while True:
            if len(self.trades_stack) == 0:
                break
            trade = self.trades_stack.pop()
            exist_amount, remained_amount = trade.get_amount(amount)
            filled_amount = float(amount) - float(remained_amount)
            amount = remained_amount
            avg_price = trade.get_price() * filled_amount + comulative_amount * avg_price
            comulative_amount += filled_amount
            avg_price = avg_price / comulative_amount
            if remained_amount == 0:
                break
        if exist_amount > 0 and trade is not None:
            self.trades_stack.append(trade)
        return avg_price

    def total_exist(self):
        total = 0
        for trade in self.trades_stack:
            total += trade.exist_amount
        total = round(total, 8)
        return total

    def avg_buy_price(self):
        total = 0
        avg_buy_price = 0
        for trade in self.trades_stack:
            avg_buy_price = (trade.exist_amount * trade.price + total * avg_buy_price)
            total += trade.exist_amount
            avg_buy_price = avg_buy_price / total
        avg_buy_price = round(avg_buy_price, 8)
        return avg_buy_price
