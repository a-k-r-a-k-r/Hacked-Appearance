'''
    Program: Hacked Appearance Script 01
    Author : akr
    GitHub : https://github.com/a-k-r-a-k-r
    Blog   : https://a-k-r-a-k-r.blogspot.com
'''

import random
from termcolor import colored
count = 0

while True:
    random_number = random.randint(0,1)
    print(colored(random_number,"green"),end='')
    count+=1
    if (count % 100000 == 0):
        print(colored('You are under attack','red'),end='')