import RPi.GPIO as rpi

pin = 2
dac=[26,19,13,6,5,11,9,10]
rpi.setmode(rpi.BCM)
rpi.setup(pin,rpi.OUT)
rpi.setup(dac,rpi.OUT)

pwm=rpi.PWM(pin,1000)
pwm.start(0)

try:
    while True:
        duty = int(input())
        pwm.ChangeDutyCycle(duty)
        print(duty*3.3/100)

finally:
    rpi.output(pin,0)
    rpi.output(dac,0)
    rpi.cleanup()