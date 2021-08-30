
import numpy as np

from pycrazyswarm import *
import uav_trajectory
step = 0.4

if __name__ == "__main__":
    swarm = Crazyswarm()
    timeHelper = swarm.timeHelper
    allcfs = swarm.allcfs

    traj1 = uav_trajectory.Trajectory()
    traj1.loadcsv("figure8.csv")

    TRIALS = 1
    TIMESCALE =1.0
    for i in range(TRIALS):
        for cf in allcfs.crazyflies:
            cf.uploadTrajectory(0, 0, traj1)
        x_inc = - 2 * step
        y_inc = step
        for each in allcfs.crazyflies:
            if x_inc >= 2* step:
                y_inc -= 0.6    
                x_inc = -2 *step
            pos = np.array(each.initialPosition)/8 + np.array([0, 0, 0.5])+np.array([x_inc, y_inc,0])
            each.goTo(pos, 0, 2.0)
            x_inc += step
            timeHelper.sleep(1.5)

        allcfs.startTrajectory(0, timescale=TIMESCALE)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)
        allcfs.startTrajectory(0, timescale=TIMESCALE, reverse=True)
        timeHelper.sleep(traj1.duration * TIMESCALE + 2.0)

        allcfs.land(targetHeight=0.06, duration=2.0)
        timeHelper.sleep(3.0)
