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
    
def checkSensor(left_sensor, right_sensor, back_left_sensor, back_right_sensor):
    front_left_sensor = True
    front_right_sensor = True
    print(f"Left sensor: {left_sensor}, Right sensor: {right_sensor}, Back left sensor: {back_left_sensor}, Back right sensor: {back_right_sensor}")
    
    if left_sensor == GPIO.HIGH and back_right_sensor == GPIO.LOW:
        front_left_sensor = False
    if right_sensor == GPIO.HIGH and back_left_sensor == GPIO.LOW:
        front_right_sensor = False
    if left_sensor == GPIO.LOW:
        front_left_sensor = True
        if left_sensor == GPIO.LOW and front_left_sensor == True:
            print("Left sensor detected line")
            Move(GPIO.LOW, 0, 50)
            time.sleep(0.2)
    if right_sensor == GPIO.LOW:
        front_right_sensor = True
        if right_sensor == GPIO.LOW and front_right_sensor == True:
            print("Right sensor detected line")
            Move(GPIO.LOW, 50, 0)
            time.sleep(0.2)
        
    if back_left_sensor == GPIO.LOW:
        print("Left back sensor detected line")
        front_right_sensor = False
        Move(GPIO.LOW, 0, 50)
    elif back_right_sensor == GPIO.LOW:
        print("Right back sensor detected line")
        front_left_sensor = False
        Move(GPIO.LOW, 50, 0)
    elif left_sensor == GPIO.LOW and right_sensor == GPIO.LOW:
        print("Both sensors detected line... moving forward slowly")
        Move(GPIO.LOW, 40, 40)
    
    
    
try:
    while True:
        sensor_value_left = GPIO.input(line_sensor_left)
        sensor_value_right = GPIO.input(line_sensor_right)
        back_sensor_left_value = GPIO.input(back_sensor_left)
        back_sensor_right_value = GPIO.input(back_sensor_right)
        current_time = time.time()
        if sensor_value_left == GPIO.LOW and sensor_value_right == GPIO.LOW and back_sensor_left_value == GPIO.LOW and back_sensor_right_value == GPIO.LOW:
            print("All sensors detect no line")
            Move(GPIO.LOW, 50, 50)
        else:
            checkSensor(sensor_value_left, sensor_value_right, back_sensor_left_value, back_sensor_right_value)
            
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Keyboard interrupt detected.")
except Exception as e:
    print(f"An error occured: {e}")
finally:
    GPIO.cleanup()
    print("GPIO cleanup completed.")