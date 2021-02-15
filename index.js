var engine  = require('clap-trigger');
// var request = require('request');
const Lifx  = require('node-lifx-lan');
const API = "";
var options = {
	method: 'POST',
	json: true,
	data: {"selector": "all"},
	url: 'https://api.lifx.com/v1/lights/all/toggle',
	headers: {
	  'Authorization':'Bearer ' + API
	}
};
var trigger = new engine(); // options here
var on = true;

trigger.start(function(){
  console.log("start")
});

function checkLightStates() {
	Lifx.discover(0).then(function(deviceList) {
		console.log(deviceList)
		var firstLight = deviceList[0];

		if (!firstLight) return {};
		else return firstLight.deviceGetPower();
	}).then(function(isPowered) {
		if (isPowered.level == 1) {
			on = true;
		} else {
			on = false;
		}
	});
}

checkLightStates();
setInterval(checkLightStates, 120000); //2 minutes

//Don't turn off strip
trigger.clap(function() {
	console.log("Clap");

	if (!on) {
		Lifx.turnOnBroadcast();
		on = true;
	} else {
		Lifx.turnOffBroadcast();
		on = false;
	}	
});