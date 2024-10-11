import keyboard
import time


front_left_sensor = 0
front_right_sensor = 0
back_left_sensor = 0
back_right_sensor = 0

try:
    while True:
        if keyboard.is_pressed('1'):
            front_left_sensor = 1 if front_left_sensor == 0 else 0
            print(f"Front left sensor: {'aktiv' if front_left_sensor else 'ikke aktiv'}")
        if keyboard.is_pressed('2'):
            front_right_sensor = 1
            print(f"Front right sensor: {'aktiv' if front_right_sensor else 'ikke aktiv'}")
        if keyboard.is_pressed('3'):
            back_left_sensor = 1
            print(f"Back left sensor: {'aktiv' if back_left_sensor else 'ikke aktiv'}")
        if keyboard.is_pressed('4'):
            back_right_sensor = 1
            print(f"Back right sensor: {'aktiv' if back_right_sensor else 'ikke aktiv'}")
        else:
            print("All sensors are inactive")
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    print("Cleaning up")