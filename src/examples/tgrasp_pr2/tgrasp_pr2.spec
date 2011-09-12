# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.
# Note that all values are separated by *tabs*.


======== EXPERIMENT CONFIG 0 ========

Calibration: # Coordinate transformation between map and experiment: XScale, XOffset, YScale, YOffset
0.0111626463135,-6.4486871051,-0.01693824892,6.09812116252

InitialRegion: # Initial region number
3

InitialTruths: # List of initially true propositions

Lab: # Lab configuration file
pr2GazeboRos.lab

Name: # Name of the experiment
Gazebo_pr2

RobotFile: # Relative path of robot description file
pr2_gazebo.robot


======== SETTINGS ========

Actions: # List of actions and their state (enabled = 1, disabled = 0)
pick_up,1
drop,1
radio,1
extinguish,0

Customs: # List of custom propositions
carrying_item

RegionFile: # Relative path of region description file
tgrasp_pr2.regions

Sensors: # List of sensors and their state (enabled = 1, disabled = 0)
fire,0
person,1
hazardous_item,1

currentExperimentName:
Gazebo_pr2


======== SPECIFICATION ========

RegionMapping:

hallway=p6
room1=p5
room4=p2
room2=p4
room3=p3
others=p7,p8,p9,p10

Spec: # Specification in simple English
Env starts with false
Robot starts in room1
If you were in room1 then do not person
If you were in room1 then do not hazardous_item
Do pick_up if and only if you are sensing hazardous_item and you are not activating carrying_item
Do drop if and only if you are activating carrying_item and you were in room1
If you are activating pick_up or you activated pick_up then stay there
If you are activating drop or you activated drop then stay there
Do radio if and only if you are sensing person
If you are activating radio or you activated radio then stay there
If you activated pick_up then do carrying_item
If you activated drop and you did not activate pick_up then do not carrying_item
If you activated carrying_item and you did not activate drop then do carrying_item
If you did not activate carrying_item and you did not activate pick_up then do not carrying_item
If you are not activating carrying_item and you are not activating radio then visit room3


