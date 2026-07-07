filter_enabled = False
website_properties_enabled = False

def side_menu_visible(builder):
    global filter_enabled, website_properties_enabled
    
    if filter_enabled or website_properties_enabled:
        side_menu = builder.get_object("side-menu")
        side_menu.show()
        return True
        
    else:
        side_menu.hide()
        return False
    

def on_filter_toggle(builder):
    global filter_enabled
    filter_enabled = not filter_enabled
    side_menu_visible(builder)
    

def on_website_properties_toggle(builder):
    global website_properties_enabled
    website_properties_enabled = not website_properties_enabled
    side_menu_visible(builder)
    

def init(builder):
    filter_switch_button = builder.get_object("filter-switch-button")
    filter_switch_button.connect("clicked", on_filter_toggle(builder))
    
    website_properties_button = builder.get_object("website-properties-button")
    website_properties_button.connect("clicked", on_website_properties_toggle(builder))