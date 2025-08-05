#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging as lg

# DEBUG, INFO, WARNING, ERROR, CRITICAL
lg.basicConfig(
    level=lg.DEBUG,
    filename="traderbot.log",
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# lg.info("This is a info message.")
# lg.debug("This is a debug message.")
# lg.warning("This is a warning message.")
# lg.error("This is a error message.")
# lg.critical("This is a critical message.")
