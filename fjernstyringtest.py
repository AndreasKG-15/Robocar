import time
from sshkeyboard import listen_keyboard

active_keys = set()

def kør_fremad():
    print("Bilen kører fremad!")

def kør_bagud():
    print("Bilen kører tilbage!")

def drej_venstre():
    print("Bilen drejer til venstre!")

def drej_højre():
    print("Bilen drejer til højre!")

def update_actions():
    if 'w' in active_keys:
        kør_fremad()
    if 's' in active_keys:
        kør_bagud()
    if 'a' in active_keys:
        drej_venstre()
    if 'd' in active_keys:
        drej_højre()


def press(key):
    active_keys.add(key)
    update_actions()
    

#    if key == 'w':
#        kør_fremad()
#        print("'w' pressed: Kører fremad")
#    elif key == 's':
#        kør_bagud()
#        print("'s' pressed: Kører bagud")
#    elif key == 'd':
#        drej_højre()
#        print("'d' pressed: Drej til højre")
#    elif key == 'a':
#        drej_venstre()
#        print("'a' pressed: Drej til venstre")
    

def release(key):
    active_keys.discard(key)
    update_actions()

listen_keyboard(
    on_press=press,
    on_release=release,
    sequential=False,
)

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Programmet stoppes.")
