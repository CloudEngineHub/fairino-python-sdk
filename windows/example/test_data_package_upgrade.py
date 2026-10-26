from fairino import Robot
import time


def test_data_package_upgrade(robot):
    """Data package upgrade test"""
    print("\n========== Data Package Upgrade Test ==========")

    time.sleep(0.2)  # 200ms

    # Data package upgrade
    rtn = robot.DataPackageUpgrade("D://zUP/upgrade/FR5/fr_user_data.tar.gz")
    print(f"robot DataPackageUpgrade rtn is {rtn}")

    # Poll upgrade progress until 100%
    upgradeProgress = 0
    while upgradeProgress < 100:
        rtn, upgradeProgress = robot.GetDataPackageUpgradeProgress()
        print(f"robot data package upgrade progress : {upgradeProgress}")
        time.sleep(0.2)  # 200ms


def test_joint_all_param_upgrade(robot):
    """Joint all parameters upgrade test"""
    print("\n========== Joint All Param Upgrade Test ==========")

    # Disable robot before upgrading parameters
    robot.RobotEnable(0)
    time.sleep(0.2)  # 200ms

    # Joint all parameters upgrade
    rtn = robot.JointAllParamUpgrade("D://zUP/upgrade/FR3WMS/jointallparameters.db")
    print(f"robot JointAllParamUpgrade rtn is {rtn}")

    # Poll upgrade progress until 100%
    upgradeProgress = 0
    while upgradeProgress < 100:
        rtn, upgradeProgress = robot.GetJointAllParamUpgradeProgress()
        print(f"robot joint all param upgrade progress : {upgradeProgress}")
        time.sleep(0.2)  # 200ms


def main():
    # Establish connection with the robot controller
    robot = Robot.RPC('192.168.58.2')
    time.sleep(0.5)  # Wait for connection and data reception

    # Run the desired test (uncomment one at a time)
    test_data_package_upgrade(robot)
    # test_joint_all_param_upgrade(robot)

    # Close connection
    robot.CloseRPC()


if __name__ == "__main__":
    main()