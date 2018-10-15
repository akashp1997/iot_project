import RPi.GPIO as GPIO

import weather, temp, datetime

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

def on():
	GPIO.output(26, GPIO.LOW)

def off():
	GPIO.output(26, GPIO.HIGH)

t = weather.get_temperature()
try:
	while True:
		time_now = datetime.datetime.now()
		if(time_now.minute==0 and time_now.second==0):
			t = weather.get_temperature()
		if(t[0]>=30):
			set_temp = (t[0]*0.9)+(t[1]*0.05)
		else:
			set_temp = (t[0]*1.1)+(t[1]*0.05)
		read = temp.read_temp()
		print(set_temp, read)
		if(set_temp>read):
			on()
		else:
			off()
except KeyboardInterrupt:
	off()
