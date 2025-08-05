#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
from logging.handlers import TimedRotatingFileHandler

base_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.join(base_dir, "logs")
os.makedirs(log_dir, exist_ok=True)

log_name = os.path.join(log_dir, "traderbot.log")  # Base log file name

# Set up logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Remove existing handlers to avoid duplicate logs (important when re-running)
logger.handlers.clear()

# TimedRotatingFileHandler: rotates logs at midnight; keeps last 7 days' logs
handler = TimedRotatingFileHandler(log_name, when="midnight", interval=1, backupCount=7)
handler.suffix = "%Y-%m-%d"  # Date suffix for rotated logs (e.g., app.log.2024-08-05)
handler.setFormatter(
    logging.Formatter(
        fmt="%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
)

logger.addHandler(handler)
logger.addHandler(logging.StreamHandler())  # Also outputs to console

# Example usage:
# logger.info("This is an info message.")
# lg.debug("This is a debug message.")
# lg.warning("This is a warning message.")
# lg.error("This is a error message.")
# lg.critical("This is a critical message.")
