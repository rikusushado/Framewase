import gi

gi.require_version("Gtk", "3.0")
gi.require_version('Gdk', '3.0')

from gi.repository import Gtk, Gdk

style_sheet_path = "website_manager/source/location_assistant/global.css"
window_source = "website_manager/source/location_assistant/window.glade"

def applyStyle():
    screen = Gdk.Screen.get_default()
    provider = Gtk.CssProvider()
    provider.load_from_path(style_sheet_path)
    Gtk.StyleContext.add_provider_for_screen(screen, provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
    
def buildWindow(glade_source):
    builder = Gtk.Builder()
    builder.add_from_file(glade_source)
    window = builder.get_object("main-window")
    
    return window
