
# ------------------------------------------
# 
# 	Project:      Sensor to Actuator
#	Author:       Mauricio Rodriguez & Anthony Bautista
#	Created:
#	Description:  As a distance sensor senses something, motor will stop. 
# ------------------------------------------

# Library imports
from vex import *

# Begin project code
while 1==1:
    pass
    distance = distance_2.object_distance()
    brain.screen.print(distance)
    brain.screen.next_row()
    if 1<=distance<500:
        pass
        motor_1.stop()
    else:
        pass
        motor_1.set_velocity(100, PERCENT)
        motor_1.spin(FORWARD)
