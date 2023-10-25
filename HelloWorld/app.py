# -*- encoding=utf8 -*-
# __author__ = "chenthungfang"

from airtest.core.api import *

devices = ["android://127.0.0.1:5037/3dc31914?cap_method=MINICAP&touch_method=MAXTOUCH&"]


print("start...")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device(devices[0])
dev = device()

def not_found_error():
    print("Not found error")

def test_web_url(dev, url="free5gc.org"):
    CHROME_APP = 'com.android.chrome'
    dev.home()
    dev.start_app(CHROME_APP)
    
    poco("com.android.chrome:id/home_button").click()
    poco("com.android.chrome:id/url_bar").click()
    
    dev.text(f"{url}")

    wait(Template(r"./../src/free5GC_logo.png", threshold=0.5), timeout=5, interval=1, intervalfunc=not_found_error)
    
    dev.home()
    

times = 1
for _ in range(times):
    test_web_url(dev, 'free5gc.org')
    sleep(1)
