
# ------------------------------------------
# 
# 	Project:      Two Sensor Conditions
#	Author:       Mauricio Rodriguez
#	Created:
#	Description:  VEXcode V5 Python Project
# 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
while True:

 if limit_switch_d.pressing() and limit_switch_e.pressing():
        pass
        led_yellow.on()
        led_green.off

else:

        pass
        led_green.on()
        led_yellow.off()
