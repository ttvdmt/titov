import RPi.GPIO as rpi
import time

def perevod(x):
    return [int (digit) for digit in bin(x)[2:].zfill(8)]

dac=[26,19,13,6,5,11,9,10]

rpi.setmode(rpi.BCM)
rpi.setup(dac,rpi.OUT)

try:
    period=int(input())

    while(True):
        for i in range(256):
            bin=perevod(i)
            rpi.output(dac,bin)
            time.sleep(period/512)

        for i in range(255,-1,-1):
            bin=perevod(i)
            rpi.output(dac,bin)
            time.sleep(period/512)

finally:
    rpi.output(dac,0)
    rpi.cleanup()
