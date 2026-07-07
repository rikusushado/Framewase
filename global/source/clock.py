import threading
import time

clock_thread = threading._DummyThread

clock_stop = False
clock_active = False

def clock(frametime):
    global clock_active, clock_stop
    
    if frametime > 1:
        print("Error: Frametime cannot exceed 1 second")
        exit(-1)
        
    half_time = frametime / 2
    
    while not clock_stop:
        clock_active = True
        time.sleep(half_time)
        clock_active = False
        time.sleep(half_time)

def init(frametime):
    clock_thread = threading.Thread(target=clock, args=(frametime))
    clock_thread.start()
    
def stop():
    clock_thread.join()
    
def is_active():
    return clock_active