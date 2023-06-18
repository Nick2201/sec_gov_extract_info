import sys,os
sys.path.insert(0, os.getcwd())
from primary_sec.utils.drivers.driver_gecko import driver_func
def selenium_open(site_link: str) -> None:
    connect = driver_func().get("https://www.google.com/search?q=poetry+scripts&oq=poetry+scripts&aqs=chrome.0.69i59j69i64j69i59j35i39j0i512l4.2574j0j1&sourceid=chrome&ie=UTF-8").pa
    print(connect.page_source)
