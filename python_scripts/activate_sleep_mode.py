#####################################################
# Turns "off" the house and plays a random good night
# message on Homeosaur
#####################################################

# Get Params
messageNum = int(data.get('randomNum')) # Get random number from HASS.

# Array of good night messages.
messageArray = ["Good night Mr. Monkey!", "Night night.", "Bed time!", "I love cozy blankets.", "I'll go ahead and lock up.",
                "Sleepy times activated.", "I'll stand guard.", "Make sure the stuffs are tucked in!",
                "Who programmed this? It's awesome.", "Mohave, make sure Chick is tucked in!"]

# Play random good night message.
data = { "entity_id" : "media_player.homeosaur", "message" : messageArray[messageNum] }
hass.services.call('tts', 'google_say', data)

# Turn on bedroom fan
data = { "entity_id" : "switch.bedroom_fan" }
hass.services.call('switch', 'turn_on', data)

# Turn off tv
data = { "entity_id" : "remote.living_room" }
hass.services.call('remote', 'turn_off', data)

# Turn off all lights in the house
logger.info("Turning off all lights")
data = { "entity_id" : "group.all_lights" }
hass.services.call('light', 'turn_off', data)
