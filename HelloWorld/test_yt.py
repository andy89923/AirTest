from airtest.core.api import *

devices = ["android://127.0.0.1:5037/3dc31914?cap_method=MINICAP&touch_method=MAXTOUCH&"]


print("start...")
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

connect_device(devices[0])
dev = device()


def test_youtube(dev):
    dev.home()
    dev.stop_app("com.google.android.youtube")

    dev.shell('am start -a android.intent.action.VIEW "http://www.youtube.com/watch?v=934WINmgSm8"')
    
    # Wait for app to progress
    sleep(3)

    # [BUG] Since Youtube's app bug, have to click the button to have normal UI
    poco("Navigate up").click()
    sleep(3)
    poco("com.google.android.youtube:id/floaty_title").click()

    # There may be an ads pop out
    ads_skip = poco("com.google.android.youtube:id/skip_ad_button_text")
    if ads_skip.exists():
        ads_skip.click()
    
    # Video playing time
    sleep(10)


times = 10
for _ in range(times):
    test_youtube(dev)
    sleep(5)

