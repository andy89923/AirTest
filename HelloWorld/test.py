# -*- encoding=utf8 -*-
__author__ = "chenthungfang"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, 
               logdir="/Users/chenthungfang/Desktop/test_log", 
               devices=["android://127.0.0.1:5037/3dc31914?cap_method=MINICAP&touch_method=MAXTOUCH&",]
              )

print("start...")


# start_app('com.google.android.calendar')
# text("test input")

def connect_wifi(ssid, password="", password_type='wpa2'):
    shell(f'cmd -w wifi connect-network {ssid} {password_type} {password}')


shell("svc wifi disable")
shell("svc data disable")

sleep(3)

shell("svc wifi enable")
shell("svc data enable")

WIFI_SSID = 'cslab'
WIFI_PASS = 'wirelab020'
WIFI_PASS_TYPE = 'wpa2'

connect_wifi(WIFI_SSID, WIFI_PASS, WIFI_PASS_TYPE)

print(shell("ping -c1 8.8.8.8"))

# print(shell("dumpsys wifi"))

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath="./test_log")