from fairino import Robot
import time


def main():
    # Establish connection with the robot controller
    robot = Robot.RPC('192.168.58.2')
    time.sleep(0.5)  # Wait for connection and data reception

    print("========== Gripper Motion Done Test ==========")

    # Open the gripper
    rtn = robot.MoveGripper(2, 50, 50, 100, 30000, 0, 0, 0, 0, 0)
    print(f"MoveGripper(open) ret={rtn}")
    time.sleep(2)
    rtn, pkg = robot.GetRobotRealTimeState()
    print(f"gripper_motiondone {pkg.gripper_motiondone}")

    # Close the gripper
    rtn = robot.MoveGripper(2, 90, 100, 100, 30000, 0, 0, 0, 0, 0)
    print(f"MoveGripper(close) ret={rtn}")
    time.sleep(2)
    rtn, pkg = robot.GetRobotRealTimeState()
    print(f"gripper_motiondone {pkg.gripper_motiondone}")

    # Wait for motion done, no object detected, timeout 5s, stop with error
    rtn = robot.GripperWaitMotionDone(2, 5000, 0, 0)
    print(f"GripperWaitMotionDone(no object detected) ret={rtn}")

    # Loop and query gripper motion status
    while True:
        rtn, status = robot.GetGripperMotionDone()
        print(f"motion status:{status[0]},{status[1]}\n")

        rtn, pkg = robot.GetRobotRealTimeState()
        print(f"error code {pkg.main_code},{pkg.sub_code}")

        time.sleep(0.5)

    # Close connection (never reached due to infinite loop)
    robot.CloseRPC()


if __name__ == "__main__":
    main()