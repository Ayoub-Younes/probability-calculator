import copy
import random

# Function to generate a list of balls based on input dictionary
def contents(obj):
    contents = []
    for key, value in obj.items():
        for i in range(value):
            contents.append(key)
    return contents

# Hat class definition
class Hat:
    def __init__(self, **kwargs):
        self.contents = contents(kwargs)
        
    def __str__(self):
        return f"contents: {self.contents}"

    # Draw balls from the hat
    def draw(self, num):
        removed_balls = []
        content = self.contents.copy()
        if num <= len(content):
            for i in range(num):
                x = random.choice(content)
                removed_balls.append(x)
                content.remove(x)
            return removed_balls
        else:
            return content

# Experiment function to calculate probability
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    
    # Test if the draw matches expected balls
    def test():
        removed_balls = hat.draw(num_balls_drawn)
        tests = []
        for key, value in expected_balls.items():
            if removed_balls.count(key) >= value:
                tests.append(True)
            else:
                tests.append(False)
        return all(tests)
    
    # Run experiment
    for i in range(num_experiments):
        if test():
            M += 1
    return M / num_experiments

# User interaction to collect inputs and run the experiment
def user_interaction():
    # Get the ball colors and their counts
    print("Enter the colors of the balls in the hat and their quantities (e.g., red=4, blue=3):")
    hat_contents_input = input("Enter the balls in the hat (format: color1=count1,color2=count2,...): ")
    hat_contents_dict = {}
    for pair in hat_contents_input.split(','):
        color, count = pair.split('=')
        hat_contents_dict[color] = int(count)
    
    # Create the Hat object
    hat = Hat(**hat_contents_dict)
    print(f"Created Hat: {hat}")
    
    # Get expected balls to be drawn
    expected_balls_input = input("Enter the expected balls to be drawn (format: color1=count1,color2=count2,...): ")
    expected_balls_dict = {}
    for pair in expected_balls_input.split(','):
        color, count = pair.split('=')
        expected_balls_dict[color] = int(count)

    # Get number of balls to draw and number of experiments
    num_balls_drawn = int(input("Enter the number of balls to draw: "))
    num_experiments = int(input("Enter the number of experiments to perform: "))
    
    # Run the experiment and calculate probability
    probability = experiment(hat, expected_balls_dict, num_balls_drawn, num_experiments)
    
    # Display the result
    print(f"Probability of drawing the expected balls: {probability:.4f}")

# Run the user interaction function
user_interaction()
