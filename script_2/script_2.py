'''
    Program: Hacked Appearance Script 02
    Author : akr
    GitHub : https://github.com/a-k-r-a-k-r
    Blog   : https://a-k-r-a-k-r.blogspot.com
'''

import time
import random
import pyfiglet
from termcolor import colored

count = 0
word = pyfiglet.figlet_format("your  \ncomputer  \nis  \nunder  \nattack")

while True:
    random_number = random.randint(0,1)
    print(colored(random_number,"green"),end='')
    count+=1
    if (count % 100000 == 0):
        print(colored("\n"+word,'red'))
        time.sleep(1)