from utils.ResponseMappers import order_mapper


class OrdersRepository:
    def __init__(self, db):
        self.db = db
        self.table_name = 'orders'

    def get_max_ids(self, username):
        sql = 'SELECT symbol, MAX(CAST(id AS INTEGER)) FROM %s WHERE username = \'%s\' GROUP BY symbol;'
        results = self.db.execute_query(sql % self.table_name, username)
        results = {entry['symbol']: entry['max'] for entry in results}
        return results

    def get_orders(self, username):
        orders_sql = 'SELECT symbol, id, orderid, orderlistid, price::REAL, qty::REAL, quoteqty::REAL, commission::REAL, commissionasset, EXTRACT(EPOCH FROM time) * 1000 as time, isbuyer, ismaker, isbestmatch FROM %s WHERE username = \'%s\' ORDER BY time;'

        return self.db.execute_query(orders_sql % self.table_name, username)

    def insert_order(self, username, order):
        order_data = order_mapper(order)
        order_data['username'] = username
        self.db.insert_record(self.table_name, order_data)
