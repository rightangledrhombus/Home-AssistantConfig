""" Brighten morning lights and change the temperature """

# Set Params
#brightness goes from 0 - 255
brightness_max = 175
brightness_min = 0
brightness_increment = 10

# mired = 1,000,000/kelvin
mired_max = 450
mired_min = 225
mired_increment = 20

# set lights to change
#entity_ids = ['light.kitchen_left', 'light.kitchen_right', 'light.living_room_lamp_tv']
entity_ids = ['light.gaming_room_lamp']

# initialize all lists
n_lights = len(entity_ids)
states = [None] * n_lights
brightness = [None] * n_lights
mired = [None] * n_lights
new_brightness = [None] * n_lights
new_mired = [None] * n_lights

# loop through lists, find state values and set new ones
for i in range(0,n_lights):
    # get attributes of light
    states[i] = hass.states.get(entity_ids[i])
    brightness[i] = states[i].attributes.get('brightness') or 0
    mired[i] = states[i].attributes.get('color_temp') or 255

    # set new data
    new_brightness[i] = brightness[i] + brightness_increment
    new_mired[i] = mired[i] - mired_increment

    # mired values for color temp go from approx.
    # mired = 1,000,000/kelvin
    if (new_mired[i] < mired_min): new_mired[i] = mired_min
    elif (new_mired[i] > mired_max): new_mired[i] = mired_max

    if (new_brightness[i] < brightness_min): new_brightness[i] = brightness_min
    elif (new_brightness[i] > brightness_max): new_brightness[i] = brightness_max

    # Call service
    data = { "entity_id" : entity_ids[i], "brightness" : 0, "color_temp" : 450}
    hass.services.call('light', 'turn_on', data)
    data = { "entity_id" : entity_ids[i]}
    hass.services.call('light', 'turn_off', data)
