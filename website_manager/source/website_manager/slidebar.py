import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

def snap_handle(sliderbar, min_value, max_value, step_increment = 1):
    pass

def snappy(slidebar):
    adjustment = slidebar.get_adjustment()
    min_value = adjustment.get_lower()
    max_value = adjustment.get_upper()
    step_increment = adjustment.get_step_increment()
    
    adjustment.connect(("value-change", ""), snap_handle(slidebar, min_value, max_value, step_increment))
    
    
    
    