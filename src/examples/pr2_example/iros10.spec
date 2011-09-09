# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.
# Note that all values are separated by *tabs*.


======== EXPERIMENT CONFIG 0 ========

Calibration: # Coordinate transformation between map and experiment: XScale, XOffset, YScale, YOffset
0.0145090906457,-7.97493804517,-0.0163607845119,5.97177404282

InitialRegion: # Initial region number
0

InitialTruths: # List of initially true propositions

Lab: # Lab configuration file
playerstage.lab

Name: # Name of the experiment
PlayerStage

RobotFile: # Relative path of robot description file
pioneer_stage.robot


======== EXPERIMENT CONFIG 1 ========

Calibration: # Coordinate transformation between map and experiment: XScale, XOffset, YScale, YOffset
0.0111626463135,-6.4486871051,-0.01693824892,6.09812116252

InitialRegion: # Initial region number
2

InitialTruths: # List of initially true propositions

Lab: # Lab configuration file
pr2GazeboRos.lab

Name: # Name of the experiment
ASL

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
iros10.regions

Sensors: # List of sensors and their state (enabled = 1, disabled = 0)
fire,0
person,1
hazardous_item,1

currentExperimentName:
ASL


======== SPECIFICATION ========

RegionMapping:

living=p4
deck=p7
porch=p3
dining=p18,p19
bedroom=p8
others=p9,p10,p11,p12,p13,p14,p15,p16,p17
kitchen=p5

Spec: # Specification in simple English
Env starts with false
Robot starts in deck
If you were in porch then do not person
If you were in porch then do not hazardous_item
Do pick_up if and only if you are sensing hazardous_item and you are not activating carrying_item
Do drop if and only if you are activating carrying_item and you were in kitchen
If you are activating pick_up or you activated pick_up then stay there
If you are activating drop or you activated drop then stay there
Do radio if and only if you are sensing person
If you are activating radio or you activated radio then stay there
If you activated pick_up then do carrying_item
If you activated drop and you did not activate pick_up then do not carrying_item
If you activated carrying_item and you did not activate drop then do carrying_item
If you did not activate carrying_item and you did not activate pick_up then do not carrying_item
If you are not activating carrying_item and you are not activating radio then visit kitchen
If you are not activating carrying_item and you are not activating radio then visit bedroom
always not living
#If you are not activating carrying_item and you are not activating radio then visit living
#If you are not activating carrying_item and you are not activating radio then visit bedroom
If you are not activating carrying_item and you are not activating radio then visit kitchen
If you did not activate carrying_item then always not porch
If you are activating carrying_item and you are not activating radio then visit living


