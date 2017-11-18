# External module imports
import RPi.GPIO as GPIO
import time
import sys
import config

if len(sys.argv)!=3:
	print "Wrong argument count. Usage: " 
	print "        " + sys.argv[0] + " <machine_name> <command>"
	print "Available commands are:"
	print "         reset"
	print "         power"
	print "         power_4s"
	print "         get_status"
	sys.exit(1)


powerPin = config.POWER_PINS[sys.argv[1]]
resetPin = config.RESET_PINS[sys.argv[1]]
statusPin = config.STATUS_PINS[sys.argv[1]]
command=sys.argv[2]

GPIO.setwarnings(False) 
# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

GPIO.setup(powerPin, GPIO.OUT) 
GPIO.output(powerPin, GPIO.HIGH)

GPIO.setup(resetPin, GPIO.OUT) 
GPIO.output(resetPin, GPIO.HIGH)

GPIO.setup(statusPin, GPIO.IN) 


if command == "reset":
	GPIO.output(resetPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(resetPin, GPIO.HIGH)
elif command == "power":
	GPIO.output(powerPin, GPIO.LOW)
	time.sleep(0.5)
	GPIO.output(powerPin, GPIO.HIGH)
elif command == "power_4s":
	GPIO.output(powerPin, GPIO.LOW)
	time.sleep(4.5)
	GPIO.output(powerPin, GPIO.HIGH)
elif command == "get_status":
	if GPIO.input(statusPin) == 1 :
		status = 0
	else:
		status = 1

	print status
else: 
	print "Unknown command: " + command
	sys.exit(2)

sys.exit(0)

