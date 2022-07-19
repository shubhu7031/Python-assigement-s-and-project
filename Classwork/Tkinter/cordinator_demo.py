from pynput import *

def get_coords(x,y):
    print(f"Now at:{x,y}")

with mouse.Listener(on_move=get_coords)as listen:
    listen.join()