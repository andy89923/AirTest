
from airtest.core.api import *
import logging

ENABLE_WAIT_TIME = 10
DISABLE_WAIT_TIME = 10


class System_Module:
    device = None
    logger = None
    
    def __init__(self, device):
        self.device = device
        self.logger = logging.getLogger('Saviah.System')
        
        self.data_off(1)
        self.wifi_off(1)
        self.airplane_off(1)
        
    def wifi_on(self, time=ENABLE_WAIT_TIME):
        self.logger.debug("Set Wi-Fi enable")
        self.device.shell("svc wifi enable")
        sleep(time)
        
    def wifi_off(self, time=DISABLE_WAIT_TIME):
        self.logger.debug("Set Wi-Fi disable")
        self.device.shell("svc wifi disable")
        sleep(time)

    def wifi_test_round(self):
        self.logger.info("Wi-Fi Test Round")
        self.wifi_off()
        self.wifi_on()
        self.logger.info("Done")
        
    def data_on(self, time=ENABLE_WAIT_TIME):
        self.logger.debug("Set Data enable")
        self.device.shell("svc data enable")
        sleep(time)
        
    def data_off(self, time=DISABLE_WAIT_TIME):
        self.logger.debug("Set Data disable")
        self.device.shell("svc data disable")
        sleep(time)
        
    def data_test_round(self):
        self.logger.info("Data Test Round")
        self.data_off()
        self.data_on()
        self.logger.info("Done")
        
    def airplane_on(self, time=ENABLE_WAIT_TIME):
        self.logger.debug("Airplane mode enable")
        self.device.shell("settings put global airplane_mode_on 1")
        sleep(time)
        
    def airplane_off(self, time=DISABLE_WAIT_TIME):
        self.logger.debug("Airplane mode disable")
        self.device.shell("settings put global airplane_mode_on 0")
        sleep(time)
        
    def airplane_round(self):
        self.logger.info("Airplane Test Round")
        self.airplane_on()
        self.airplane_off()
        self.logger.info("Done")





if __name__ == "__main__":
    device = connect_device("android://")
    control = System_Module(device)
    
    control.wifi_test_round()
    
    
    
    
    