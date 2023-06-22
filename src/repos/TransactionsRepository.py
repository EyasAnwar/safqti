from utils.ResponseMappers import deposit_mapper, withdrawal_mapper, payment_mapper


class TransactionsRepository:
    def __init__(self, db):
        self.db = db
        self.table_name = 'transactions'

    def insert_withdrawals(self, username, withdrawals):
        for rec in withdrawals:
            r = withdrawal_mapper(rec)
            r['username'] = username
            self.db.insert_record(self.table_name, r)

    def insert_deposits(self, username, deposits):
        for rec in deposits:
            r = deposit_mapper(rec)
            r['username'] = username
            self.db.insert_record(self.table_name, r)

    def insert_payments(self, username, payments):
        for pay in payments:
            r = payment_mapper(pay)
            r['username'] = username
            self.db.insert_record(self.table_name, r)
