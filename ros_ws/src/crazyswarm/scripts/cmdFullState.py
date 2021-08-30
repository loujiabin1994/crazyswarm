#!/usr/bin/env python

import numpy as np

from pycrazyswarm import *
import uav_trajectory


def executeTrajectory(timeHelper, cf, trajpath, rate=100, offset=np.zeros(3)):
    traj = uav_trajectory.Trajectory()
    traj.loadcsv(trajpath)

    start_time = timeHelper.time()
    while not timeHelper.isShutdown():
        t = timeHelper.time() - start_time
        if t > traj.duration:
            break

        e = traj.eval(t)
        cf.cmdFullState(
            # (e.pos + np.array(cf.initialPosition) + offset),
            (e.pos + offset)/2,
            e.vel/2,
            e.acc/2,
            e.yaw/2,
            e.omega)

        timeHelper.sleepForRate(rate)


if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    cf = swarm.allcfs.crazyflies[0]

    rate = 30.0
    Z = 1

    cf.takeoff(targetHeight=Z, duration=Z+1.0)
    timeHelper.sleep(Z+2.0)
    cf.goTo([2, 0, Z], 0, 2)
    timeHelper.sleep(2)
    executeTrajectory(timeHelper, cf, "sequence_trajectories/7/19.csv", offset=np.array([2, 0, 0.1]))

    cf.notifySetpointsStop()
    cf.land(targetHeight=0.03, duration=Z+1.0)
    timeHelper.sleep(Z+2.0)
