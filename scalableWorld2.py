import json, keyboard, threading

#This is the Scalable World 2 Framework by SkySlicer500
#It serves the purpose of allowing the user to create a world of their own design and play out scenarios by the rules they set

worldSize = None
chunkSize = None
worldBoundary = None
worldChunks = None
stepping = False
nextStep = False
running = None
tickActions = None
collisionActions = None

exampleTickActions = [[
    ["onFire", "burnTime", "maxBurnTime"], #The properties that are required in an object in order to perform the following ticks/collisions
    [["onFire", "==", True], ["burnTime", ">=", "maxBurnTime"]], #If statement
    [["onFire", "=", True], ["burnTime", "=", 0]], #If statement result
    [["burnTime", "+", 1]] #Else statement result (if applicable)
]]
exampleCollisionActions = [[
    ["flammable", "onFire"],
    [["flammable", 1, "==", True, 0], ["onFire", 1, "==", False, 0], ["onFire", 2, "==", True, 0]], #1 = object1, 2 = object2, 0 = not an object / not applicable
    [["onFire", 1, "=", True, 0]],
    []
]]

def instantiateWorld(size, chunk):
    global worldSize, chunkSize, worldBoundary, worldChunks, tickActions, collisionActions
    worldSize = size
    chunkSize = chunk
    tickActions = []
    collisionActions = []

    worldBoundary = worldSize * chunkSize

    worldChunks = []
    for x in range(worldSize):
        worldChunks.append([])
        for y in range(worldSize):
            worldChunks[x].append([])
            for z in range(worldSize):
                worldChunks[x][y].append([])
def toggleStepping(type=None):
    global stepping
    stepping = not stepping
    if (type != None and isinstance(type, bool)):
        stepping = type
    return(stepping)

def createMaterial(name:str) -> dict:
    material = {}
    material["name"] = name
    return(material)
def applyPropertyToMaterial(material:dict, propertyName:str, propertyValue) -> dict:
    material[propertyName] = propertyValue
    return(material)

def createObject(objectName:str, size:tuple[int, int, int], properties:dict) -> dict:
    conceptObject = {}
    conceptObject["name"] = objectName
    conceptObject["size"] = size
    conceptObject["properties"] = properties
    return(conceptObject)
def instantiateObject(position:tuple[int, int, int]=(0, 0, 0), conceptObject:dict=None, instanceName:str=None, size:tuple[int, int, int]=None, properties:dict=None):
    global worldChunks
    worldObject = {}
    positionOfChunk = (position[0]%chunkSize, position[1]%chunkSize, position[2]%chunkSize)
    positionInChunk = (position[0]-positionOfChunk[0]*chunkSize, position[1]-positionOfChunk[1]*chunkSize, position[2]-positionOfChunk[2]*chunkSize)
    worldObject["chunk"] = positionOfChunk
    worldObject["position"] = positionInChunk
    if (conceptObject != None):
        worldObject["name"] = conceptObject["name"]
        worldObject["size"] = conceptObject["size"]
        worldObject["properties"] = conceptObject["properties"]
    if (instanceName != None):
        worldObject["name"] = instanceName
    if (size != None):
        worldObject["size"] = size
    if (properties != None):
        worldObject["properties"] = properties
    worldChunks[positionOfChunk[0]][positionOfChunk[1]][positionOfChunk[2]].append(worldObject)
    return(worldObject)
def unInstantiateObject(worldObject):
    global worldChunks
    for x in worldChunks[worldObject["chunk"][0]][worldObject["chunk"][1]][worldObject["chunk"][2]]:
        if (x == worldObject):
            del(x)

def createTickAction(tickAction):
    global tickActions
    tickActions.append(tickAction)
def createCollisionAction(collisionAction):
    global collisionActions
    collisionActions.append(collisionAction)
def onTick(object):
    for x in tickActions:
        #Ensure all of the neccessary properties are present
        check = False
        for x0 in x[0]:
            if (not x0 in object["properties"].keys()):
                check = True
        if (check):
            continue
        #Check if the if statement provided is true
        continuous = True
        operators = {"==": lambda pv0, pv2: pv0 == pv2, ">=": lambda pv0, pv2: pv0 >= pv2, ">": lambda pv0, pv2: pv0 > pv2, 
                        "<=": lambda pv0, pv2: pv0 <= pv2, "<": lambda pv0, pv2: pv0 < pv2, "!=": lambda pv0, pv2: pv0 != pv2}
        for x1 in x[1]:
            x10 = x1[0]
            if (isinstance(x10, str)):
                x10 = object["properties"][x1[0]]
            x12 = x1[2]
            if (isinstance(x12, str)):
                x12 = object["properties"][x1[2]]
            continuous = continuous and operators[x1[1]](x10, x12)
        #Do the operations
        operators = {"=": lambda pv0, pv2: pv2, "+": lambda pv0, pv2: pv0 + pv2, "-": lambda pv0, pv2: pv0 - pv2,
                        "*": lambda pv0, pv2: pv0 * pv2, "/": lambda pv0, pv2: pv0 / pv2}
        #If the provided if statement is true do the following
        #If the provided if statement is false do the following at 3 instead
        for x2 in x[2+continuous]:
            x22 = x2[2]
            if (isinstance(x22, str)):
                x22 = object["properties"][x2[2]]
            object["properties"][x2[0]] = operators[x2[1]](object["properties"][x2[0]], x22)
def onCollision(object1, object2):
    for x in collisionActions:
        #Ensure all of the neccessary properties are present
        objects = [object1, object2]
        check = False
        for x0 in x[0]:
            if (not x0 in object1["properties"].keys()):
                check = True
            if (not x0 in object2["properties"].keys()):
                check = True
        if (check):
            continue
        #Check if the if statement provided is true
        continuous = True
        operators = {"==": lambda pv0, pv2: pv0 == pv2, ">=": lambda pv0, pv2: pv0 >= pv2, ">": lambda pv0, pv2: pv0 > pv2, 
                        "<=": lambda pv0, pv2: pv0 <= pv2, "<": lambda pv0, pv2: pv0 < pv2, "!=": lambda pv0, pv2: pv0 != pv2}
        for x1 in x[1]:
            x10 = x1[0]
            if (isinstance(x10, str)):
                x10 = objects[x1[1]]["properties"][x1[0]]
            x13 = x1[3]
            if (isinstance(x13, str)):
                x13 = objects[x1[4]]["properties"][x1[3]]
            continuous = continuous and operators[x1[2]](x10, x13)
        #Do the operations
        operators = {"=": lambda pv0, pv2: pv2, "+": lambda pv0, pv2: pv0 + pv2, "-": lambda pv0, pv2: pv0 - pv2,
                        "*": lambda pv0, pv2: pv0 * pv2, "/": lambda pv0, pv2: pv0 / pv2}
        #If the provided if statement is true do the following
        #If the provided if statement is false do the following at 3 instead
        for x2 in x[2+continuous]:
            x23 = x2[3]
            if (isinstance(x23, str)):
                x23 = objects[x2[4]]["properties"][x2[3]]
            objects[x2[1]]["properties"][x2[0]] = operators[x2[2]](objects[x2[1]]["properties"][x2[0]], x23)

def updateChunk(chunk):
    for x in range(len(chunk)):
        xHalfSize = (chunk[x]["size"][0] // 2, chunk[x]["size"][1] // 2, chunk[x]["size"][2] // 2)
        xPosition = chunk[x]["position"]
        for y in range(len(chunk)):
            yHalfSize = (chunk[y]["size"][0] // 2, chunk[y]["size"][1] // 2, chunk[y]["size"][2] // 2)
            yPosition = chunk[x]["position"]

            positionDifference = (abs(xPosition[0] - yPosition[0]), abs(xPosition[1] - yPosition[1]), abs(xPosition[2] - yPosition[2]))
            allowedDifference = (xHalfSize[0] + yHalfSize[0], xHalfSize[1] + yHalfSize[1], xHalfSize[2] - yHalfSize[2])
            if (positionDifference[0] < allowedDifference[0] or positionDifference[1] < allowedDifference[1] or positionDifference[2] < allowedDifference[2]):
                onCollision(chunk[x], chunk[y])
        onTick(chunk[x])
def updateChunks():
    global worldChunks
    for x in worldChunks:
        for y in x:
            for z in y:
                updateChunk(z)
    return(0)

def saveState(stateName:str): #Save world state
    try:
        file = open("saves/"+stateName+".json")
        toWrite = {
            "worldChunks": worldChunks
        }
        json.dump(toWrite, file)
    except:
        print("State file failed to be saved.")
def loadState(stateName:str): #Load world state
    global worldChunks
    try:
        file = json.load(open("saves/"+stateName+".json"))
        worldChunks = file["worldChunks"]
    except:
        print("State file failed to be read.")
def cloneState(stateName:str, cloneName:str): #Create a new file with the same state as another state file
    try:
        file = json.load(open("saves/"+stateName+".json"))
        newFile = open("saves/"+cloneName+".json")
        json.dump(file, newFile)
    except:
        print("State file failed to be cloned.")

def start():
    bootValue = 0
    return(bootValue)
def update():
    if (keyboard.is_pressed('q')):
        return(1)
    returnValue = 0
    returnValue = updateChunks()
    return(returnValue)
def end(exitValue):
    print("World system ended with:", exitValue)
def callStep():
    global nextStep
    nextStep = True
def step():
    global nextStep
    while (not nextStep):
        pass
    nextStep = False
def main():
    global running
    running = threading.Thread(target=trueMain)
    running.start()
def kill():
    if (isinstance(running, threading.Thread)):
        running.join()
def trueMain():
    ask = start()
    while (ask == 0):
        ask = update()
        if (stepping):
            step()
    end(ask)
    return