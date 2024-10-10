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
        
left_sensor_enabled = True
right_sensor_enabled = True

max_speed = 70
lowest_speed = 10

sensor_left_flag = False
sensor_right_flag = False
back_sensor_left_flag = False
back_sensor_right_flag = False

left_sensor_time = 0
right_sensor_time = 0
back_sensor_left_time = 0
back_sensor_right_time = 0

try:
    while True:
        sensor_value_left = GPIO.input(line_sensor_left)
        sensor_value_right = GPIO.input(line_sensor_right)
        back_sensor_left_value = GPIO.input(back_sensor_left)
        back_sensor_right_value = GPIO.input(back_sensor_right)
        current_time = time.time()
        '''
        if sensor_value_left == GPIO.LOW and sensor_value_right == GPIO.LOW:
            print("Both sensors detected line, moving forward slowly")
            Move(GPIO.LOW, max_speed, max_speed)
        #elif back_line_sensor_left_value == GPIO.LOW:
        #    left_sensor_enabled = False
        #    print("Left sensor disabled")
        #    print("backup sensor enabled")
        #    while left_sensor_enabled == False:
        #        Move(GPIO.LOW, 0, 70)
        #        if(sensor_value_right == GPIO.LOW):
        #            left_sensor_enabled = True
        #            print("Left sensor enabled")
        #            break
            #time.sleep(0.1)
            #if sensor_value_right == GPIO.LOW:
            #    break
        #elif back_line_sensor_right_value == GPIO.LOW:
        #    right_sensor_enabled = False
        #    print("Right sensor disabled")
        #    print("Righ backup sensor enabled")
        #    while right_sensor_enabled == False:
        #        Move(GPIO.LOW, 70, 0)
        #        if(sensor_value_left == GPIO.LOW):
        #            right_sensor_enabled = True
        #            print("Right sensor enabled")
        #            break
        elif back_sensor_left_value == GPIO.LOW and back_sensor_right_value == GPIO.LOW:
            print("Both back sensors detected line")
            Move(GPIO.LOW, lowest_speed+30, lowest_speed+30) 
        elif back_sensor_left_value == GPIO.LOW:
            print("Back left sensor detected line")
            Move(GPIO.LOW, lowest_speed, max_speed+5) 
        elif back_sensor_right_value == GPIO.LOW:
            print("Back right sensor detected line")
            Move(GPIO.LOW, max_speed+5, lowest_speed)
        elif sensor_value_right == GPIO.HIGH and sensor_value_left == GPIO.HIGH:
            print("No line detected, moving forward")
            Move(GPIO.LOW, max_speed, max_speed)
        elif sensor_value_left == GPIO.LOW and left_sensor_enabled:
            print("Left sensor detected line")
            right_sensor_enabled = True
            Move(GPIO.LOW, lowest_speed, max_speed)
        elif sensor_value_right == GPIO.LOW and right_sensor_enabled:
            print("Right sensor detected line")
            left_sensor_enabled = True
            Move(GPIO.LOW, max_speed, lowest_speed)
            #if sensor_value_left == GPIO.LOW:
            #    break
            #time.sleep(0.1)
        '''
        ''' elif back_sensor_right_value == GPIO.LOW and sensor_value_left == GPIO.LOW:
            print("Back right sensor detected line")
            Move(GPIO.LOW, lowest_speed, max_speed) 
        elif back_sensor_left_value == GPIO.LOW and sensor_value_right == GPIO.LOW:
            print("Back right sensor detected line")
            Move(GPIO.LOW, max_speed, lowest_speed)
        '''
        if sensor_value_left == GPIO.LOW:
            sensor_left_flag = True
            left_sensor_time = current_time
            #print("Left sensor detected")
        if sensor_value_right == GPIO.LOW:
            sensor_right_flag = True
            right_sensor_time = current_time
            #print("Right sensor detected")
        if back_sensor_left_value == GPIO.LOW:
            back_sensor_left_flag = True
            back_sensor_left_time = current_time
            #print("Back left sensor detected")
        if back_sensor_right_value == GPIO.LOW:
            back_sensor_right_flag = True
            back_sensor_right_time = current_time
            #print("Back right sensor detected")
            
        # Pair sensor detection
        
        # If both front sensors detect line
        if sensor_left_flag and sensor_right_flag:
            if current_time - left_sensor_time < 0.5 and current_time - right_sensor_time < 0.5:
                print("Both front sensors detected")
                Move(GPIO.LOW, max_speed, max_speed)
        # If front left sensor and back right sensor detect line
        if sensor_left_flag and back_sensor_right_flag:
            if current_time - left_sensor_time < 0.5 and current_time - back_sensor_right_time < 0.5:
                print("Left front and right back sensors detected")
                Move(GPIO.LOW, lowest_speed, max_speed)
        # if front right sensor and back left sensor detect line
        if sensor_right_flag and back_sensor_left_flag:
            if current_time - right_sensor_time < 0.5 and current_time - back_sensor_left_time < 0.5:
                print("Right front and left back sensors detected")
                Move(GPIO.LOW, max_speed, lowest_speed)
        # if front left sensor and back left sensor detect line (left side)
        if sensor_left_flag and back_sensor_left_flag:
            if current_time - left_sensor_time < 0.5 and current_time - back_sensor_left_time < 0.5:
                print("Left front and left back sensors detected")
                Move(GPIO.LOW, lowest_speed, max_speed)
        # if front right sensor and back right sensor detect line (right side)
        if sensor_right_flag and back_sensor_right_flag:
            if current_time - right_sensor_time < 0.5 and current_time - back_sensor_right_time < 0.5:
                print("Right front and right back sensors detected")
                Move(GPIO.LOW, max_speed, lowest_speed)
        
        # Individiual sensor detection
        
        # if front left sensor detects line
        if sensor_left_flag:
            Move(GPIO.LOW, lowest_speed, max_speed)
        # if front right sensor detects line
        if sensor_right_flag:
            Move(GPIO.LOW, max_speed, lowest_speed)
        # if back left sensor detects line
        if back_sensor_left_flag:
            Move(GPIO.LOW, lowest_speed, max_speed)
        # if back right sensor detects line
        if back_sensor_right_flag:
            Move(GPIO.LOW, max_speed, lowest_speed)
            
            
        time.sleep(0.1)   
except KeyboardInterrupt:
    pass

finally:
    print("Cleaning up")
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()
    GPIO.cleanup()
