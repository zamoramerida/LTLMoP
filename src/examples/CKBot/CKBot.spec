# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.
# Note that all values are separated by *tabs*.


======== EXPERIMENT CONFIG 0 ========

Calibration: # Coordinate transformation between map and experiment: XScale, XOffset, YScale, YOffset
0.00391824202523,-1.05182291018,-0.00579735948376,1.16655331908

InitialRegion: # Initial region number
4

InitialTruths: # List of initially true propositions

Lab: # Lab configuration file
CKBot.lab

Name: # Name of the experiment
Default

RobotFile: # Relative path of robot description file
CKBot.robot


======== SETTINGS ========

Actions: # List of actions and their state (enabled = 1, disabled = 0)
None,1

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
CKBot.regions

Sensors: # List of sensors and their state (enabled = 1, disabled = 0)
None,1

currentExperimentName:
Default


======== SPECIFICATION ========

RegionMapping:

r4=p2
others=p1
r1=p5
r2=p4
r3=p3

Spec: # Specification in simple English
Visit r1
Visit r4
Visit r2
Visit r3


