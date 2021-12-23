####################################
# CONTROLLER FOR LIGHTS
####################################

# Imports
from phue import Bridge
from ip_address import bridge_ip
import time

############ Light Activation ##############

def activate_lights(bridge_ip):
    bridge = Bridge(bridge_ip)
    n = 1
    while n == 1:
        activate_lights.bridge.connect()
        n +=1
        return
    light_names = bridge.get_light_objects('name')
    return light_names

################################################################
# LIGHT FUNCTIONS
################################################################
def lights():
    lights = activate_lights(bridge_ip) # Bridge IP needs to be set within ip_address, use Tkinter
    for light in lights:
        lights[light].on = True
        lights[light].hue = 15000
        lights[light].saturation = 120
        
def alert():
    lights = activate_lights(bridge_ip)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 180
        lights[light].saturation = 100
    time.sleep(1)
    for light in lights:
        lights[light].on = True
        lights[light].hue = 7000
        lights[light].saturation = 100
       
################################################################
# LIGHT ACTIVATION LOGIC
################################################################

if __name__ == '__main__':
    lights()

######## MOTION DETECTION ########
# if motion_is_detected == True:
#   alert() -> Calls the Function called alert()