import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.IN, pull_up_down = GPIO.PUD_UP) #pull up

#output High/Low
for i in range(5):
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.1)
    GPIO.output(19, GPIO.LOW)
    time.sleep(0.1)

#PWM
pwm = GPIO.PWM(19, 500)
pwm.start(0)

for i in range(20):
    GPIO.output(19, GPIO.HIGH)
    pwm.ChangeDutyCycle(i*5)
    time.sleep(0.01)

for i in range(20):
    pwm.ChangeDutyCycle(100-i*5)
    time.sleep(0.01)

pwm.stop()

#input
while 1:
    if GPIO.input(21)==0:
        GPIO.output(19, GPIO.HIGH)
        time.sleep(0.1)
        GPIO.output(19,GPIO.LOW)
