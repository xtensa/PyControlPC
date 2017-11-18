# PyControlPC
This is extremely simple Python utility for Raspberry PI to press power or reset button on remote PC using CLI. Power and Reset button pins of the controlled PC should be connected to Raspberry Pi GPIO port as illustrated on the attached schematics (scheme.jpg).

Usage:
	python pcontrol.py <machine_name> <command>

Multiple machines could be configured on different GPIO pins. Edit config.py to change the name or add new controlled machine.

Available commands are:
         reset
         power
         power_4s
         get_status
