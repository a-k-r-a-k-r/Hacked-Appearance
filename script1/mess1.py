import random
from termcolor import colored
count = 0

while True:
    random_number = random.randint(0,1)
    print(colored(random_number,"green"),end='')
    count+=1
    if (count % 100000 == 0):
        print(colored('You are under attack','red'),end='')