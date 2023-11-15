from src import test_web_browser, test_video_play
from src import testcase

import sys
import argparse

from MyLogging import ColoredFormatter
import logging

from airtest.core.api import *

logger = None
def init_logger(log_file, level):
    global logger

    airtest_logger = logging.getLogger('airtest')
    airtest_logger.setLevel(logging.WARNING)
    airtest_logger.propagate = False

    logger = logging.getLogger('Saviah')
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(ColoredFormatter("%(levelname)s: %(message)s"))
    logger.addHandler(console_handler)

    if log_file != None:
        logging.basicConfig(
            filename=log_file, 
            filemode='a',
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger.debug(f'Log file: {log_file}')



def main_testing(device, poco, times=-1):
    global logger
    
    logger.info("Main Testing")
    
    if times == -1:
        logger.warning("Start Ultimate Testing")
    counter = 1
    while True:
        logger.info(f"Testing counter: {counter}")
        
        
        logger.debug("WebBrowserTesting")
        test_web_browser(device, poco, testcase.webBrowser_testcases)
        
        logger.debug("YT Video Testing")
        test_video_play(device, poco, testcase.video_testcases)

        logger.info(f"End of testing round {counter}.")
        if counter == times:
            break
        counter += 1

    logger.info("End of Testing")


USAGE_INFO = "[Saviah_UX_Testing]\n"
USAGE_INFO += "[USAGE] testing.py [-h] [--log LOG] [--device DEVICE [DEVICE ...]]"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=USAGE_INFO)

    parser.add_argument("--device", nargs="+", help="Connected Device")
    parser.add_argument("--log", "-l", default=None, help="Log file")
    parser.add_argument("--level", default=logging.INFO, help="Log Level")
    parser.add_argument("--round", "-r", default=10, help="Testing Round")
    args = parser.parse_args()

    devices = args.device
    log_file = args.log
    log_level = int(args.level)
    round = int(args.round)

    init_logger(log_file, log_level)
    logger.info('Start Saviah UX Testing')
    
    if devices == None:
        logger.error(USAGE_INFO)
        exit(1)
        
    logger.info(f'Number of Devices: {len(devices)}')
    if len(devices) > 1:
        logger.warning("Only support one devices(ver 0.1)")

    try:
        logger.debug(f'Connecting to device {devices[0]}')
        now_dev = connect_device(devices[0])
        logger.debug('Connected!')
    except Exception as e:
        logger.error(f'Cannot connect to {devices[0]}', exc_info=True)
        exit(1)
    
    from poco.drivers.android.uiautomation import AndroidUiautomationPoco
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

    main_testing(now_dev, poco, round)
