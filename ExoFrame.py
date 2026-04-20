from arm import Arm
from leg import Leg
from torso import Torso

class ExoFrame:
    def __init__(self):
        self.torso = Torso()
        self.left_arm = Arm("Left")
        self.right_arm = Arm("Right")
        self.left_leg = Leg("Left")
        self.right_leg = Leg("Right")

    def move_arm(self, side, joint_name, angle):
        arm = self.left_arm if side.lower() == "left" else self.right_arm
        arm.move_joint(joint_name, angle)

    def move_leg(self, side, joint_name, angle):
        leg = self.left_leg if side.lower() == "left" else self.right_leg
        leg.move_joint(joint_name, angle)

    def move_torso(self, joint_name, angle):
        self.torso.move_joint(joint_name, angle)

    def get_status(self):
        print("=== ExoFrame Status ===")
        print(f"Torso:      {self.torso.joints}")
        print(f"Left Arm:   {self.left_arm.joints}")
        print(f"Right Arm:  {self.right_arm.joints}")
        print(f"Left Leg:   {self.left_leg.joints}")
        print(f"Right Leg:  {self.right_leg.joints}")

    def reset(self):
        for joint in self.torso.joints:
            self.torso.joints[joint] = 0.0
        for joint in self.left_arm.joints:
            self.left_arm.joints[joint] = 0.0
        for joint in self.right_arm.joints:
            self.right_arm.joints[joint] = 0.0
        for joint in self.left_leg.joints:
            self.left_leg.joints[joint] = 0.0
        for joint in self.right_leg.joints:
            self.right_leg.joints[joint] = 0.0
        print("All joints reset to 0.0")
