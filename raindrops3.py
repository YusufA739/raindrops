import random,sys,time,os
from colorama import Fore, Back, Style
current = ""
currentframe = []
currentframelengthofraindrop = []
lengthofraindrop = []

#manually get screen width from user. They copy and paste one line and we use count to detect the cells per row
for carrier in range(500):
    sys.stdout.write("0")


#change these to change frame size
#linesperframe = 55#55x209 for fullscreen command prompt for my pc
#cellsperline = 222
linesperframe = int(input("type in your height:"))
cellsperline = len(input("use this to calibrate your width and paste the line length:"))

#change these to alter the length of raindrops and the length in between new raindrops in the same column
lowestvalue = -1000#increasing the spacing between raindrops in the same column
stopvalue = 0#value to signify the "stop" length of a raindrop, within lowest value and highest value range
highestvalue = 10#max len of raindrops

#change these to change what numbers appear in the raindrops
lowestraindropnumber = 5
highestraindropnumber = 5

#change to alter line rest time and frame rest time
lineresttime = 0
frameresttime = 0

targetFramerate = 40
currentFramerate = 0

#make the first line
for placeholder in range(cellsperline):#cells per line is given by user input
    lengthofraindrop.append(random.randint(lowestvalue,highestvalue))
    current += str(random.randint(lowestraindropnumber,highestraindropnumber))

#make the first frame using the first line
for i in range(linesperframe):
    currentframe.append(current)
    currentframelengthofraindrop.append(lengthofraindrop.copy())

while True:
    start = time.perf_counter()
    for line in range(linesperframe):
        for cell in range(cellsperline):
            if currentframelengthofraindrop[line][cell] <= 0:
                sys.stdout.write(Fore.BLACK + currentframe[line][cell])
            else:
                color = random.randint(0,1)
                if color == 0:
                    sys.stdout.write(Fore.BLACK + currentframe[line][cell])
                elif color == 1:
                    sys.stdout.write(Fore.GREEN + currentframe[line][cell])
        sys.stdout.write("\n")
        time.sleep(lineresttime)
    time.sleep(frameresttime)
    end = time.perf_counter()
    file = open("framerate.txt","w")
    file.write("Target: "+str(targetFramerate)+"\n"+"Actual: "+str(1/(end-start)))
    file.flush()#will force the buffer to write (quick one) but the file can still be used later on down the code execution
    
    
    current = ""
    lengthofraindrop = currentframelengthofraindrop[0].copy()
    for i in range(cellsperline):
        if lengthofraindrop[i] > stopvalue:
            if highestraindropnumber > lowestraindropnumber:
                current += str(random.randint(lowestraindropnumber,highestraindropnumber))#change to (0,1) for binary
                lengthofraindrop[i] -= 1
            else:
                current += str(lowestraindropnumber)
                lengthofraindrop[i] -= 1
        elif lengthofraindrop[i] <= lowestvalue:
            if highestraindropnumber > lowestraindropnumber:
                current += str(random.randint(lowestraindropnumber,highestraindropnumber))#change to (0,1) for binary
                lengthofraindrop[i] = random.randint(stopvalue,highestvalue)
            else:
                current += str(lowestraindropnumber)
                lengthofraindrop[i] = random.randint(stopvalue,highestvalue)
        else:
            current += str(lowestraindropnumber)
            lengthofraindrop[i] -= 1

    #display current frame
    for carrier in range(linesperframe-1,0,-1):
        currentframe[carrier] = currentframe[carrier-1]
        currentframelengthofraindrop[carrier] = currentframelengthofraindrop[carrier-1].copy()
    
    #finally, update the next frame's first line
    currentframe[0] = current
    currentframelengthofraindrop[0] = lengthofraindrop.copy()

    os.system("cls")