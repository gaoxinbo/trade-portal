#!/usr/bin/env python

# coding=utf8
from yahoo_finance import Share

s = Share("FB")
s.refresh()

print("open " + s.get_open())
print("close " + s.get_price())
print("date " + s.get_trade_datetime())

