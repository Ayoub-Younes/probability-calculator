import copy
import random

def contents(obj):
    contents = []
    for key, value in obj.items():
            for i in range(value):
                contents.append(key)
    return contents

class Hat:
    def __init__(self, **kwargs):
        self.contents = contents(kwargs)
    def __str__(self):
        return f"contents:{self.contents}"

    def draw(self,num):
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
#-------------------------------------------------------
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    
    def test():
        removed_balls = hat.draw(num_balls_drawn)
        tests = []
        for key, value in expected_balls.items():
            if removed_balls.count(key) >= value:
                tests.append(True)
            else:
                tests.append(False)
        return all(tests)
    for i in range(num_experiments):
        if test(): M += 1
    return M/num_experiments
#------------------------------------------------------


hat = Hat(black=6, red=4, green=3)
print(hat)



print(experiment(hat=hat,expected_balls={"red":2,"green":1}, num_balls_drawn=5, num_experiments=2000))
