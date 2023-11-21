from airtest.core.api import *
import logging

from .ApplicationName import AndroidApp

def close_all_tabs(device, poco):
    logger = logging.getLogger('Saviah.WebTesting')
    logger.debug("Close all tabs")

    CHROME_APP = AndroidApp.chrome.value
    device.home()
    device.start_app(CHROME_APP)
    
    poco(f"{CHROME_APP}:id/tab_switcher_button").click()
    poco(f"{CHROME_APP}:id/menu_button").click()
    poco(text="Close all tabs").click()
    poco(f"{CHROME_APP}:id/positive_button").click()
    device.home()

def test_web_browser(device, poco, testcases):
    CHROME_APP = AndroidApp.chrome.value

    logger = logging.getLogger('Saviah.WebTesting')
    logger.info("WebBrowserTesting")
    
    device.shell(f'am force-stop {CHROME_APP}')    
    try:
        close_all_tabs(device, poco)
    except Exception as e:
        logger.error(f'Cannot close web browser tabs.', exc_info=True)

    for url, target in testcases.items():
        logger.debug(f"Testing on {url}") 
        device.shell(f'am start -a android.intent.action.VIEW -d {url}')
        sleep(2)
        # wait(target, timeout=5, intervalfunc=not_found_error)
        try:
            assert_exists(target, "Target not exist")
            logger.debug("Pass")
        except Exception as e:
            logger.error(f"Can't found target template on {url}", exc_info=True)
        device.home()
    logger.info("Done")

