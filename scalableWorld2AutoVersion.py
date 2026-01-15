import scalableWorld2, random

#This is the Auto version of Scalable World 2 by SkySlicer500
#It serves the purpose of generating large amounts of "unique" world entities
#It is most reliable for getting things done quickly but without individuality
#One of the better use cases would be to test the creaation of properties before manually building a world around them

createdProperties = []
createdPropertyValues = []
propertyIndex = 0
createdMaterials = []
materialIndex = 0
createdObjects = []
objectIndex = 0
createdInstances = []

running = False
stepping = False

def toHex(input):
    constants = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    bin = []
    tempIn = input
    while(tempIn > 0):
        bin.append(constants[tempIn % 16])
        tempIn //= 16
    binOut = [bin[x] for x in range(len(bin)-1, -1, -1)]
    return(binOut)

def buildMaterials(buildNumber):
    global createdMaterials, materialIndex
    for x in range(buildNumber):
        materialName = toHex(materialIndex)
        materialIndex += 1
        createdMaterials.append(scalableWorld2.createMaterial(materialName))
def buildObjects(buildNumber):
    global createdObjects, objectIndex
    for x in range(buildNumber):
        objectName = toHex(objectIndex)
        objectMaterial = createdMaterials[random.randint(0, len(createdMaterials)-1)]
        objectSize = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
        objectIndex += 1
        createdObjects.append(scalableWorld2.createObject(objectName, objectSize, objectMaterial))
def buildInstances(buildNumber):
    global createdInstances
    for x in range(buildNumber):
        instanceObject = createdObjects[random.randint(0, len(createdObjects)-1)]
        objectPosition = (random.randint(0, scalableWorld2.worldBoundary), random.randint(0, scalableWorld2.worldBoundary), random.randint(0, scalableWorld2.worldBoundary))
        createdInstances.append(scalableWorld2.instantiateObject(objectPosition, conceptObject=instanceObject))
def createProperties(buildNumber):
    global createdProperties, propertyIndex
    propertyTypes = [int, str, bool]
    for x in range(buildNumber):
        propertyValueType = propertyTypes[random.randint(0, len(propertyTypes)-1)]
        propertyIndex += 1
        createdProperties.append(toHex(propertyIndex))
        createdPropertyValues.append(propertyValueType)
def allocateProperties(buildNumber):
    global createdMaterials
    for x in range(buildNumber):
        materialIndex = random.randint(0, len(createdMaterials)-1)
        propertyIndex = random.randint(0, len(createdProperties)-1)
        if (createdPropertyValues[propertyIndex] == str):
            propertyValue = toHex(random.randint(0, 1000000))
        elif (createdPropertyValues[propertyIndex] == int):
            propertyValue = random.randint(0, 1000000)
        elif (createdPropertyValues[propertyIndex] == bool):
            bools = [True, False]
            propertyValue = bools[random.randint(0, 1)]
        scalableWorld2.applyPropertyToMaterial(createdMaterials[materialIndex], createdProperties[propertyIndex], propertyValue)
def buildProperties(buildNumber):
    comparators = ["==", ">=", ">", "<=", "<", "!="]
    operators = ["=", "+", "-", "*", "/"]
    for x in range(buildNumber):
        actionType = random.randint(0, 1)
        action = [[], [], [], []]
        propertiesUsed = {}
        for y in range(random.randint(2, 15)):
            condition = []
            firstProperty = createdProperties[random.randint(0, len(createdProperties)-1)]
            conditionType = random.randint(1, 3)
            if (conditionType == 1):
                operator = comparators[random.randint(0, len(comparators)-1)]
            else:
                operator = operators[random.randint(0, len(operators)-1)]
            constantVal = 0
            if (random.randint(0, 2) == 0):
                constant = random.randint(0, 1000000)
            elif (random.randint(0, 2) == 1):
                bools = [True, False]
                constant = bools[random.randint(0, 1)]
            elif (random.randint(0, 2) == 2):
                constant = createdProperties[random.randint(0, len(createdProperties)-1)]
                propertiesUsed[constant] = 1
                constantVal = random.randint(1, 2)
            propertiesUsed[firstProperty] = 1
            if (actionType == 0):
                condition = [firstProperty, operator, constant]
            elif (actionType == 1):
                condition = [firstProperty, random.randint(1, 2), operator, constant, constantVal]
            action[conditionType].append(condition)
        action[0] = propertiesUsed.keys()
        if (actionType == 0):
            scalableWorld2.createTickAction(action)
        elif (actionType == 1):
            scalableWorld2.createCollisionAction(action)

def delMaterials(delNumber):
    global createdMaterials
    if (delNumber > len(createdMaterials)):
        delNumber = len(createdMaterials)
    for x in range(delNumber):
        del(createdMaterials[random.randint(0, len(createdMaterials)-1)])
def delObjects(delNumber):
    global createdObjects
    if (delNumber > len(createdObjects)):
        delNumber = len(createdObjects)
    for x in range(delNumber):
        del(createdObjects[random.randint(0, len(createdObjects)-1)])
def delInstances(delNumber):
    if (delNumber > len(createdInstances)):
        delNumber = len(createdInstances)
    for x in range(delNumber):
        instanceNumber = random.randint(0, len(createdInstances)-1)
        del(createdInstances[instanceNumber])
        scalableWorld2.unInstantiateObject(instanceNumber)
def delProperties(delNumber):
    global createdProperties
    if (delNumber > len(createdProperties)):
        delNumber = createdProperties
    for x in range(delNumber):
        #Delete property
        instanceNumber = random.randint(0, len(createdProperties)-1)
        instanceName = createdProperties[instanceNumber]
        del(createdProperties[instanceNumber])
        del(createdPropertyValues[instanceNumber])
        #Delete all tick and collision effects that contained that property
        for y in scalableWorld2.tickActions:
            for z in y[0]:
                if (z == instanceName):
                    del(y)
        for y in scalableWorld2.collisionActions:
            for z in y[0]:
                if (z == instanceName):
                    del(y)
        #Remove properties from materials that contain the property
        for y in createdMaterials:
            if (instanceName in y.keys()):
                y.pop(instanceName)

scalableWorld2.instantiateWorld(random.randint(1, 1000), random.randint(1, 1000))

while True:
    print("Enter a command to create world (help):")
    message = input().split()
    if (running):
        if (message[0] == "step" and stepping):
            scalableWorld2.callStep()
        elif (message[0] == "kill"):
            scalableWorld2.kill()
            running = False
    if (message[0] == "help"):
        print("HELP:\nbuild materials/objects/instances/world ([int] limit) --adds things into existence"
              "\nremove materials/objects/instances ([int] limit) -- removes things from existence"
              "\nrun ([int] stepping 1:True) --starts the world system\nauto ([int] limit) --automatically creates and deletes things in existence")
    elif (message[0] == "build"):
        if (len(message) <= 2):
            buildNumber = 1
        else:
            buildNumber = int(message[2])
        try:
            if (message[1] == "materials"):
                buildMaterials(buildNumber)
            elif (message[1] == "properties"):
                buildProperties(buildNumber)
            elif (message[1] == "objects"):
                buildObjects(buildNumber)
            elif (message[1] == "instances"):
                buildInstances(buildNumber)
            elif (message[1] == "world"):
                scalableWorld2.instantiateWorld(random.randint(1, 1000), random.randint(1, 1000))
        except:
            print("A value passed into build was not a number.")
    elif (message[0] == "remove"):
        if (len(message) <= 2):
            delNumber = 1
        else:
            delNumber = int(message[2])
        try:
            if (message[1] == "materials"):
                delMaterials(delNumber)
            elif (message[1] == "properties"):
                delProperties(delNumber)
            elif (message[1] == "objects"):
                delObjects(delNumber)
            elif (message[1] == "instances"):
                delInstances(delNumber)
        except:
            print("A value passed into remove was not a number")
    elif (message[0] == "run"):
        print("Running the world")
        if (len(message) > 1 and message[1] == 1):
            scalableWorld2.toggleStepping(type=True)
            stepping = True
        else:
            scalableWorld2.toggleStepping(type=False)
            stepping = False
        scalableWorld2.main()
        running = True
    elif (message[0] == "auto"):
        if (len(message[1]) <= 2):
            autoNumber = 1
        else:
            autoNumber = int(message[1])
        for x in range(autoNumber):
            nextAction = random.randint(0, 6)
            if (nextAction == 0):
                buildMaterials(random.randint(1, len(createdMaterials)))
            elif (nextAction == 1):
                buildObjects(random.randint(1, len(createdObjects)))
            elif (nextAction == 2):
                buildInstances(random.randint(1, len(createdInstances)))
            elif (nextAction == 3):
                buildProperties(random.randint(1, len(createdProperties)))
            elif (nextAction == 4):
                delMaterials(random.randint(1, len(createdMaterials)))
            elif (nextAction == 5):
                delObjects(random.randint(1, len(createdObjects)))
            elif (nextAction == 6):
                delInstances(random.randint(1, len(createdInstances)))
            elif (nextAction == 7):
                delProperties(random.randint(1, len(createdProperties)))
    else:
        print("The input command was not recognized")