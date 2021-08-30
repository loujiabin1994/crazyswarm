"""Takeoff-hover-land for one CF. Useful to validate hardware config."""

from pycrazyswarm import Crazyswarm
import sys

TAKEOFF_DURATION = 2.5
HOVER_DURATION = 5.0


def main(i):
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[i-1]
    cf.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
    timeHelper.sleep(TAKEOFF_DURATION + HOVER_DURATION)
    cf.land(targetHeight=0.04, duration=2.5)
    timeHelper.sleep(TAKEOFF_DURATION)


# if __name__ == "__main__":
#     main(1)
swarm = Crazyswarm()
timeHelper = swarm.timeHelper
cf1 = swarm.allcfs.crazyflies[0]
# cf2 = swarm.allcfs.crazyflies[1]
cf1.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
# cf1.takeoff(targetHeight=0.5, duration=TAKEOFF_DURATION)
timeHelper.sleep(TAKEOFF_DURATION + 1.0)
cf1.goTo([0, 0, 0.5], 0, 2)
# cf1.goTo([1, 0, 0.5], 0, 2)
timeHelper.sleep(3.0)
# cf1.enableCollisionAvoidance([cf2], [0.5, 0.5, 0.5])
# cf1.enableCollisionAvoidance([cf2], [0.5, 0.5, 0.5])