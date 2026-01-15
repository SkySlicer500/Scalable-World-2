import scalableWorld2

#This is the API version of Scalable World 2 by SkySlcier500
#It serves the purpose of acting as an intermediate with another program that intends to use Scalable World 2
#This allows for the collaboration of many individuals, many bots, or the utilization of unique interfaces

createdMaterials = []
createdObjects = []

running = False
stepping = False

nextData = []

def waitForData(type=str):
    global nextData
    if (type == str):
        if (len(nextData) > 0 and isinstance(nextData[0], str)):
            out = nextData[0]
            del(nextData[0])
            return(out)
        inParse = input()
        return(inParse)
    elif (type == int):
        if (len(nextData) > 0 and isinstance(nextData[0], int)):
            out = nextData[0]
            del(nextData[0])
            return(out)
        else:
            nextData = []
        while True:
            try:
                inParse = int(input())
                break
            except:
                print("Non integer input not accepted")
        return(inParse)
    elif (type == bool):
        if (len(nextData) > 0 and isinstance(nextData[0], bool)):
            out = nextData[0]
            del(nextData[0])
            return(out)
        else:
            nextData = []
        while True:
            try:
                inParse = bool(input())
            except:
                print("Non boolean input not accepted")

while True:
    try:
        inParse = waitForData(int)
        if (running):
            if (inParse == 0 and stepping): #Process stepping
                scalableWorld2.callStep()
            elif (inParse == 1):
                scalableWorld2.kill()
                running = False

        if (inParse == -2): #Send help data to requestor
            helpText = ("Help Text:\n-2:Help\n-1:Setup World->int:World Size, int:Chunk Size\n0:Create Material->str:Material Name\n"
                "1:Apply Properties to Materials->int:Material Index, str:Property Name, int:Property Value\n"
                "2:Create Objects->str:Object Name, int:X Size, int:Y Size, int:Z Size, int:Material Index\n"
                "3:Instantiate Objects->int:Object Index, int:X Position, int:Y Position, int:Z Position\n"
                "4:File Manipulation->int:(0:Save, 1:Load), str:File Name\n5:Run World, int:Stepping (1:True)")
            print(helpText)
        elif (inParse == -1): #Set up the world
            inParse1 = waitForData(int)
            inParse2 = waitForData(int)
            scalableWorld2.instantiateWorld(inParse1, inParse2)
        elif (inParse == 0): #Create material
            inParse1 = waitForData(str)
            createdMaterials.append(scalableWorld2.createMaterial(inParse1))
        elif (inParse == 1): #Apply properties to materials
            inParse1 = waitForData(int)
            inParse2 = waitForData(str)
            inParse3 = waitForData(int)
            createdMaterials[inParse1] = scalableWorld2.applyPropertyToMaterial(createdMaterials[inParse1], inParse2, inParse3)
        elif (inParse == 2): #Create objects
            inParse1 = waitForData(str)
            inParse2 = waitForData(int)
            inParse3 = waitForData(int)
            inParse4 = waitForData(int)
            inParse5 = waitForData(int)
            createdObjects.append(scalableWorld2.createObject(inParse1, (inParse2, inParse3, inParse4), createdMaterials[inParse5]))
        elif (inParse == 3): #Instantiate objects
            inParse1 = waitForData(int)
            inParse2 = waitForData(int)
            inParse3 = waitForData(int)
            inParse4 = waitForData(int)
            scalableWorld2.instantiateObject((inParse2, inParse3, inParse4), conceptObject=createdObjects[inParse1])
        elif (inParse == 4): #File Manipulation
            inParse1 = waitForData(int)
            inParse2 = waitForData(str)
            if (inParse1 == 0): #Save
                scalableWorld2.saveState(inParse2)
            elif (inParse1 == 1): #Load
                scalableWorld2.loadState(inParse2)
        elif (inParse == 5): #Run world
            inParse1 = waitForData(int)
            if (inParse1 == 1):
                scalableWorld2.toggleStepping(type=True)
                stepping = True
            else:
                scalableWorld2.toggleStepping(type=False)
                stepping = False
            scalableWorld2.main()
            running = True
        elif (inParse == 6): #Take File
            inParse1 = waitForData(str)
            file = open(inParse1)
            nextData = file.readlines()
        elif (inParse == 7): #Create properties
            inParse1 = waitForData(int)
            action = [[], [], [], []]
            propertiesUsed = {}
            while True:
                condition = []
                inParse3 = waitForData(str)
                inParse4 = waitForData(str)
                inParse5 = waitForData(int)
                if (inParse5 == 0):
                    inParse5 = waitForData(int)
                    if (inParse5 == 0):
                        inParse6 = waitForData(int)
                    else:
                        inParse6 = waitForData(bool)
                else:
                    inParse6 = waitForData(str)
                propertiesUsed[inParse3] = 1
                if (inParse1 == 0):
                    condition = [inParse3, inParse4, inParse6]
                elif (inParse1 == 1):
                    inParse8 = waitForData(int)
                    inParse9 = waitForData(int)
                    condition = [inParse3, inParse8, inParse4, inParse6, inParse9]
                inParse7 = waitForData(bool)
                inParse10 = waitForData(int)
                if (inParse10 >= 0 and inParse10 <= 2):
                    action[inParse10+1].append(condition)
                if (inParse7):
                    break
            action[0] = propertiesUsed.keys()
            if (inParse1 == 0):
                scalableWorld2.createTickAction(action)
            elif (inParse1 == 1):
                scalableWorld2.createCollisionAction(action)
        else: #Send code not found response to requestor
            print("Input code not found")
    except: #Send something went wrong response to requestor
        print("Something went wrong")