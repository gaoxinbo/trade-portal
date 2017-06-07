
import db


class DataProvider():
    def __init__(self):
        self.conn = db.get_connection("840326") 

    def getCurrentPosition(self):
        sql = "select symbol, position, avg_cost, currency from position"
        d = [] 
        with self.conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            for item in result: 
                r = {}
                r['symbol'] = item[0]
                r['position'] = item[1]
                r['avg_cost'] = item[2]
                r['currency'] = item[3]
                d.append(r)
            
        return d
        
    def getPortion(self):
        position = self.getCurrentPosition();
        portion = []
        for item in position:
            symbol = item['symbol']
            price = self.getCurrentClosePrice(symbol)
            if not price:
                continue

            d = {} 
            d['symbol'] = symbol
            d['value'] = float(price['close']) * float(item['position'])
            portion.append(d)

        return portion


    def getCurrentClosePrice(self, symbol):
        sql = "select close_price from daily_price where symbol = %s order by trade_date desc limit 1"  
        d = {}
        with self.conn.cursor() as cursor:
            cursor.execute(sql, symbol)    
            item = cursor.fetchone()
            if not item:      
                return None


            d['close'] = item[0]
        return d


        
if __name__ == '__main__':
    p = DataProvider()
    print(p.getPortion())
