
from pycrazyswarm import Crazyswarm
import sys
from enum import Enum
import rospy

from sensor_msgs.msg import  Joy

TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0
swarm = Crazyswarm()
timeHelper = swarm.timeHelper
cf = swarm.allcfs.crazyflies[0]


class Xbox360Buttons(Enum):
    Green  = 0,
    Red    = 1,
    Blue   = 2,
    Yellow = 3,
    LB     = 4,
    RB     = 5,
    Back   = 6,
    Start  = 7,
    COUNT  = 8,


def callback(data):
    if data.buttons[0] != 0:
        cf.takeoff(targetHeight=0.5, duration=2.5)
        timeHelper.sleep(2.5)
    if data.buttons[1] != 0:
        cf.land(0.05, 3)
        timeHelper.sleep(3)
    if data.axes[0] != 0:
        cf.goTo([data.axes[0]/5, 0, 0], 0, 0.5, relative=True)
        timeHelper.sleep(0.5)
    if data.axes[1] != 0:
        cf.goTo([0, data.axes[1]/5, 0], 0, 0.5, relative=True)
        timeHelper.sleep(0.5)
    if data.axes[3] != 0:
        cf.goTo([0, 0, data.axes[3]/5], 0, 0.5, relative= True)
        timeHelper.sleep(0.5)


def listnner():
    # rospy.init_node('joy_fly', anonymous=True)
    rospy.Subscriber('/joy', Joy, callback, queue_size=1)
    rospy.spin()


if __name__ == '__main__':
    listnner()


