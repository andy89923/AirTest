# -*- encoding=utf8 -*-
# __author__ = "chenthungfang"

from airtest.core.api import *

devices = ["android://127.0.0.1:5037/3dc31914?cap_method=MINICAP&touch_method=MAXTOUCH&"]



print("start...")

connect_device(devices[0])
dev = device()

def check_wifi_state(dev):
    result = dev.shell('dumpsys wifi')
    states = []
    for line in result.split('\n'):
        if line.count('curState'):
            state = line.split('=')[1]
            states.append(state)
    if "ConnectedState" in states:
        return True
    return False


def connect_wifi(dev, ssid, password="", password_type='wpa2'):
    dev.shell(f'cmd -w wifi connect-network {ssid} {password_type} {password}')
    timeout = 10
    while timeout > 0:
        sleep(1)
        timeout -= 1
        if check_wifi_state(dev):
            log("Wi-Fi is connected successfully")
            return True
    log("Wi-Fi connect timeout")
    return False


WIFI_SSID = 'cslab'
WIFI_PASS = 'wirelab020'
WIFI_PASS_TYPE = 'wpa2'

def test_wifi_connection():
    shell("svc wifi disable")
    shell("svc data disable")
    sleep(3)
    shell("svc wifi enable")
    shell("svc data enable")
    connect_wifi(dev, WIFI_SSID, WIFI_PASS, WIFI_PASS_TYPE)
    print(check_wifi_state(dev))
    

# test_wifi_connection()

# from airtest.utils.logger import get_logger


        
# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)