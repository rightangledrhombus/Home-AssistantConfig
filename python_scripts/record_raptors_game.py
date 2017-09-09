#####################################################
# Record Raptors game at the appropriate time and
# channel
#####################################################

# Function to delay the script so the Harmony commands execute in the correct order (Can't use time.sleep()
# because I can't import anyhting)
def delay(amount):
    temp = 0
    for i in range(0,amount):
        temp = 1

# Get Params
input_string = data.get('input_string') #Should be in format 'Station HH:MM'
input_string = "TSN 12:00" # for testing
current_time = 21

# Get station and time from the input string
station = input_string.split()[0]
time = input_string.split()[1]
time_hours = int(float(time.split(":")[0])) * 2 #each hour is two units
time_mins = int(float(time.split(":")[1]) / 30) #each 30 min is one unit

# turn on PVR
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "PowerToggle" }
#hass.services.call('remote', 'send_command', data)

# Turn on Guide
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "Guide" }
#hass.services.call('remote', 'send_command', data)

# Navigate to channel
delay(50)
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "9" }
hass.services.call('remote', 'send_command', data)
delay(400)
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "0" }
hass.services.call('remote', 'send_command', data)
delay(400)
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "0" }
hass.services.call('remote', 'send_command', data)

# Navigate to time slot
n_moves_right = time_hours + time_mins - current_time
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "DirectionRight" }
for i in range(0,n_moves_right):
    hass.services.call('remote', 'send_command', data)

# Record
delay(10000)
data = { "entity_id" : "remote.living_room", "device" : "45839120", "command" : "Record" }
hass.services.call('remote', 'send_command', data)
