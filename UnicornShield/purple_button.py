import unicornshield as unicorn
import time
import atexit

unicorn.brightness(0.3) # Only 30% power.


@atexit.register
def turnoff():
    unicorn.clear()

unicorn.setAll(255, 0, 255)
unicorn.show()
leuchtet = True

while True:
    if unicorn.buttonPressed():
        if leuchtet:
            unicorn.clear()
            print("LEDs aus")
            time.sleep(1.5)
        else:
            unicorn.setAll(255, 0, 255)
            unicorn.show()
            print("LEDs an")
            time.sleep(1.5)
        leuchtet = not leuchtet

    time.sleep(0.5)
