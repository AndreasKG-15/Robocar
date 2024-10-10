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

back_sensor_left = 2
back_sensor_right = 3


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

GPIO.setup(back_sensor_left, GPIO.IN)
GPIO.setup(back_sensor_right, GPIO.IN)

pwm1 = GPIO.PWM(pwm1F, 50)
pwm2 = GPIO.PWM(pwm2F, 50)
pwm3 = GPIO.PWM(pwm1B, 50)
pwm4 = GPIO.PWM(pwm2B, 50)
# pwm front right
pwm1.start(0)
# pwm front left
pwm2.start(0)
# pwm back right
pwm3.start(0)
# pwm back left
pwm4.start(0)

front_left_sensor = True
front_right_sensor = True




def Move(state, speedLeft, speedRight):
    GPIO.output(dir1F, state)
    GPIO.output(dir2F, state)
    GPIO.output(dir1B, state)
    GPIO.output(dir2B, state)
    # Set speed for front right motor
    pwm1.ChangeDutyCycle(speedRight)
    # Set speed for front left motor
    pwm2.ChangeDutyCycle(speedLeft)
    # Set speed for back right motor
    pwm3.ChangeDutyCycle(speedRight)
    # Set speed for back left motor
    pwm4.ChangeDutyCycle(speedLeft)
    
try:
    while True:
        sensor_value_left = GPIO.input(line_sensor_left)
        sensor_value_right = GPIO.input(line_sensor_right)
        back_sensor_left_value = GPIO.input(back_sensor_left)
        back_sensor_right_value = GPIO.input(back_sensor_right)
        current_time = time.time()
        if sensor_value_left == 1 and sensor_value_right == 1   :
            print("Both sensors are off the line")
            Move(0, 50, 50)
        if sensor_value_left == 1 and sensor_value_right == 0 and front_left_sensor == True and front_right_sensor == True:
            print("Right sensor detected line")
            front_left_sensor = True
            Move(0, 50, 0)
        if sensor_value_left == 0 and sensor_value_right == 1 and front_left_sensor == True and front_right_sensor == True:
            print("Left sensor detected line")
            front_right_sensor = True
            Move(0, 0, 50)
        if sensor_value_left == 0 and sensor_value_right == 0 and front_left_sensor == True and front_right_sensor == True:
            print("Both sensors detected line")
            Move(0, 40, 40)
        if back_sensor_left_value == 1 and back_sensor_right_value == 0 and front_left_sensor == True and front_right_sensor == True:
            print("Right back sensor detected line")
            front_left_sensor = False
            Move(0, 50, 0)
        if back_sensor_left_value == 0 and back_sensor_right_value == 1 and front_left_sensor == True and front_right_sensor == True:
            print("Left back sensor detected line")
            front_right_sensor = False
            Move(0, 0, 50)
        if back_sensor_left_value == 0 and back_sensor_right_value == 0 and front_left_sensor == True and front_right_sensor == True:
            print("Both back sensors detected line")
            Move(0, 40, 40)
            
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("GPIO cleanup completed.")