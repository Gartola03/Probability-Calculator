import copy
import random
# Consider using the modules imported above.

class Hat:

    def __init__(self, **args):
        self.contents = []
        for key, value in args.items():
            self.contents += value * [key]
    
    def draw(self, num):
        try:
            balls = random.sample(self.contents, num)
        except:
            balls = copy.deepcopy(self.contents)
        for ball in balls:
            self.contents.remove(ball)

        return balls
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        balls = hat_copy.draw(num_balls_drawn)
        ebal_list = []
        for key, value in expected_balls.items():
            ebal_list += value * [key]
        if contains_ball(ebal_list,balls):
            M += 1

    return M/num_experiments


def contains_ball(expect,draw):
    for i in expect:
        if i in draw:
            draw.remove(i)
        else:
            return False
    return True
