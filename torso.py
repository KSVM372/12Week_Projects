class Torso:
    def __init__(self):
        #1. Create a dictionary that holds each joint name paired with its current angle (starting at 0)
        self.joints = {"waist": 0.0, "neck": 0.0}
    def move_joint(self, joint_name, angle):
        #1. Save the old angle of the joint
        old_angle = self.joints[joint_name]
        #2. Update the joint's angle to the new angle
        self.joints[joint_name] = angle
        #3. Print a message indicating the joint has moved
        print(f"{joint_name} moved from {old_angle} to {angle}")