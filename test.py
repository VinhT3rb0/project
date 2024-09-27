from  EmulatorGUI import GPIO
import time
import random
BUZZER_PIN = 18
UP_BUTTON_PIN = 23
DOWN_BUTTON_PIN = 24
TEMp_LIMIT_DEFAULT = 30
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)
GPIO.setup(UP_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(DOWN_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def lcd_display_string(text, line):
    print(f"LCD line {line}: {text}")
temp_limit = TEMp_LIMIT_DEFAULT
alarm_activity = False
def adjust_temp_limit():
    global temp_limit
    if GPIO.input(UP_BUTTON_PIN) ==GPIO.LOW:
        temp_limit += 1
        print(f"Temp Limit: {temp_limit}")
    elif GPIO.input(DOWN_BUTTON_PIN) == GPIO.LOW:
        temp_limit -= 1
        print(f"Temp Limit: {temp_limit}")

def trigger_alarm():
    global alarm_activity
    alarm_activity = True
    GPIO.output(BUZZER_PIN, GPIO.HIGH)
    lcd_display_string("Careful!",1)
    time.sleep(5)
    if GPIO.input(UP_BUTTON_PIN) ==GPIO.LOW or GPIO.input(DOWN_BUTTON_PIN) ==GPIO.LOW:
        reset_temp()
def reset_temp():
    global alarm_activity
    alarm_activity = False
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    lcd_display_string("Cleared alarm!",1)
    time.sleep(2)
    lcd_display_string("",1)
def read_temperature_humidity():
    temperature = random.uniform(10.0,40.0)
    humidity = random.uniform(30.0, 90.0)
    return temperature,humidity
try:
    while True:
        humidity, temperature = read_temperature_humidity()
        lcd_display_string(f"Temp: {temperature:.1f}C", 1)
        lcd_display_string(f"Humidity: {humidity:.1f}%", 2)
        adjust_temp_limit()
        lcd_display_string(f"Temp limit: {temp_limit}",1)
        if(temperature > temp_limit):
            trigger_alarm()
        time.sleep(5)
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup() 