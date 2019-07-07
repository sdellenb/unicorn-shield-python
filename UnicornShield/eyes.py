import unicornshield as unicorn
import time

while True:
    print(unicorn.nose())
    if unicorn.nose() < 0.25:
        unicorn.leftEyeOn()
        unicorn.rightEyeOn()
    else:
        unicorn.leftEyeOff()
        unicorn.rightEyeOff()

    time.sleep(0.5)
