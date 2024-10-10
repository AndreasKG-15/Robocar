import RPi.GPIO as GPIO
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

# Line sensor
line_sensor_left = 16
line_sensor_right = 12


# Setting pins to outpt
GPIO.setup(dir1F, GPIO.OUT)
GPIO.setup(dir2F, GPIO.OUT)
GPIO.setup(dir1B, GPIO.OUT)
GPIO.setup(dir2B, GPIO.OUT)
GPIO.setup(pwm1F, GPIO.OUT)
GPIO.setup(pwm2F, GPIO.OUT)
GPIO.setup(pwm1B, GPIO.OUT)
GPIO.setup(pwm2B, GPIO.OUT)
GPIO.setup(line_sensor_left, GPIO.IN)
GPIO.setup(line_sensor_right, GPIO.IN)

pwm1 = GPIO.PWM(pwm1F, 50)
pwm2 = GPIO.PWM(pwm2F, 50)
pwm3 = GPIO.PWM(pwm1B, 50)
pwm4 = GPIO.PWM(pwm2B, 50)
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)



sensor_value_left = GPIO.input(line_sensor_left)
sensor_value_right = GPIO.input(line_sensor_right)

def forward(direction, speed):
    if direction == 'forward':
        GPIO.output(dir1F, GPIO.LOW)
        GPIO.output(dir2F, GPIO.LOW)
        GPIO.output(dir1B, GPIO.LOW)
        GPIO.output(dir2B, GPIO.LOW)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)
    pwm3.ChangeDutyCycle(speed)
    pwm4.ChangeDutyCycle(speed)
    if sensor_value_left == GPIO.HIGH:
        pwm1.ChangeDutyCycle(speed/2)
        pwm3.ChangeDutyCycle(speed/2)
    if sensor_value_right == GPIO.HIGH:
        pwm2.ChangeDutyCycle(speed/2)
        pwm4.ChangeDutyCycle(speed/2)
    if sensor_value_left == GPIO.HIGH and sensor_value_right == GPIO.HIGH:
        pwm1.ChangeDutyCycle(speed/4)
        pwm2.ChangeDutyCycle(speed/4)
        pwm3.ChangeDutyCycle(speed/4)
        pwm4.ChangeDutyCycle(speed/4)
        


forward('forward', 100)
time.sleep(5)

pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()
GPIO.cleanup()