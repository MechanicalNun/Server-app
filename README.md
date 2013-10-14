Server-app
==========

The server can be deployed on a raspberry pi or on a laptop

default mode:
Nun and Booth are present

Receiving:
Sin data -> has meta label for client, if booth or Nun. 
Visualization filters from dashboard
events from booth app

Sending:
Sound data (booth) -> is the booth android app event driven for light and sound? 
Light data (booth)
Visual data (projector)

Munging:

Creating a record for each sin
querying the db for sin categories
Creating JSON data for dashboard
returning light sequence for booth
accessing correct index for sound 


confging your wifi card, headless: 
# 1. plug in network card and cable and turn your machine on. 
# 2. Find ip address in from your routers page
# 3. ssh into it using pi@<ip_address>, password is 'raspberry'
# 4. in command line type: 
~ $ sudo -i
~ $ sudo nano /etc/wpa_supplicant/wpa_supplicant.conf
ssid, '<your wifis name>'
password
:wq
testing: 
~ $ ifdown wlan0
unplug cable
~ $ ifup wlan0





