import os
from time import sleep
open('/home/clover/catkin_ws/src/clover/clover/launch/aruco.launch','w').write(open('data/launch/aruco.launch','r').read())
open('/home/clover/catkin_ws/src/clover/clover/launch/clover.launch','w').write(open('data/launch/clover.launch','r').read())
os.system('mv data/model/* /home/clover/catkin_ws/src/clover/clover_simulation/models/')



