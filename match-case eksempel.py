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

        match(sensor_value_left, sensor_value_right, back_sensor_left_value, back_sensor_right_value):
            case(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.LOW):
                print("Left sensor is on the line")
                Move(GPIO.LOW, 0, 50)
            case(GPIO.LOW, GPIO.HIGH, GPIO.LOW, GPIO.LOW):
                print("Right sensor is on the line")
                Move(GPIO.LOW, 50, 0)
            case(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.LOW):
                print("Back left sensor is on the line")
                Move(GPIO.LOW, 0, 50)
            case(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.HIGH):
                print("Back right sensor is on the line")
                Move(GPIO.LOW, 50, 0)
            case(GPIO.LOW, GPIO.HIGH, GPIO.HIGH, GPIO.LOW):
                print("Right sensor and back left sensor are on the line")
                Move(GPIO.LOW, 50, 0)
            case(GPIO.HIGH, GPIO.LOW, GPIO.LOW, GPIO.HIGH):
                print("Left sensor and back right sensor are on the line")
                Move(GPIO.LOW, 0, 50)
            case(GPIO.LOW, GPIO.LOW, GPIO.HIGH, GPIO.HIGH):
                print("Left and right sensor are on the line")
                Move(GPIO.LOW, 25, 25)
            case(GPIO.HIGH, GPIO.HIGH, GPIO.LOW, GPIO.LOW):
                print("Back left and back right sensor are on the line")
                Move(GPIO.LOW, 25, 25)
            case(GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW):
                print("All sensors are on the line")
                Move(GPIO.LOW, 0, 0)
            case(GPIO.HIGH, GPIO.HIGH, GPIO.HIGH, GPIO.HIGH):
                print("No sensors are on the line")
                if sensor_value_left == GPIO.LOW:
                    print("Left sensor is on the line")
                    Move(GPIO.LOW, 50, 0)
                Move(GPIO.LOW, 50, 50)
        time.sleep(0.1)    
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
    print("GPIO cleanup")