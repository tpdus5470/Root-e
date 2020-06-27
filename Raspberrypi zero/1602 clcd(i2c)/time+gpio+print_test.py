#github library use : https://github.com/eleparts/RPi_I2C_LCD_driver

import RPi.GPIO as GPIO
import RPi_I2C_driver
import time


lcd = RPi_I2C_driver.lcd(0x27)

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#firt main title and time
lcd.clear()
lcd.print("Root-e")

lcd.setCursor(0,1)
now = time.localtime()
lcd.print(now.tm_hour)
lcd.print(":")
lcd.print(now.tm_min)
lcd.print(":")
lcd.print(now.tm_sec)


i=0

while 1:
    if GPIO.input(21)==0:
        GPIO.output(16, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(16,GPIO.LOW)
        i=i+1
        lcd.clear()
        lcd.print(i)
