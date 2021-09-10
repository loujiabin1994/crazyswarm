from console import Console
import numpy as np
import airsim

if __name__ == "__main__":
    con = Console("192.168.0.104")
    # center = airsim.Vector3r(0, 0, 0)
    # p = np.array(con.sim_server.simCreateVoxelGrid(center, 10, 10, 4, 0.1, "111")) * 0.1
    con.publish_pcl()
    # con.takeoff(duration=2, height=1)
