import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw >= len(self.contents):
            return self.contents
        drawn_balls = random.sample(self.contents, num_balls_to_draw)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count_successful_experiments = 0

    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_balls_count = {}

        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1

        success = True
        for color, count in expected_balls.items():
            if color not in drawn_balls_count or drawn_balls_count[color] < count:
                success = False
                break

        if success:
            count_successful_experiments += 1

    probability = count_successful_experiments / num_experiments
    return probability
