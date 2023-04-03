import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dac = [26,19,13,6,5,11,9,10]
comp = 4
troyka = 17

gpio.setup(dac, gpio.OUT)
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

try:
    while True:
        i = adc()
        print("Volt: ",3.3*i/256)
finally:
    gpio.output(dac, 0)
    gpio.cleanup()