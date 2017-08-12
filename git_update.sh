#cd /home/homeassistant/.homeassistant
#source /srv/homeassistant/bin/activate
#hass --script check_config -c /home/homeassistant/.homeassistant/

sudo git add ./
sudo git status
#sudo echo -n "Enter the Description for the Change: "
#read CHANGE_MSG
read -p 'Enter the Description for the Change: ' CHANGE_MSG
sudo git commit -m "${CHANGE_MSG}"
sudo git push origin master

#exit
