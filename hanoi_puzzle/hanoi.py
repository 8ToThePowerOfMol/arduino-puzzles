#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import RPi.GPIO as GPIO
import time
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

## GPIO Setting:
## leds:
##    2 17 14 10
##    3 27 15 9
##    4 22 18 11
##
## buttons:
##    25
##    8
##    7
##    23 (reset)
## 24 (buzzer)

GPIO.setup(2, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(9, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(7, GPIO.IN)
GPIO.setup(8, GPIO.IN)
GPIO.setup(25, GPIO.IN)
GPIO.setup(23, GPIO.IN)
GPIO.setup(24, GPIO.OUT)
    
GPIO.output(4, GPIO.LOW)
GPIO.output(22, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(11, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(9, GPIO.LOW)
GPIO.output(2, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(14, GPIO.LOW)
GPIO.output(10, GPIO.LOW)
GPIO.output(4, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)
GPIO.output(18, GPIO.HIGH)
GPIO.output(11, GPIO.HIGH)

GPIO.output(24, GPIO.LOW)


a = [0,0,0,0]
b = [0,0,0,0]
c = [1,1,1,1]


# x={a[0]: 2, a[1]: 17, a[2]: 14, a[3]: 10, b[0]: 3, b[1]: 27, b[2]: 15, b[3]: 9, c[0]: 4, c[1]: 22, c[2]: 18, c[3]: 11}

def swap(A, B):
    try:
        i = A.index(1)
    except ValueError:
        i = 4
    try:
        j = B.index(1)
    except ValueError:
        j = 4
    if i <= j:
        A[i], B[i] = B[i], A[i]
        return i
    else:
        print("Cannot swap!")
        return -1

def get_pin(tower, i):
    if tower == 1:
        if i == 0:
            return 2
        elif i == 1:
            return 17
        elif i == 2:
            return 14
        elif i == 3:
            return 10
        else:
            print("Pin error!")
            return -1
    elif tower == 2:
        if i == 0:
            return 3
        elif i == 1:
            return 27
        elif i == 2:
            return 15
        elif i == 3:
            return 9
        else:
            print("Pin error!")
            return -1
    elif tower == 3:
        if i == 0:
            return 4
        elif i == 1:
            return 22
        elif i == 2:
            return 18
        elif i == 3:
            return 11
        else:
            print("Pin error!")
            return -1
    else:
        print("Pin error!")
        return -1

def reset():
    GPIO.output(4, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    time.sleep(2)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(4, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.output(18, GPIO.LOW)
    GPIO.output(11, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(15, GPIO.HIGH)
    GPIO.output(9, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(3, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    GPIO.output(15, GPIO.LOW)
    GPIO.output(9, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(2, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(14, GPIO.HIGH)
    GPIO.output(10, GPIO.HIGH)
    time.sleep(.5)
    GPIO.output(2, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(14, GPIO.LOW)
    GPIO.output(10, GPIO.LOW)
    time.sleep(.5)
    GPIO.output(4, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)
    GPIO.output(18, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    print("Reset done!")

def beep():
   GPIO.output(24, GPIO.HIGH)
   time.sleep(.03)
   GPIO.output(24, GPIO.LOW)

is_any_button_pressed = False

while a != [1,1,1,1]:
    while(GPIO.input(25) == False) or (GPIO.input(8) == False) or (GPIO.input(7) == False) or (GPIO.input(23) == False):
        time.sleep(.3)

    print(a, b, c, sep='\n')

    is_any_button_pressed = False
    while 1:
        if not is_any_button_pressed:
            if(GPIO.input(25) == False):
                source = int(1)
                is_any_button_pressed = True
                print("source =", source)
                beep()
                break
            elif(GPIO.input(8) == False):
                source = int(2)
                is_any_button_pressed = True
                print("source =", source)
                beep()
                break
            elif(GPIO.input(7) == False):
                source = int(3)
                is_any_button_pressed = True
                print("source =", source)
                beep()
                break
            elif(GPIO.input(23) == False):
                source = int(0)
                is_any_button_pressed = True
                print("source =", source)
                beep()
                break
            else:
                pass
                
    while(GPIO.input(25) == False) or (GPIO.input(8) == False) or (GPIO.input(7) == False) or (GPIO.input(23) == False):
        time.sleep(.3)

    is_any_button_pressed = 0
    while 1:
        if is_any_button_pressed == 0:
            if(GPIO.input(25) == False):
                dest = int(1)
                is_any_button_pressed = 1
                print("dest =", dest)
                beep()
                break
            elif(GPIO.input(8) == False):
                dest = int(2)
                is_any_button_pressed = 1
                print("dest =", dest)
                beep()
                break
            elif(GPIO.input(7) == False):
                dest = int(3)
                is_any_button_pressed = 1
                print("dest =", dest)
                beep()
                break
            elif(GPIO.input(23) == False):
                dest = int(0)
                is_any_button_pressed = 1
                print("dest =", dest)
                beep()
                break
            else:
                pass
            
    if source == 0 or dest == 0:
        reset()
        a = [0,0,0,0]
        b = [0,0,0,0]
        c = [1,1,1,1]
        i = -1
        beep()
        
    # switch for all posibilities swapping inside array:
    elif source == 1 and dest == 2:
        i = swap(a, b)
    elif source == 1 and dest == 3:
        i = swap(a, c)
    elif source == 2 and dest == 1:
        i = swap(b, a)
    elif source == 2 and dest == 3:
        i = swap(b, c)
    elif source == 3 and dest == 1:
        i = swap(c, a)
    elif source == 3 and dest == 2:
        i = swap(c, b)
    else:
        print("Cannot swap!")
        i = -1

    if i != -1:
        zhas = get_pin(source, i)
        rozs = get_pin(dest, i)
        GPIO.output(zhas, GPIO.LOW)
        GPIO.output(rozs, GPIO.HIGH)
    else:
        print("Pin is not searching!")

print("YOU WON!")
GPIO.output(24, GPIO.HIGH)
for k in range(10):
    beep()
    time.sleep(.1)

GPIO.cleanup()
