import pybullet as p
import time


def main():
    print("Hello from evorobotics!")
    print("Starting PyBullet simulation...")

    # Connect to PyBullet
    physicsClient = p.connect(p.GUI)
    p.setGravity(0, 0, -9.81)

    # Load a plane and a sphere
    planeId = p.loadURDF("plane.urdf")
    sphereStartPos = [0, 0, 1]
    sphereId = p.loadURDF("sphere2.urdf", sphereStartPos)

    # Run simulation for 5 seconds
    for i in range(240):
        p.stepSimulation()
        time.sleep(1./240.)

    p.disconnect()
    print("Simulation complete!")


if __name__ == "__main__":
    main()
