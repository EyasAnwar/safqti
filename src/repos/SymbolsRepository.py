
import time


class SymbolsRepository:

    def __init__(self, db) -> None:
        self.db = db
        self.symbols = []
        self.table_name = 'symbols'

    def get_symbols(self):
        if not self.symbols:
            self.symbols = self.db.get_records(self.table_name)
        return self.symbols

    def get_symbol_info(self, symbol):
        # Return from catch if exist
        if any(m['symbol'] == symbol for m in self.get_symbols()):
            return next(item for item in self.get_symbols() if item["symbol"] == symbol)
        symbol_info = None
        # Fetch from Binance and make up to 10 trials
        trials = 10
        while trials > 0:
            try:
                if not any(m['symbol'] == symbol for m in self.get_symbols()):
                    info = self.client.get_symbol_info(symbol)
                    ticker = {
                        'symbol': info['symbol'],
                        'baseasset': info['baseasset'],
                        'quoteasset': info['quoteasset']
                    }
                    self.db.insert_record(self.table_name, ticker)
                    self.symbols.append(info)
                symbol_info = next(
                    item for item in self.get_symbols() if item["symbol"] == symbol)
                break
            except Exception as e:
                print(e)
                trials = trials - 1
                time.sleep(1)
        return symbol_info
