""" Brighten morning lights and change the temperature """

# Set Params
#brightness goes from 0 - 255
brightness_max = 130
brightness_min = 0
brightness_increment = 10

# mired = 1,000,000/kelvin
mired_max = 450
mired_min = 225
mired_increment = 15

# set lights to change
entity_ids = ['light.kitchen_left', 'light.kitchen_right', 'light.living_room_lamp_tv', 'light.guest_bathroom']

# get attributes of light
states = hass.states.get(entity_ids[0])
brightness = states.attributes.get('brightness')
mired = states.attributes.get('color_temp')

# set new data
new_brightness = brightness + brightness_increment
new_mired = mired - mired_increment

# mired values for color temp go from approx.
# mired = 1,000,000/kelvin
if (new_mired < mired_min): new_mired = mired_min
elif (new_mired > mired_max): new_mired = mired_max

if (new_brightness < brightness_min): new_brightness = brightness_min
elif (new_brightness > brightness_max): new_brightness = brightness_max

# Call service
for i in range(0,len(entity_ids)):
    data = { "entity_id" : entity_ids[i], "brightness" : new_brightness, "color_temp" : new_mired}
    hass.services.call('light', 'turn_on', data)
