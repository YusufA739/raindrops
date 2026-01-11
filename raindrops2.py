import random,sys,time,os
from colorama import Fore, Back, Style
current = ""
lengthofraindrop = []
for carrier in range(238):#you're gonna have to manually get this
    lengthofraindrop.append(random.randint(-100,10))
while True:
    current = ""
    for i in range(238):
        if lengthofraindrop[i] > 0:
            current += "1"
            lengthofraindrop[i] -= 1
        elif lengthofraindrop[i] <= -100:
            current += "0"
            lengthofraindrop[i] = random.randint(0,10)
        else:
            current += "0"
            lengthofraindrop[i] -= 1

    for carrier in range(238):
        if lengthofraindrop[carrier] > 0:
            sys.stdout.write(Fore.GREEN+current[carrier])
        else:
            sys.stdout.write(Fore.BLACK+current[carrier])
        time.sleep(0.0001)