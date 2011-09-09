Name: # Full name of the robot
pr2Gazebo

Sensors: # Available binary sensor propositions

Actions: # Available binary actuator propositions

MotionControlHandler: # Module with continuous controller for moving between regions
handlers.motionControl.heatController

DriveHandler:
#handlers.drive.gazeboDrive
handlers.drive.pr2GazeboDrive
