from datetime import datetime as dt
import argparse
import pickle
import os


from TradesModule import TradesModule
from dotenv import load_dotenv
import psycopg
from tqdm import tqdm
from repos.OrdersRepository import OrdersRepository
from services.OrdersService import OrdersService
from services.TransactionsService import TransactionsService
from utils.DatabaseManager import DatabaseManager

from binance.client import Client


def print_open_trades(trades_module):
    for manager in trades_module.coin_managers.keys():
        m = trades_module.coin_managers[manager].coin_trades_manager
        if len(m.trades_stack) > 0:
            qty_usdt = round(m.total_exist() * m.avg_buy_price(), 1)
            if qty_usdt > 10:  # Ignore small balances
                print(m.trades_stack[0].time, manager,
                      m.total_exist(), m.avg_buy_price(), qty_usdt)


def cache_results(api_key, all_trades):
    with open(os.path.join('cache', api_key, 'all_trades.pkl'), 'wb') as output:
        pickle.dump(all_trades, output, pickle.HIGHEST_PROTOCOL)


def init_cache(api_key):
    if not os.path.exists(os.path.join('cache', api_key)):
        os.makedirs(os.path.join('cache', api_key))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Summarize your Binance account trades.')
    parser.add_argument('--fetch_orders_history', action=argparse.BooleanOptionalAction,
                        help='Fetch Orders History')
    parser.add_argument('--generate_trades_report', action=argparse.BooleanOptionalAction,
                        help='Generate Trades Report')
    parser.add_argument('--fetch_transactions_history', action=argparse.BooleanOptionalAction,
                        help='Fetch Transactions History')

    args = parser.parse_args()
    print(args)

    start_time = dt.now()

    load_dotenv()
    username = os.environ.get('BINANCE_USERNAME')
    api_key = os.environ.get('API_KEY')
    secret_key = os.environ.get('API_SECRET')

    client = Client(api_key, secret_key)
    db = DatabaseManager.instance()
    db.connect()

    init_cache(api_key)

    if args.fetch_orders_history:
        # ############ Fetch Orders History ####################
        ordersService = OrdersService(client, db, username)
        ordersService.fetch_all()
        # #######################################################

    if args.generate_trades_report:
        # ############ Calculate Orders  ########################
        all_trades = ordersService.generate_report()
        cache_results(api_key, all_trades)
        end_time = dt.now()
        duration = end_time - start_time
        print(duration)
        print(ordersService.trades_module.coin_managers)
        # Print Open trades
        print_open_trades(ordersService.trades_module)
        # #######################################################

    if args.fetch_transactions_history:
        transactionService = TransactionsService(client, db, username)
        start_time = '2019-06-08 00:00:00'

        transactionService.process(start_time)
