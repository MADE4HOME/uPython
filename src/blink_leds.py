
from fx_timer import FxTimer
from made4home import m4h

update_interval = 500

update_timer = FxTimer()

state = 0

brightness = 10

def setup():
    update_timer.setExpirationTime(update_interval)
    update_timer.updateLastTime()
    m4h.setup()

def loop():
    update_timer.update()
    if update_timer.expired():
        update_timer.updateLastTime()
        update_timer.clear()

        # set the LED with the state of the variable:
        if state == 0:
            m4h.setL1(0, 0, 0)
            m4h.setL2(0, 0, 0)
        
        elif state == 1:
            m4h.setL1(brightness, 0, 0)
            m4h.setL2(brightness, 0, 0)
        
        elif state == 2:
            m4h.setL1(0, brightness, 0)
            m4h.setL2(0, brightness, 0)
        
        elif state == 3:
            m4h.setL1(0, 0, brightness)
            m4h.setL2(0, 0, brightness)
        
        elif state == 4:
            m4h.setL1(brightness, brightness, brightness)
            m4h.setL2(brightness, brightness, brightness)
        
        else:
            m4h.setL1(0, 0, 0)
            m4h.setL2(0, 0, 0)
            state = 0
        
        state += 1

def main():

    setup()

    while True:
        loop()
    
if __name__ == "__main__":
    main()
