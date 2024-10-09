from RPi.GPIO import GPIO as GPIO
import time

# set up pins

GPIO.setmode(GPIO.BCM)

# Front direction
dir1F = 14
dir2F = 23

# Back direction
dir1B = 15
dir2B = 24

# PWM
pwm1F = 25
pwm2F = 8

pwm1B = 7
pwm2B = 1


# Setting pins to outpt
GPIO.setup(dir1F, GPIO.OUT)
GPIO.setup(dir2F, GPIO.OUT)
GPIO.setup(dir1B, GPIO.OUT)
GPIO.setup(dir1B, GPIO.OUT)
GPIO.setup(pwm1F, GPIO.OUT)
GPIO.setup(pwm2F, GPIO.OUT)
GPIO.setup(pwm1B, GPIO.OUT)
GPIO.setup(pwm2B, GPIO.OUT)

pwm = GPIO.PWM(pwm1F, 50)
pwm.start(0)
time.sleep(5)
pwm.stop()
GPIO.cleanup()