import unicornshield as unicorn
import time

while True:
    if unicorn.buttonPressed():
        unicorn.rightEyeOn()
        unicorn.leftEyeOff()
    else:
        unicorn.leftEyeOn()
        unicorn.rightEyeOff()

    time.sleep(0.1)
