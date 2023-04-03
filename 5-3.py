import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

leds=[21,20,16,12,7,8,25,24]
dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT)
gpio.setup(leds,gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perevod(x):
    return [int (digit) for digit in bin(x)[2:].zfill(8)]

def adc():
    for i in range(256):
        x = perevod(i)
        gpio.output(dac, x)
        compresult = gpio.input(comp)
        if compresult == 0:
            return i
    return 0

def ledslook(x):
    n = int(x/256*8)
    arr = [0]*8
    for i in range(n):
        arr[i] = 1
    return arr

try:
    while True:
        i = adc()
        gpio.output(leds,ledslook(i))
finally:
    gpio.output(dac, 0)
    gpio.cleanup()