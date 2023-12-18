# Complete project details at https://RandomNerdTutorials.com

import time

from made4home import m4h, PIN_RELAY_1, PIN_IN_1, PIN_RELAY_2, PIN_IN_2, PIN_RELAY_3, PIN_IN_3, PIN_RELAY_4, PIN_IN_4
from fx_timer import FxTimer

update_interval = 1

update_timer = FxTimer()

mqtt_client = None

opto_inputs_msg = ""

def sub_cb(topic, msg):

    print((topic, msg))

    if topic == output_1_topic and msg == state_on:
        m4h.digitalWrite(PIN_RELAY_1, 1)

    elif topic == output_1_topic and msg == state_off:
        m4h.digitalWrite(PIN_RELAY_1, 0)

    elif topic == output_2_topic and msg == state_on:
        m4h.digitalWrite(PIN_RELAY_2, 1)

    elif topic == output_2_topic and msg == state_off:
        m4h.digitalWrite(PIN_RELAY_2, 0)

    elif topic == output_3_topic and msg == state_on:
        m4h.digitalWrite(PIN_RELAY_3, 1)

    elif topic == output_3_topic and msg == state_off:
        m4h.digitalWrite(PIN_RELAY_3, 0)

    elif topic == output_4_topic and msg == state_on:
        m4h.digitalWrite(PIN_RELAY_4, 1)

    elif topic == output_4_topic and msg == state_off:
        m4h.digitalWrite(PIN_RELAY_4, 0)

def connect_and_subscribe():
    global mqtt_client

    mqtt_client = MQTTClient(client_id, mqtt_server)
    mqtt_client.set_callback(sub_cb)
    mqtt_client.connect()
    mqtt_client.subscribe(outputs_topic)
    
    print('Connected to %s MQTT broker, subscribed to %s topic' % (mqtt_server, outputs_topic))
    
    return mqtt_client

def restart_and_reconnect():
    print('Failed to connect to MQTT broker. Reconnecting...')
    time.sleep(10)
    machine.reset()

def setup():
    global m4h, update_timer, mqtt_client

    m4h.setup()

    update_timer.setExpirationTime(update_interval)
    update_timer.updateLastTime()

    try:
        mqtt_client = connect_and_subscribe()
    except OSError as e:
        restart_and_reconnect()

        try:
            mqtt_client.publish(greetings_topic, "Hi, I'm MADE4HOME ^^")
            mqtt_client.check_msg()
        except OSError as e:
            pass

def loop():
    global mqtt_client, update_timer

    try:
        mqtt_client.check_msg()
    except OSError as e:
        restart_and_reconnect()

    update_timer.update()
    if update_timer.expired():
        update_timer.updateLastTime()
        update_timer.clear()

        try:
            opto_inputs_msg = "["
            opto_inputs_msg += str(m4h.digitalRead(PIN_IN_1) == 0) + ", "
            opto_inputs_msg += str(m4h.digitalRead(PIN_IN_2) == 0) + ", "
            opto_inputs_msg += str(m4h.digitalRead(PIN_IN_3) == 0) + ", "
            opto_inputs_msg += str(m4h.digitalRead(PIN_IN_4) == 0)
            opto_inputs_msg += "]"
            mqtt_client.publish(inputs_topic, opto_inputs_msg)
        except OSError as e:
            pass

def main():

    setup()

    while True:
        loop()
    
if __name__ == "__main__":
    main()
