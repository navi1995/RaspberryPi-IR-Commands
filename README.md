# Python Infrared Remote LIFX Control for Raspberry Pi

# Usage

Intended to be for personal use in my home. Personalise as you require.
sensor.py holds the code for retrieving HEX/Binary identifiers of which buttons on a remote was pressed. 
infrared.py will listen for button presses and run specified functions (in variable Buttons)
buttons.py has all the functions I use to run when a button has been pressed with a variety of uses with LIFX lights. I use the Lifx cloud API for this.

index.js is a seperate node.js app which I am using to hit an endpoint on my desktop PC locally which turns off my PC for a specified button press. 

Replace API key with your own. 

Raspberry Pi Receiver I use: https://www.jaycar.co.nz/5mm-infrared-receiver/p/ZD1952
