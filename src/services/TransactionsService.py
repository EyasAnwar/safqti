import os
import time
import calendar
from datetime import datetime as dt
from dotenv import load_dotenv
from tqdm import tqdm

from binance.client import Client
from repos.TransactionsRepository import TransactionsRepository
from utils.DatabaseManager import DatabaseManager


class TransactionsService:
    def __init__(self, client, db, username):
        self.username = username
        self.client = client
        self.db = db
        self.transactionsRepo = TransactionsRepository(db)

    def fetchWithdrawals(self, client, start_time, end_time):
        withdrawals = []
        withdrawals = self.client.get_withdraw_history(
            startTime=start_time, endTime=end_time)
        return withdrawals

    def fetchDeposits(self, client, start_time, end_time):
        deposits = []
        deposits = self.client.get_deposit_history(
            startTime=start_time, endTime=end_time)
        return deposits

    def fetchPayments(self, client, start_time, end_time):
        # The endpoint limits the interval up to 18 months ago.
        if start_time < int((time.time() - 18 * 30 * 24 * 60 * 60) * 1000):
            return []
        pays = self.client.get_pay_trade_history(
            startTime=start_time, endTime=end_time)
        if len(pays['data']) == 0:
            return []
        return pays['data']

    def iterate(self, start, stop, step, fn):
        start = calendar.timegm(time.strptime(
            start, '%Y-%m-%d %H:%M:%S'))
        start = start * 1000
        for istart in tqdm(range(start, stop, step)):
            fn(self.client, istart, istart + step)

    def fetch_and_insert(self, client, start, stop):
        withdrawals = self.fetchWithdrawals(client, start, stop)
        self.transactionsRepo.insert_withdrawals(self.username, withdrawals)
        deposits = self.fetchDeposits(client, start, stop)
        self.transactionsRepo.insert_deposits(self.username, deposits)
        payments = self.fetchPayments(client, start, stop)
        self.transactionsRepo.insert_payments(self.username, payments)

    def process(self, start_time):
        current_time = int(time.time()*1000)
        # Three Months Interval
        interval = 1000 * 60 * 60 * 24 * 30 * 3
        self.iterate(start_time, current_time, interval, self.fetch_and_insert)
