# Example for turning on yellow LED in group C:
# i
# c
# 3

# Mapping GPIO to LED
#
# A (6 - GND)
#  2 -> blue
#  3 -> red
#  4 -> yellow 
# 14 -> green
#
# B (14 - GND)
# 17 -> blue
# 27 -> red
# 22 -> yellow
# 18 -> green
#
# C (20 - GND)
# 24 -> blue
# 10 -> red
#  9 -> yellow
# 25 -> green
#
# D (25 - GND)
# 11 -> blue
#  8 -> red
#  7 -> yellow
#  0 -> green


group_A = [ 2,  3,  4, 14]
group_B = [17, 27, 22, 18]
group_C = [24, 10,  9, 25]
group_D = [11,  8,  7,  0]
groups = [group_A, group_B, group_C, group_D]

# Maximum of one blue LED can be turned on, since it takes 11 mA of current.
# I am too lazy to add an additional resistor.
blue_leds = [2, 17, 24, 11]
blue_on = -1

import RPi.GPIO as GPIO
import time


def init():
    for g in groups:
        for x in g:
            GPIO.setup(x, GPIO.OUT)
            GPIO.output(x, GPIO.LOW)


def run():
    while True:
        command = str(input("Turn on: i, Turn off: o, Turn everything off: x, Quit: q: "))
        if command == "q":
            return
        elif command == "x":
            func = None
            for g in groups:
                for x in g:
                    turn_off(x)
            continue
        elif command == "i":
            func = turn_on
        elif command == "o":
            func = turn_off
        else:
            print("Unknown command.")
            continue

        group = str(input("Choose group (row) from {a, b, c, d}: "))
        if group == "a": g = group_A
        elif group == "b": g = group_B
        elif group == "c": g = group_C
        elif group == "d": g = group_D
        else:
            print("Unknown group.")
            continue

        i = int(input("Choose element index (col) from {1, 2, 3, 4}: "))
        if i < 1 or 4 < i:
            print("Index mistake.")
            continue
        
        if not func(g[i - 1]):
            print("Cannot turn on LED.")
            continue


def turn_on(gpio):
    global blue_on
    global blue_leds
    if gpio in blue_leds:
        if blue_on > -1:
            return False
        else:
            blue_on = gpio
    GPIO.output(gpio, GPIO.HIGH)
    return True


def turn_off(gpio):
    global blue_on
    global blue_leds
    if gpio in blue_leds and blue_on == gpio:
        blue_on = -1
    GPIO.output(gpio, GPIO.LOW)
    return True


def test():
    for g in groups:
        for x in g:
            GPIO.output(x, GPIO.HIGH)
            time.sleep(2)
            GPIO.output(x, GPIO.LOW)


if __name__=="__main__":
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    init()

    run()

    GPIO.cleanup()
