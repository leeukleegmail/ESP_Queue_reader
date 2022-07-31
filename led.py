from machine import Pin


def all_off():
    Pin(23, Pin.OUT).off()
    Pin(22, Pin.OUT).off()
    Pin(4, Pin.OUT).off()


def red(value):
    all_off()
    led = Pin(23, Pin.OUT)
    led.value(value)


def blue(value):
    all_off()
    led = Pin(4, Pin.OUT)
    led.value(value)


def green(value):
    all_off()
    led = Pin(22, Pin.OUT)
    led.value(value)

