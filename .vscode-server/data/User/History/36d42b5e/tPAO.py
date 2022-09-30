
'''
Alle dem der er under her er imports, som vi bruger senere i koden.
'''
from sense_hat import SenseHat
from datetime import datetime
import signal
import sys
import time, datetime

hat = SenseHat()

'''
Den kode under er starten af vores raspberry pi.

'''
hat.show_message("Programmet starter")

def signal_term_handler(signal,frame):
    hat.show_message("Programmet slutter")
    sys.exit(0)

signal.signal(signal.SIGTERM, signal_term_handler)
signal.signal(signal.SIGINT, signal_term_handler)


hour_color = (0, 255, 0)
minute_color = (0, 0, 255)
second_color = (255, 0, 0)
time_12_c = (255,255,225)
timeformat_12 = False
directionvertical = True
off = (0, 0, 0)

hat.clear()

def pushed_up(event):
    global timeformat12
    print(event.action)
    if event.action == "released":
        hat.clear()
        timeformat12 = True
        hat.set_pixel(0, 0, time_12_c)

def pushed_down(event):
    global timeformat12
    print(event.action)
    if event.action == "released":
        hat.clear()
        timeformat12 = False
        hat.set_pixel(0, 0, off)

def pushed_left(event):
    global directionvertical
    print(event.action)
    if event.action == "released":
        hat.clear()
        directionvertical = False

def pushed_right(event):
    global directionvertical
    print(event.action)
    if event.action == "released":
        hat.clear()
        directionvertical = True

hat.stick.direction_up = pushed_up
hat.stick.direction_down = pushed_down
hat.stick.direction_right = pushed_right
hat.stick.direction_left = pushed_left

def display_binary(value, row, color):
    global directionvertical
    binary_str = '{0:8b}'.format(value)
    if directionvertical:
        for x in range(0, 8):
            if binary_str[x] == '1':
                hat.set_pixel(x, row, color)
            else:
                hat.set_pixel(x, row, off)
    else:
        arr = [int(a) for a in str(value)]
        if len(arr)>1:
            binary_str = "{0:4b}".format(arr[1])
            print(binary_str)
            for y in range(0,4):
                if binary_str[y] == '1':
                    hat.set_pixel(row, y, color)
                else:
                    hat.set_pixel(row, y, off)
        binary_str = "{0:4b}".format(arr[0])
        for x in range(0, 4):
            if binary_str[x] == '1':
                hat.set_pixel(row-1, x, color)
            else:
                hat.set_pixel(row-1, x, off)

while True:
    t = datetime.datetime.now()
    if timeformat_12 == True:
        t = t.strftime("%I:%M:%S")
        t = datetime.datetime.strftime(t,"%H:%M:%S")
    display_binary(t.hour, 2, hour_color)
    display_binary(t.minute, 4, minute_color)
    display_binary(t.second, 6, second_color)
    time.sleep(1)