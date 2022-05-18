# senior-thesis
This github repository contains code for the Robot Guided Training:
The Role of the Human Model project.

Brief overview of parts:

NSFExercise:  Work from other project by Paul Gesel.  Used in the conversion of
human data to YuMi data.

yumi_exercise_all_joints.bag:  ROS bag that replays YuMi's Joint State data.
Intended to be played while 32_to_pose.py is active.

HardCodedVideos:  Videos that show the motions of the model hard-coded.

beginner_tutorials:  package that contains Python scripts and other package
necessities.

beta:  Previous versions of scripts and implementations that were later
rewritten to be more object-oriented, or that particular implementation
was discarded.

testing:  Various scripts used to test certain functions of ROS and Unity,
such as publishing Poses and specified rotations around a certain axis.

32_to_pose.py:  Converts Float32MultiArray data into Pose data with proper
transformations.

joint_revised.py:  Class used to create a Joint object.  Contains publishers and
subscribers for each jont as well as math to put data in the correct coordinate
system.

human_parse.py:  Used for a separate implementation that uses human sensor
data to move joints to specified position in global coordinate system.  Used
with data contained in data folder.

unity-zip-links.txt:  Txt containing Google Drive folder to compressed versions
of Unity projects.  This is done to conserve storage on GitHub.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

UNITY SCRIPT DESCRIPTIONS:

CameraSwitch.cs:  Script used to activate specified camera.

HumanShoulderController.cs:  Connected to Axis object that is meant to represent
human motion.

PositionElbowController.cs:  Controls elbow joint on human model when using
Human to Human Model implementation.

PositionShoulderController.cs:  Controls shoulder joint on human model when using
Human to Human Model implementation.

RightWristController.cs:  Controls wrist on human model when using Human to Human
Model implementation.

UpperRightArmController.cs:  Controls the upper right arm when using YuMi to
human model implementation.

LowerRightArmController.cs:  Controls the lower right arm when using YuMi to
human model implementation.

YumiTextInfo.cs:  Calculates and contains the text information that appears
in the corner of the screen.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

DIRECTIONS FOR RUNNING YUMI TO HUMAN MODEL:

1. Clone repository and download Thesis animation zip file.  Unzip the zip.
2. In Linux terminal (or WSL), type hostname -I to get IP address.  Copy.
3. In terminal run roslaunch rosbridge_server rosbridge_websocket.launch address:=(insert copie address here).
4. Open Thesis Animation Project.
5. In the ROSConnector (see object on left side), change the IP address of the port
to the address that was copied earlier, followed by :9090.
6. In another terminal, navigate to the top folder of the directory.
7. Run source devel/setup.bash.
8. Run roscd beginner_tutorials/scripts.
9. Run python 32_to_pose.py.
10.  In Unity, under the ROS connector, uncheck the PositionElbowController,
PositionShoulderController, and RightWristController.
11. Hit the play button in Unity.
12. In another terminal, navigate to the folder that contains yumi_exercise_all_joints.bag.
13. The human model should move.

DIRECTIONS FOR RUNNING HUMAN TO HUMAN MODEL:

1. Follow directions 1-8 in previous set of directions.
2. Run human_parse.py.
3. In Unity, under the ROS connector, uncheck the UpperRightArmController,
LowerRightArmController, and HumanShoulderController.
4. Hit the play button in Unity.
5. The human model should move.
