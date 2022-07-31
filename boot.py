import time
import network
from settings import wifi_ssid, wifi_password
import upip

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect(wifi_ssid, wifi_password)
sta_if.ifconfig()
x = 0
while not sta_if.isconnected() and x < 10:
    print("Connecting.......")
    x += 1
    time.sleep(1)

if sta_if.isconnected():
    print("Internet Connected")
else:
    print("Connection failed")

upip.install("micropython-umqtt.simple")