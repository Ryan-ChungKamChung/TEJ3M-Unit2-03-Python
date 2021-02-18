#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in February 2021
# Cycles RGB colours


import board
import digitalio
import time

import constants


def main():
    # Loops RGB from the LED

    led = digitalio.DigitalInOut(board.D13)
    led.direction = digitalio.Direction.OUTPUT

    while True:
        # Red
        led.value = True
        time.sleep(constants.BLINK_TIME)
        led.value = False
        time.sleep(constants.DELAY_TIME)


if __name__ == "__main__":
    main()
