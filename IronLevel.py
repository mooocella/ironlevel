from machine import Pin, PHM
from time import sleep

pwm = PWM(Pin(15))

led = Pin(13, Pin.OUT)

pwm. freq(1000)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button. value():
        led.value(0)
        sleep(0.3)
        for duty in range (65025):
            pwm.duty_u16(duty)
            sleep(0.00001)
        for duty in range (65025, 0, -5):
            pwm. duty _u16(duty)
            sleep(0.00001)
    else:
        led.toggle()
