import calendar
import time
from datetime import datetime as dt


def withdrawal_mapper(rec):
    insertTime = calendar.timegm(time.strptime(
        rec['applyTime'], '%Y-%m-%d %H:%M:%S'))
    insertTime = insertTime * 1000
    insertTime = str(dt.fromtimestamp(insertTime/1000))
    r = {'time': insertTime, 'source': rec['address'],
         'amount': rec['amount'], 'asset': rec['coin'], 'type': 'withdraw'}

    return r


def deposit_mapper(rec):
    insertTime = str(dt.fromtimestamp(rec['insertTime']/1000))
    r = {'time': insertTime, 'source': rec['address'],
         'amount': rec['amount'], 'asset': rec['coin'], 'type': 'deposit'}

    return r


def payment_mapper(pay):
    insertTime = str(dt.fromtimestamp(pay['transactionTime']/1000))
    r = {
        'time': insertTime,
        'source': pay['receiverInfo']['accountId'] if float(pay['amount']) < 0 else pay['receiverInfo']['accountId'],
        'amount': abs(float(pay['amount'])),
        'asset': pay['currency'],
        'type': 'withdraw_pay' if float(pay['amount']) < 0 else 'deposit_pay'}

    return r


def order_mapper(order):
    order_data = order.copy()
    order_data['isBuyer'] = 'Y' if order_data['isBuyer'] == 'True' else 'N'
    order_data['isMaker'] = 'Y' if order_data['isMaker'] == 'True' else 'N'
    order_data['isBestMatch'] = 'Y' if order_data['isBestMatch'] == 'True' else 'N'
    order_data['time'] = str(
        dt.fromtimestamp(order_data['time']/1000))[:-3]
    return order_data
