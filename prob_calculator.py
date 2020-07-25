import random


class Hat:
    contents = []

    def __init__(self, **balls):
        for key in balls:
            for i in range(balls[key]):
                self.contents.append(key)

    def draw(self, number_of_balls):

        return self.contents if number_of_balls > len(self.contents) else random.sample(self.contents,
                                                                                        k=number_of_balls)

    def get_contents(self):
        return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match_count = 0
    for i in range(num_experiments):
        flag = False
        balls_drawn = hat.draw(num_balls_drawn)
        print(balls_drawn)
        for key in expected_balls:
            if len(list(filter(lambda x: x == key, balls_drawn))) >= expected_balls[key]:
                flag = True
            else:
                flag = False
                break
        if flag:
            match_count += 1

    return match_count / num_experiments
