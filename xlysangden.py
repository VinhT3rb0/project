from EmulatorGUI import GPIO
#import RPi.GPIO as GPIO
import time

led_pins = [5, 6, 13, 19, 26, 16, 20, 21]  
button_pin = 12  
delay = 1  
GPIO.setmode(GPIO.BCM)
for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def clear_leds():
    for pin in led_pins:
        GPIO.output(pin, GPIO.LOW)
def show_leds(byte):
    for i in range(8):
        if byte & (1<<i):
            GPIO.output(led_pins[i], GPIO.HIGH)
        else:
            GPIO.output(led_pins[i], GPIO.LOW)
def led_effect():
    pattern = [
        0b00011000,
        0b00100100,
        0b01000010,
        0b10000001,
        0b00000000,
        0b10000001,
        0b01000010,
        0b00100100,
        0b00011000
    ]
    for byte in pattern:
        if GPIO.input(button_pin) == GPIO.LOW:
            clear_leds()
            return
        show_leds(byte)
        time.sleep(delay)

try:
    is_running = False
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:  
            if GPIO.input(button_pin) == GPIO.LOW:  
                is_running = not is_running  
                while GPIO.input(button_pin) == GPIO.LOW:  
                    time.sleep(0.1)

        if is_running:
            led_effect() 
        else:
            clear_leds()

        time.sleep(0.1)

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()
