from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

# Number of times to press the keys (set to None for infinite loop)
repetitions = None  # or set to None

# Delay between key presses
delay = 1.0  # in seconds

try:
    count = 0
    while repetitions is None or count < repetitions:
        keyboard.press(Key.up)
        keyboard.release(Key.up)
        print("Pressed UP")
        time.sleep(delay)

        keyboard.press(Key.down)
        keyboard.release(Key.down)
        print("Pressed DOWN")
        time.sleep(delay)

        count += 1
except KeyboardInterrupt:
    print("Stopped by user")
