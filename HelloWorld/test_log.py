# -*- encoding=utf8 -*-
import logging

__author__ = "Airtest"

logger = logging.getLogger("airtest")
logger.setLevel(logging.WARNING)

__author__ = "chenthungfang"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=None, devices=["android://127.0.0.1:5037/3dc31914?cap_method=MINICAP&touch_method=MAXTOUCH&",])

    

# script content
print("start...")


logger.info("123")

sleep(1)

logger.warning("war123")
logger.warning("war456")

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=None)