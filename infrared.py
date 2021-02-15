
from buttons import *
from sensor import *

#This will dynamically call a function python for a given infrared remote button press. These functions are assigned in 
#dictionary Buttons.
def buttonPress():
	print("detected")
	inData = convertHex(getBinary()) #Runs subs to get incomming hex value
	if inData in Buttons:
		val = Buttons[inData]

		if callable(val):
			val(inData)
		else:
			print(Buttons[inData]) #Prints corresponding english name for button
	else:
		print ('is out')
		print(inData)
	
	buttonListener()
	


def buttonListener():
	try:
		GPIO.wait_for_edge(18, GPIO.FALLING)
		buttonPress()
	except:
		pass


Buttons = {
	'0x300ffb04f': ON,#'ON',
	'0x300fff807': OFF,#'OFF',
	'0x300ffb847': BRIGHTNESS_DOWN,
	'0x300ff906f': BRIGHTNESS_UP,
	'0x300ff9867': COLOR_BUTTON,#RED_BUTTON,
	'0x300ffd827': COLOR_BUTTON,#GREEN_BUTTON,
	'0x300ff8877': COLOR_BUTTON,#BLUE_BUTTON,
	'0x300ffa857': COLOR_BUTTON,#WHITE_BUTTON,
	'0x300ffe817': TEST,
	'0x300ff02fd': 'RED2',
	'0x300ff50af': 'RED3',
	'0x300ff38c7': 'RED4',
	'0x300ff48b7': 'GREEN1',
	'0x300ff32cd': 'GREEN2',
	'0x300ff7887': 'GREEN3',
	'0x300ff28d7': 'GREEN4',
	'0x300ff6897': 'BLUE1',
	'0x300ff20df': 'BLUE2',
	'0x300ff708f': 'BLUE3',
	'0x300fff00f': 'BLUE4',
	'0x300ffb24d': FLASH,#'FLASH',
	'0x300ff00ff': 'STROBE',
	'0x300ff58a7': 'FADE',
	'0x300ff30cf': 'SMOOTH'
}
buttonListener()