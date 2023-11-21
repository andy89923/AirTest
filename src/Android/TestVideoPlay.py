from airtest.core.api import *
import logging

from .ApplicationName import AndroidApp


def close_yt(device):
    YT_APP = AndroidApp.youtube.value
    
    device.home()
    device.stop_app(YT_APP)
    device.shell(f'am force-stop {YT_APP}')
    
    

def test_video_play(device, poco, testcase, loading_time=5):
    YT_APP = AndroidApp.youtube.value
    
    logger = logging.getLogger('Saviah.VideoTesting')
    logger.info("YT Video Testing")
    
    for url, time in testcase:
        logger.debug(f"Testing on {url}") 
        
        close_yt(device)
        device.shell(f'am start -a android.intent.action.VIEW "{url}"')
        
        # Wait for app to progress
        sleep(loading_time)

        # [BUG] Since Youtube's app bug, have to click the button to have normal UI
        # poco("Navigate up").click()
        # sleep(3)
        # poco("com.google.android.youtube:id/floaty_title").click()

        loading_spin = poco("com.google.android.youtube:id/load_spinner")
        if loading_spin.exists():
            logger.error(f"Lost connection when testing on Video Streaming. {url}")
            sleep(time)
            continue

        # There may be an ads pop out
        ads_skip = poco("com.google.android.youtube:id/skip_ad_button_text")
        if ads_skip.exists():
            logger.debug(f"YT video found ad: {url}") 
            ads_skip.click()
        
        # Video playing time
        sleep(time)
    close_yt(device)
    logger.info("Done")
