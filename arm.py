class Arm:
    def __init__(self, side):
        #1. Save the side ("Left" or "Right") to self
        self.side = side
        #2. Create a dictionary that holds each joint name
        # paired with its current angle (starting at 0)
        self.joints = {"shoulder": 0.0, "elbow": 0.0, "wrist": 0.0}
    def move_joint(self, joint_name, angle):
        #1. Save the old angle of the joint
        old_angle = self.joints[joint_name]
        #2. Update the joint's angle to the new angle
        self.joints[joint_name] = angle
        #3. Print a message indicating the joint has moved
        print(f"{self.side} {joint_name} moved from {old_angle} to {angle}")