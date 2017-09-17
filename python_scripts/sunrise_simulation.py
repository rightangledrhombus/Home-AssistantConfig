""" Brighten morning lights and change the temperature """

# Set Params
#brightness goes from 0 - 255
brightness_increment = 10
brightness_max = 130
brightness_min = 0
# mired = 1,000,000/kelvin
mired_increment = 25
mired_max = 450
mired_min = 150

# set lights to change
entity_id1 = 'light.kitchen_left'
entity_id2 = 'light.kitchen_right'
entity_id3 = 'light.living_room_lamp_tv'

# get attributes of light
states = hass.states.get(entity_id1)
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
data = { "entity_id" : entity_id1, "brightness" : new_brightness, "color_temp" : new_mired}
hass.services.call('light', 'turn_on', data)
data = { "entity_id" : entity_id2, "brightness" : new_brightness, "color_temp" : new_mired}
hass.services.call('light', 'turn_on', data)
data = { "entity_id" : entity_id3, "brightness" : new_brightness, "color_temp" : new_mired}
hass.services.call('light', 'turn_on', data)
