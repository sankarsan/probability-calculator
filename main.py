from probability_calculator import prob_calculator as pc

hat = pc.Hat(black=6, red=4, green=3)
probability = pc.experiment(hat=hat,
                            expected_balls={"red": 2, "green": 1},
                            num_balls_drawn=5,
                            num_experiments=3)
print("Probability:", probability)