
import db


class DataProvider():
    def __init__(self):
        self.conn = db.get_connection("harbin73") 

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
        

if __name__ == '__main__':
    p = DataProvider()
    print(p.getCurrentPosition())
