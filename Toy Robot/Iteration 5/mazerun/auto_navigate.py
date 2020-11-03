import math

class Navigate:
    
    def __init__(self):
        self.current_angle = 90

    def suggest_movement(self, current, next, angle):
        self.current_angle = int(angle*(180/math.pi))%360
        angle_between_points = self.find_angle_difference(current, next)

        if self.current_angle in [1, 91, 181, 271]:
            self.current_angle -= 1

        # print('angle between is {} and current pos is {} with a next of {}, current_angle is {}'.format(angle_between_points, current, next, self.current_angle))

        if (self.current_angle == 0) and (angle_between_points == 90):
            return ['forward', '1']
        if (self.current_angle == 270) and (angle_between_points == 180):
            return ['forward', '1']
        if (self.current_angle == 180) and (angle_between_points == 270):
            return ['forward', '1']
        if (self.current_angle == 90) and (angle_between_points == 0):
            return ['forward', '1']
        return ['left'] 

    def find_angle_difference(self, point_one, point_two):
        rad = math.atan2(point_two[1]-point_one[1], point_two[0]-point_one[0])
        return int(rad*(180/math.pi))%360