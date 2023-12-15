
from made4home import m4h, PIN_RELAY_1, PIN_IN_1, PIN_RELAY_2, PIN_IN_2, PIN_RELAY_3, PIN_IN_3, PIN_RELAY_4, PIN_IN_4

def setup():
    m4h.setup()

def loop():
    # Update the output states via input states.
    m4h.digitalWrite(PIN_RELAY_1, (0 == m4h.digitalRead(PIN_IN_1)))
    m4h.digitalWrite(PIN_RELAY_2, (0 == m4h.digitalRead(PIN_IN_2)))
    m4h.digitalWrite(PIN_RELAY_3, (0 == m4h.digitalRead(PIN_IN_3)))
    m4h.digitalWrite(PIN_RELAY_4, (0 == m4h.digitalRead(PIN_IN_4)))

def main():

    setup()

    while True:
        loop()
    
if __name__ == "__main__":
    main()
