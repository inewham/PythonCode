These scripts were created to address an issue I was experiencing with my BT Home Hub, I had specified an IP address in the DMZ settings (Advanced Settings > Firewall > Configuration > DMZ), but the last octet of the address would randomly change.
The first script (marked with desktop) was the initial proof of concept, and it worked great; but my intension was to run it on a headless server (hence the script marked server).
The server script requires a Selenium docker container (https://hub.docker.com/r/selenium/standalone-chrome).
I understand the code could be written better, but it was my first functional script.. Enjoy!
