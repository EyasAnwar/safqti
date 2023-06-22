class Trade:
    def __init__(self, in_time, in_amount, in_price):
        self.time = in_time
        self.amount = float(in_amount)
        self.exist_amount = float(in_amount)
        self.price = float(in_price)

    def sell(self, sell_amount, sell_price):
        if float(sell_amount) > float(self.exist_amount):
            remaind_amount = round(
                float(sell_amount) - float(self.exist_amount), 8)
            trade_difference = float(
                self.exist_amount) * float(sell_price) - float(self.exist_amount) * float(self.price)
            self.exist_amount = 0
            return self.exist_amount, remaind_amount, trade_difference
        remaind_amount = 0
        trade_difference = float(
            sell_amount) * float(sell_price) - float(sell_amount) * float(self.price)
        self.exist_amount = round(
            float(self.exist_amount) - float(sell_amount), 8)
        if self.exist_amount * self.price < 0.5:
            self.exist_amount = 0
        return self.exist_amount, remaind_amount, trade_difference

    def get_amount(self, amount):
        if float(amount) > float(self.exist_amount):
            remaind_amount = round(float(amount) - float(self.exist_amount), 8)
            self.exist_amount = 0
            return self.exist_amount, remaind_amount
        remaind_amount = 0
        self.exist_amount = round(float(self.exist_amount) - float(amount), 8)
        return self.exist_amount, remaind_amount

    def get_price(self):
        return self.price
