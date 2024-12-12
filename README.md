# MAVLink work

This repo holds some of the scripts used in my project on security regarding MAVLink. These scripts were mainly used on the raspberry pi acting as the third party on a link.

As an alternative to the scripts, running MAVProxy was also explored instead.

[mavlinkreciever.py](mavlinkreciever.py) is an example reciever that listens to messages on a link.

[disarm.py](disarm.py) sends a disarm command to the drone.

[sendgcsmessage.py](sendgcsmessage.py) sends a message to the GCS. I used this after I locked out the drone from the original GCS. 

[setupsigning.py](setupsigning.py) shows how to enable message signing on a link using pymavlink. I was having trouble with it initially, so opted to showcase how to do it here. 

[disarm-wordlist.py](disarm-wordlist.py) iterates through the [rockyou](https://github.com/danielmiessler/SecLists/blob/master/Passwords/Leaked-Databases/rockyou.txt.tar.gz) wordlist and attempts to disarm the drone by attempting multiple passwords. 