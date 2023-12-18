# Complete project details at https://RandomNerdTutorials.com

import time
from umqttsimple import MQTTClient
import ubinascii
import machine
import micropython
import network
import esp
esp.osdebug(None)
import gc
gc.collect()

ssid = 'REPLACE_WITH_YOUR_SSID'
password = 'REPLACE_WITH_YOUR_PASSWORD'
mqtt_server = 'home.iot.loc'

client_id = ubinascii.hexlify(machine.unique_id())

outputs_topic = b'made4home/output/#'
inputs_topic = b'made4home/inputs'
greetings_topic = b'made4home/greetings'
output_1_topic = b'made4home/output/1'
output_2_topic = b'made4home/output/2'
output_3_topic = b'made4home/output/3'
output_4_topic = b'made4home/output/4'
state_on = b'on'
state_off = b'off'

last_message = 0
message_interval = 5
counter = 0

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

