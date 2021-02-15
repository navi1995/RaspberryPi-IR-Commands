
from lifxlan import LifxLAN, Light#RED, WHITE, BLUE, GREEN
import requests
import numpy as np

RED = (65280, 65535, 65535, 3500)
WHITE = (43520, 0, 65535, 5500)
BLUE = (43520, 65535, 65535, 3500)
GREEN = (16128, 65535, 65535, 3500)
lan = LifxLAN()
API = ''
rainbowScene = '8de5780f-e036-4a8c-8482-46612f741815'
stripOnScene = '37ac65ae-7c6b-4e20-b7cf-21a9c512aba8'
strip = Light("d0:73:d5:28:d0:ba", "192.168.0.88")
light1 = Light("d0:73:d5:2a:84:c0", "192.168.0.3")
light2 = Light("d0:73:d5:2a:7c:49", "192.168.0.20")
beam = Light("d0:73:d5:2f:6a:e5", "192.168.0.6")
headers = { 'Authorization':'Bearer ' + API }
			
def ON(self):
	lan.set_power_all_lights("on", rapid=True)

def OFF(self):
	lan.set_power_all_lights("off", rapid=True)

#I want move effect on with rainbow effect. Strip only.
def BRIGHTNESS_DOWN(self):
	if strip.get_power() == 0:
		r = requests.put('https://api.lifx.com/v1/scenes/scene_id:37ac65ae-7c6b-4e20-b7cf-21a9c512aba8/activate', json = { 'fast': True }, headers=headers)
		r = requests.post('https://api.lifx.com/v1/lights/label:Strip/effects/move', json = { 'period': 5, 'power_on': True, 'fast': True }, headers=headers)
	else:
		r = requests.post('https://api.lifx.com/v1/lights/label:Strip/effects/off', json = {'power_off': True, 'fast': True }, headers=headers)

#I want move effect on with rainbow effect. Strip and beam.
def BRIGHTNESS_UP(self):
	if beam.get_power() == 0:
		r = requests.put('https://api.lifx.com/v1/scenes/scene_id:8de5780f-e036-4a8c-8482-46612f741815/activate', json = { 'fast': True }, headers=headers)
		r = requests.post('https://api.lifx.com/v1/lights/label:Beam,label:Strip/effects/move', json = { 'period': 5, 'power_on': True, 'fast': True }, headers=headers)
	else:
		r = requests.post('https://api.lifx.com/v1/lights/label:Beam,label:Strip/effects/off', json = {'power_off': True, 'fast': True }, headers=headers)

def COLOR_BUTTON(hex):	
	colours = {
		'0x300ff9867': RED,
		'0x300ffd827': GREEN,
		'0x300ff8877': BLUE,
		'0x300ffa857': WHITE
	}
	currentColour = light1.get_color()

	#If current light of colour is different, or light is off then toggle ON lights. Else toggle OFF.
	if light1.get_power() == 0 or currentColour != colours[hex]:
		turnOnLights([beam, light1, light2], colours[hex])
	else:
		turnOffLights([beam, light1, light2])

#This endpoint on my desktop PC simply turns off my PC.
def TEST(self):
	try:
		r = requests.get('http://192.168.0.13/api/commands/get', verify=False)
		print(r.text)
	except Exception as e:
		print(e)


def FLASH(self):
	if light1.get_power() == 0:
		turnOnLights([light1, light2], WHITE)
	else:
		turnOffLights([light1, light2])

def turnOffLights(lights):
	for light in lights:
		light.set_power(0, rapid=True)

def turnOnLights(lights, color):
	for light in lights:
		light.set_power(1, rapid=True)
		light.set_color(color, rapid=True)