#!/usr/bin/env python

import numpy as np
from pycrazyswarm import *
import _thread


Z = 0.3
sleepRate = 30


def goCircle(timeHelper, cf, totalTime, radius, kPosition):
        startTime = timeHelper.time()
        pos = cf.position()
        startPos = pos + np.array([0, 0, Z])
        center_circle = startPos - np.array([radius, 0, 0])
        while True:
            time = timeHelper.time() - startTime
            omega = 2 * np.pi / totalTime
            vx = -radius * omega * np.sin(omega * time)  
            vy = radius * omega * np.cos(omega * time)
            desiredPos = center_circle + radius * np.array(
                [np.cos(omega * time), np.sin(omega * time), 0])
            errorX = desiredPos - cf.position() 
            cf.cmdVelocityWorld(np.array([vx, vy, 0] + kPosition * errorX), yawRate=0)
            timeHelper.sleepForRate(sleepRate)


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf1 = swarm.allcfs.crazyflies[0]
    # cf2 = swarm.allcfs.crazyflies[1]
    cf1.takeoff(targetHeight=Z, duration=1.0+Z)
    # cf2.takeoff(targetHeight=Z, duration=1.0+Z)
    timeHelper.sleep(2 + Z)
    cf1.goTo([0, 0, 0.5], 0, 2)
    # cf2.goTo([1, 0, 0.5], 0, 2)
    timeHelper.sleep(3)
    goCircle(timeHelper, cf1, 4, -0.5, 1))
    # _thread.start_new_thread(goCircle, (timeHelper, cf1, 4, -0.5, 1))
    # _thread.start_new_thread(goCircle, (timeHelper, cf2, 4, 0.5, 1))
            


