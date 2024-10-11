import RPi.GPIO as GPIO
import time
from sshkeyboard import listen_keyboard

# Opsætning af GPIO pins
GPIO.setmode(GPIO.BCM)

# Motor pins
dir1F = 14
dir2F = 23
dir1B = 15
dir2B = 24
pwm1F = 25
pwm2F = 8
pwm1B = 7
pwm2B = 1

# Opsætning af pins til output
GPIO.setup(dir1F, GPIO.OUT)
GPIO.setup(dir2F, GPIO.OUT)
GPIO.setup(dir1B, GPIO.OUT)
GPIO.setup(dir2B, GPIO.OUT)
GPIO.setup(pwm1F, GPIO.OUT)
GPIO.setup(pwm2F, GPIO.OUT)
GPIO.setup(pwm1B, GPIO.OUT)
GPIO.setup(pwm2B, GPIO.OUT)

# PWM opsætning
pwm1 = GPIO.PWM(pwm1F, 50)
pwm2 = GPIO.PWM(pwm2F, 50)
pwm3 = GPIO.PWM(pwm1B, 50)
pwm4 = GPIO.PWM(pwm2B, 50)

# Start PWM
pwm1.start(0)
pwm2.start(0)
pwm3.start(0)
pwm4.start(0)

active_keys = set()

def Move(state, speedLeft, speedRight):
    GPIO.output(dir1F, state)
    GPIO.output(dir2F, state)
    GPIO.output(dir1B, state)
    GPIO.output(dir2B, state)
    pwm1.ChangeDutyCycle(speedRight)
    pwm2.ChangeDutyCycle(speedLeft)
    pwm3.ChangeDutyCycle(speedRight)
    pwm4.ChangeDutyCycle(speedLeft)


def forward():
    Move(GPIO.LOW, 100, 100)
    print("Fremad")

def back():
    Move(GPIO.HIGH, 100, 100)
    print("Bagud")
def left():
    Move(GPIO.LOW, 0, 100)
    print("Venstre")
def right():
    Move(GPIO.LOW, 100, 0)
    print("Højre")
def press(key):
    if key == 'w': #Fremad
        forward()
    elif key == 's': #Bagud
        back()
    elif key == 'a': #Venstre
        left()
    elif key == 'd': #Højre
        right()
    elif key == 'p': #Stop
        Move(True, 0, 0)


try:
    while True:
        time.sleep(0.1)
        listen_keyboard(on_press=press)
except KeyboardInterrupt:
    print("Programmet stoppes.")

finally:
    print("Rydder op")
    pwm1.stop()
    pwm2.stop()
    pwm3.stop()
    pwm4.stop()
    GPIO.cleanup()