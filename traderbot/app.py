#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

from traderbot.logger import initialize_logger
from traderbot.traderbotlib import *

# Initialize the logger
lg = initialize_logger()


# Check trading account status
def check_account_status():
    try:
        pass
    except Exception as e:
        lg.error("Could not get account status")
        lg.info(str(e))
        sys.exit(1)


# Close current orders
def close_open_orders():
    open_orders = []
    lg.info(f"List of open orders: {open_orders}")

    for order in open_orders:
        # close the order
        lg.info(f"Closed order: {order.id}")

    lg.info("Closing orders completed.")


def get_ticker():
    ticker = input("Enter ticker symbol: ").strip().upper()
    lg.info(f"Ticker symbol: {ticker}")

    return ticker


def main():
    check_account_status()
    close_open_orders()

    ticker = get_ticker()

    print(f"Working with ticker: {ticker}")


if __name__ == "__main__":
    main()
