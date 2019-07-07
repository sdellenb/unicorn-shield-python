import unicornshield as unicorn
import time
import atexit

colors = [
    [255, 255, 255], # White
    [  0,   0, 255], # Blue
    [255, 127,   0], # Orange
    [  0, 255, 127], # Cyan
    [  0, 255,   0], # Green
    [255, 255,   0], # Yellow
    [255,   0,   0], # Red
    [255,   0, 255], # Purple
    [  0,   0,   0], # Black / Off
]

# Initial State
color_index = -1
unicorn.setAll(
    colors[color_index][0],
    colors[color_index][1],
    colors[color_index][2]
)
next_color_index = color_index + 1
unicorn.brightness(0.3) # Only 30% power.


@atexit.register
def turnoff():
    unicorn.clear()


while True:
    if unicorn.buttonPressed():
        if color_index != next_color_index:
            print("Cycling color!")
            unicorn.setAll(
                colors[color_index][0],
                colors[color_index][1],
                colors[color_index][2]
            )
            unicorn.show()
            color_index = next_color_index
    elif color_index == next_color_index:
        next_color_index = (color_index + 1) % len(colors)

    time.sleep(0.1)
