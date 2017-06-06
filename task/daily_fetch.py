#!/usr/bin/env python

import sys
import logging

import config

import yahoo_finance 
import pymysql

def print_err_and_exit():
    print("Usage: password")
    sys.exit(-1)

def get_logger():
    logger = logging.getLogger("daily_fetch")
    logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)


    logger.addHandler(ch)

    return logger
 

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
    logger = get_logger()

    sql = "replace into daily_price (symbol, trade_date, open_price, close_price) values (%s, %s, %s, %s)"

    for symbol in config.SYMBOL_LIST:
        with conn.cursor() as cursor:
            logger.info("fetching " + symbol)
            s = yahoo_finance.Share(symbol)
            opt = [] 
            opt.append(symbol)
            opt.append(s.get_trade_datetime()[0:10])
            opt.append(s.get_open())
            opt.append(s.get_price())
            logger.info(opt)
    
            cursor.execute(sql, opt)
            conn.commit()
  
