#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class TraderBot:
    ticker: str
    lg: logging.Logger = field(default_factory=lambda: logging.getLogger(__name__))

    def __post_init__(self):
        self.lg.info(f"TraderBot initialized for ticker: {self.ticker}")

    def run(self):
        pass


# INITIAL CHECKS
# TODO: Check the position
# TODO: Check if tradable

# GENERAL TREND ANALYSIS
# TODO: Load 30-min candles
# TODO: Perform general trend analysis

# LOOP
# TODO: Load 5-min candles
# TODO: Perform instant trend analysis
# TODO: Perform RSI analysis
# TODO: Perform stochastic analysis

# SUBMIT ORDER
# TODO: Submit order
# TODO: Check position

# "ENTER POSITION" MODE
# TODO: Check take profit
# TODO: Check stop loss
# TODO: Check stochastic crossing

# "EXIT POSITION" MODE
# TODO: Check order
# TODO: Check position

# PAUSE
# TODO: Wait 15-min
# TODO: Back to beggining

if __name__ == "__main__":
    pass
