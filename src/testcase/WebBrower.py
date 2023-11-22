
from airtest.core.cv import Template


webBrowser_testcases = {
    # url                 : specific pattern
    "https://free5gc.org" : Template(r"./src/testcase/img/free5GC_logo.png", threshold=0.4),
    "https://www.saviah.com/en" : Template(f"./src/testcase/img/saviah.png", threshold=0.4),
    "https://tw.yahoo.com/" : Template(f"./src/testcase/img/yahoo.png", threshold=0.4),
}