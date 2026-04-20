# Import the Arm, Leg, and Torso classes from their respective files
# so ExoFrame can create and control each body part
from arm import Arm
from leg import Leg
from torso import Torso

# ExoFrame is the main class that represents the full exoskeleton
# It holds all the body parts together and lets you control them from one place
class ExoFrame:

    def __init__(self):
        # Create one Torso (the center of the frame - waist and neck joints)
        self.torso = Torso()
        # Create a left and right Arm (each has shoulder, elbow, and wrist joints)
        self.left_arm = Arm("Left")
        self.right_arm = Arm("Right")
        # Create a left and right Leg (each has hip, knee, and ankle joints)
        self.left_leg = Leg("Left")
        self.right_leg = Leg("Right")

    def move_arm(self, side, joint_name, angle):
        # Pick the correct arm based on the side string ("left" or "right")
        # .lower() makes the check case-insensitive so "Left" and "left" both work
        arm = self.left_arm if side.lower() == "left" else self.right_arm
        # Tell that arm to move the specified joint to the given angle
        arm.move_joint(joint_name, angle)

    def move_leg(self, side, joint_name, angle):
        # Pick the correct leg based on the side string ("left" or "right")
        leg = self.left_leg if side.lower() == "left" else self.right_leg
        # Tell that leg to move the specified joint to the given angle
        leg.move_joint(joint_name, angle)

    def move_torso(self, joint_name, angle):
        # The torso has no left/right so we just pass the joint and angle straight through
        self.torso.move_joint(joint_name, angle)

    def get_status(self):
        # Print a snapshot of every joint angle across the entire exoskeleton
        # Each body part stores its joints as a dictionary {joint_name: angle}
        print("=== ExoFrame Status ===")
        print(f"Torso:      {self.torso.joints}")
        print(f"Left Arm:   {self.left_arm.joints}")
        print(f"Right Arm:  {self.right_arm.joints}")
        print(f"Left Leg:   {self.left_leg.joints}")
        print(f"Right Leg:  {self.right_leg.joints}")

    def reset(self):
        # Loop through every joint in each body part and set its angle back to 0.0
        # This returns the whole frame to its default resting position
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
