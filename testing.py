from src import test_web_browser, test_video_play
from src import testcase, System_Module

import random
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


TEST_CASE_NUM = 5
def generate_random_sequence(n=TEST_CASE_NUM):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    random_sequence = random.sample(range(1, n + 1), n)
    return random_sequence

def main_testing(device, poco, control, seq, times=-1):
    global logger
    
    logger.info("Main Testing")
    # control.data_on()
    control.wifi_on()
    
    if times == -1:
        logger.warning("Start Ultimate Testing")
    counter = 1
    while True:
        logger.info(f"Testing counter: {counter}")
        
        if seq != None:
            test_seq = seq
        else:
            test_seq = generate_random_sequence()
        
        logger.info(f"Testcase seq = {test_seq}")
        for i in test_seq:
            if i == 1:
                test_web_browser(device, poco, testcase.webBrowser_testcases)
            elif i == 2:
                test_video_play(device, poco, testcase.video_testcases)
            elif i == 3:
                control.airplane_round()
            elif i == 4:
                control.wifi_test_round()
            elif i == 5:
                control.data_test_round()
            else:
                logger.error(f"Testcase idx out of range {i}")


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
    parser.add_argument("--seq", "-s", nargs="+", default=None, help="Testing Sequence")
    args = parser.parse_args()

    devices = args.device
    log_file = args.log
    log_level = int(args.level)
    round = int(args.round)
    
    if args.seq != None:
        seq = [int(x) for x in args.seq]
    else:
        seq = None

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

    system_control = System_Module(now_dev)

    main_testing(now_dev, poco, system_control, seq, round)
