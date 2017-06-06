#!/usr/bin/env python

import sys
import config

import yahoo_finance 
import pymysql

def print_err_and_exit():
    print("Usage: password")
    sys.exit(-1)

def get_connection(passwd):
    connection = pymysql.connect(host=config.RDS_ENDPOINT,
                                 user=config.USERNAME,
                                 db=config.DB,
                                 password=passwd)
    return connection

if __name__ == '__main__':
    if len(sys.argv) <  2:      
        print_err_and_exit()
      

    conn = get_connection(sys.argv[1])

    sql = "replace into daily_price (symbol, trade_date, open_price, close_price) values (%s, %s, %s, %s)"

    for symbol in config.SYMBOL_LIST:
        with conn.cursor() as cursor:
            s = yahoo_finance.Share(symbol)
            opt = [] 
            opt.append(symbol)
            opt.append(s.get_trade_datetime())
            opt.append(s.get_open())
            opt.append(s.get_price())
    
            cursor.execute(sql, opt)
            conn.commit()
  
