
import time
import tqdm
from TradesModule import TradesModule
from repos.OrdersRepository import OrdersRepository


class OrdersService:

    def __init__(self, client, db, symbolsRepo, username) -> None:
        self.ordersRepo = OrdersRepository(db)
        self.trades_module = TradesModule()
        self.symbolsRepo = symbolsRepo
        self.username = username
        self.client = client
        self.db = db

    def fetch_orders(self, ticker, max_ids):
        if ticker['symbol'] in max_ids.keys():
            info = self.client.get_my_trades(
                symbol=ticker['symbol'], fromId=int(max_ids[ticker['symbol']]) + 1)
        else:
            info = self.client.get_my_trades(
                symbol=ticker['symbol'], limit=1000)
        return info

    def fetch_all(self):
        """Fetch all orders from Binance and insert it to the database
        Note: This method may take long time
        """
        max_ids = self.ordersRepo.get_max_ids(self.username)
        tickers = self.client.get_all_tickers()  # TODO Add unlisted symbols

        f = open('../fetched-symbols.txt', 'r')

        fetched_symbols = f.readlines()
        fetched_symbols = list(
            map(lambda s: s.replace('\n', ''), fetched_symbols))

        f = open('../fetched-symbols.txt', 'a')
        for ticker in tqdm(tickers):
            if ticker['symbol'] in fetched_symbols:
                continue
            orders = self.fetch_orders(ticker, max_ids)
            for i in orders:
                self.ordersRepo.insert_order(self.username, i)
            f.write(ticker['symbol'])
            f.write('\n')
            f.flush()
            time.sleep(0.2)

    def process_orders(self, trades):
        i = 1
        for trade in trades:
            # print(i, trade)
            i += 1

            symbol_info = self.symbolsRepo.get_symbol_info(trade['symbol'])

            if symbol_info['quoteasset'] != 'USDT':
                if trade['isbuyer'] == 'Y':
                    self.trades_module.swap(trade['time'], symbol_info['quoteasset'],
                                            symbol_info['baseasset'], trade['quoteqty'], trade['qty'])
                else:
                    self.trades_module.swap(trade['time'], symbol_info['baseasset'],
                                            symbol_info['quoteasset'], trade['qty'], trade['quoteqty'])
                self.trades_module.commission(
                    trade['time'], trade['commission'], trade['commissionasset'])
                continue
            if trade['isbuyer'] == 'Y':
                self.trades_module.buy(
                    symbol_info['baseasset'], trade['time'], trade['qty'], trade['price'])
            else:
                self.trades_module.sell(
                    symbol_info['baseasset'], trade['time'], trade['qty'], trade['price'])
            # Fees
            self.trades_module.commission(
                trade['time'], trade['commission'], trade['commissionasset'])

    def generate_report(self):
        orders = self.ordersRepo.get_orders(self.username)
        self.process_orders(orders)
        return self.trades_module.extract_trades()
