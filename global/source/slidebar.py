import gi

from . import clock

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

def get_snap_value(value, min_value, max_value, step_increment):
    step_offset = (value - min_value) % step_increment
    has_offset = step_offset != 0
    
    if has_offset:
        snap_value = round(step_offset) + min_value
        snap_overflow = snap_value > max_value
        
        if snap_overflow:
            return max_value

        else:
            return snap_value
        
    else:
        return value
        

def snap_handle(adjustment, min_value, max_value, step_increment = 1):
    if clock.is_active():
        value = adjustment.get_value()
        snap_value = get_snap_value(value, min_value, max_value, step_increment)
        
        adjustment.set_value(snap_value)


def snappy(slidebar):
    adjustment = slidebar.get_adjustment()
    min_value = adjustment.get_lower()
    max_value = adjustment.get_upper()
    step_increment = adjustment.get_step_increment()

    clock.init(1/60)
    
    adjustment.connect("value-changed", snap_handle(adjustment, min_value, max_value, step_increment))