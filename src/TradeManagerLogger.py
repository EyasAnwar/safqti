import datetime


class TradeManagerLogger:

    def __init__(self, coin_trades_manager):
        self.coin_trades_manager = coin_trades_manager
        self.trades = []
        self.trade = {}
        self.total_buy_amount = 0
        self.total_sell_amount = 0
        self.avg_buy_price = 0
        self.avg_sell_price = 0

    def add_trade(self, in_trade):
        len = self.coin_trades_manager.add_trade(in_trade)
        a = in_trade.amount * in_trade.price + self.total_buy_amount * self.avg_buy_price
        self.total_buy_amount += in_trade.amount
        self.avg_buy_price = a / self.total_buy_amount
        if self.avg_buy_price == 0:
            pass
        if len == 1:
            self.trade['start_time'] = in_trade.time
            self.trade['coin_name'] = self.coin_trades_manager.coin_name
            self.trade['orders'] = []
            self.trade['total_amount'] = 0
            self.trade['avg_buy_price'] = 0
            self.trade['avg_sell_price'] = 0
            self.trade['total_profit'] = 0
        self.trade['total_exist'] = self.total_exist()
        self.trade['avg_buy_price'] = self.avg_buy_price
        self.trade['total_amount'] += in_trade.amount
        order = {'type': 'Buy', 'USDT': round(in_trade.amount * in_trade.price, 2), 'amount': in_trade.amount,
                 'time': in_trade.time, 'price': in_trade.price}
        self.trade['orders'].append(order)
        return len

    def sell(self, time, amount, price):
        if self.coin_trades_manager.total_exist() == 0:
            return self.coin_trades_manager.sell(time, amount, price)

        total_difference, difference, percentage, start_time = self.coin_trades_manager.sell(time, amount, price)

        if self.trade != {}:
            self.trade['total_profit'] += difference

        a = float(amount) * float(price) + self.total_sell_amount * self.avg_sell_price
        self.total_sell_amount += float(amount)
        self.avg_sell_price = a / self.total_sell_amount
        self.trade['total_exist'] = self.total_exist()
        self.trade['avg_buy_price'] = self.avg_buy_price
        order = {'type': 'Sell', 'USDT': round(float(amount) * float(price), 2), 'amount': amount, 'time': time, 'price': price,
                 'difference': round(difference, 2), 'percentage': percentage}
        if 'orders' not in self.trade:
            print(self.coin_trades_manager.coin_name, time)
        self.trade['orders'].append(order)
        if self.total_exist() == 0:
            self.trade['close_time'] = time
            self.trade['avg_buy_price'] = self.avg_buy_price
            self.trade['avg_sell_price'] = self.avg_sell_price
            self.total_buy_amount = 0
            self.total_sell_amount = 0
            self.avg_buy_price = 0
            self.avg_sell_price = 0
            self.trade.pop('total_exist')
            self.trades.append(self.trade)
            self.trade = {}
        return total_difference, difference, percentage, start_time

    def get_amount(self, time, amount):
        if self.coin_trades_manager.total_exist() == 0:
            return self.coin_trades_manager.get_amount(time, amount)

        avg_price = self.coin_trades_manager.get_amount(time, amount)
        order = {'type': 'Move', 'USDT': round(float(amount) * float(avg_price), 2), 'amount': amount, 'time': time}
        self.trade['orders'].append(order)
        return avg_price

    def total_exist(self):
        total = self.coin_trades_manager.total_exist()
        return total

    def get_trades(self):
        all_trades = []
        all_trades.extend(self.trades)
        if self.trade != {}:
            all_trades.append(self.trade)
        return all_trades

    def print(self):
        if self.coin_trades_manager.total_exist() > 0:
            self.total()
        return self.text