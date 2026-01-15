import scalableWorld2

#This is the Configurable version of Scalable World 2 by SkySlicer500
#It serves the purpose of allowing the creation of a world to ones certain wims
#The ability to design the world exactly as one wants in the image that one seeks

createdMaterials = {}
createdObjects = {}
running = False
stepping = False

def getInput(type=str):
    if (type == str):
        return(input())
    elif (type == int):
        while True:
            try:
                value = int(input())
                return(value)
            except:
                print("Input value was not a number, try again")

def worldCreator():
    print("ENTERED WORLD CREATOR\nWorld Size:")
    worldSize = getInput(int)
    print("Chunk Size:")
    chunkSize = getInput(int)
    scalableWorld2.instantiateWorld(worldSize, chunkSize)
    print("Created world that is", worldSize, "in size and has chunks that are", chunkSize)

def propertyCreator():
    print("ENTERED PROPERTY CREATOR\nTick / Collision:")
    propertyType = getInput()
    if (propertyType == "Tick"):
        tickAction = [[], [], [], []]
        propertiesUsed = {}
        while True:
            print("Condition / If / Else / End:")
            inputType = getInput()
            if (inputType == "Condition"):
                condition = []
                print("Insert name of property to compare:")
                propertyName = getInput()
                propertiesUsed[propertyName] = 1
                condition.append(propertyName)
                print("Insert comparator type (==, >=, >, <=, <, !=):")
                operationType = getInput()
                condition.append(operationType)
                print("Constant / Property:")
                finalVariable = getInput()
                if (finalVariable == "Constant"):
                    print("Int / Boolean")
                    constantType = getInput()
                    if (constantType == "Int"):
                        print("Enter an int:")
                        intConstant = getInput(int)
                        condition.append(intConstant)
                    elif (constantType == "Boolean"):
                        boolSet = {"True":True, "False":False}
                        print("Enter a boolean:")
                        boolConstant = getInput()
                        condition.append(boolSet[boolConstant])
                elif (finalVariable == "Property"):
                    print("Insert property name:")
                    propertyName2 = getInput()
                    propertiesUsed[propertyName2] = 1
                    condition.append(propertyName2)
                tickAction[1].append(condition)
            elif (inputType == "If" or inputType == "Else"):
                statement = []
                print("Insert name of property to adjust:")
                propertyName = getInput()
                propertiesUsed[propertyName] = 1
                statement.append(propertyName)
                print("Insert operation type (=, +, -, *, /):")
                operationType = getInput()
                statement.append(operationType)
                print("Constant / Property:")
                finalVariable = getInput()
                if (finalVariable == "Constant"):
                    if (constantType == "Int"):
                        print("Enter an int:")
                        intConstant = getInput(int)
                        statement.append(intConstant)
                    elif (constantType == "Boolean"):
                        boolSet = {"True":True, "False":False}
                        print("Enter a boolean:")
                        boolConstant = getInput()
                        statement.append(boolSet[boolConstant])
                elif (finalVariable == "Property"):
                    print("Insert property name:")
                    propertyName2 = getInput()
                    propertiesUsed[propertyName2] = 1
                    statement.append(propertyName2)
                if (inputType == "If"):
                    tickAction[2].append(statement)
                elif(inputType == "Else"):
                    tickAction[3].append(statement)
            elif (inputType == "End"):
                break
        tickAction[0] = propertiesUsed.keys()
        scalableWorld2.createTickAction(tickAction)
        print("Created tick action")
    elif (propertyType == "Collision"):
        collisionAction = [[], [], [], []]
        propertiesUsed = {}
        while True:
            print("Condition / If / Else / End:")
            inputType = getInput()
            if (inputType == "Condition"):
                condition = []
                print("Insert name of property to compare:")
                propertyName = getInput()
                propertiesUsed[propertyName] = 1
                condition.append(propertyName)
                print("Which object is the property a part of (1 / 2)")
                objectNum = getInput(int)
                if (objectNum == 1 or objectNum == 2):
                    condition.append(objectNum)
                else:
                    condition.append(0)
                print("Insert comparator type (==, >=, >, <=, <, !=):")
                operationType = getInput()
                condition.append(operationType)
                print("Constant / Property:")
                finalVariable = getInput()
                if (finalVariable == "Constant"):
                    print("Int / Boolean")
                    constantType = getInput()
                    if (constantType == "Int"):
                        print("Enter an int:")
                        intConstant = getInput(int)
                        condition.append(intConstant)
                    elif (constantType == "Boolean"):
                        boolSet = {"True":True, "False":False}
                        print("Enter a boolean:")
                        boolConstant = getInput()
                        condition.append(boolSet[boolConstant])
                    condition.append(0)
                elif (finalVariable == "Property"):
                    print("Insert property name:")
                    propertyName2 = getInput()
                    propertiesUsed[propertyName2] = 1
                    condition.append(propertyName2)
                    print("Which object is the property a part of (1 / 2)")
                    objectNum = getInput(int)
                    if (objectNum == 1 or objectNum == 2):
                        condition.append(objectNum)
                    else:
                        condition.append(0)
                collisionAction[1].append(condition)
            elif (inputType == "If" or inputType == "Else"):
                statement = []
                print("Insert name of property to adjust:")
                propertyName = getInput()
                propertiesUsed[propertyName] = 1
                statement.append(propertyName)
                print("Which object is the property a part of (1 / 2)")
                objectNum = getInput(int)
                if (objectNum == 1 or objectNum == 2):
                    statement.append(objectNum)
                else:
                    statement.append(0)
                print("Insert operation type (=, +, -, *, /):")
                operationType = getInput()
                statement.append(operationType)
                print("Constant / Property:")
                finalVariable = getInput()
                if (finalVariable == "Constant"):
                    if (constantType == "Int"):
                        print("Enter an int:")
                        intConstant = getInput(int)
                        statement.append(intConstant)
                    elif (constantType == "Boolean"):
                        boolSet = {"True":True, "False":False}
                        print("Enter a boolean:")
                        boolConstant = getInput()
                        statement.append(boolSet[boolConstant])
                    statement.append(0)
                elif (finalVariable == "Property"):
                    print("Insert property name:")
                    propertyName2 = getInput()
                    propertiesUsed[propertyName2] = 1
                    statement.append(propertyName2)
                    print("Which object is the property a part of (1 / 2)")
                    objectNum = getInput(int)
                    if (objectNum == 1 or objectNum == 2):
                        statement.append(objectNum)
                    else:
                        statement.append(0)
                if (inputType == "If"):
                    collisionAction[2].append(statement)
                elif(inputType == "Else"):
                    collisionAction[3].append(statement)
            elif (inputType == "End"):
                break
        collisionAction[0] = propertiesUsed.keys()
        scalableWorld2.createCollisionAction(collisionAction)
        print("Created collision action")
    print("EXITING PROPERTY CREATOR")

def materialCreator():
    print("ENTERED MATERIAL CREATOR\nMaterial Name:")
    materialName = getInput()
    createdMaterials[materialName] = scalableWorld2.createMaterial(materialName)
    print("Material", materialName, "created.")

def applyMaterialProperty():
    print("APPLYING PROPERTY TO MATERIAL\nMaterial Name:")
    materialName = getInput()
    print("Property name:")
    propertyName = getInput()
    print("Property value:")
    propertyValue = getInput(int)
    createdMaterials[materialName] = scalableWorld2.applyPropertyToMaterial(createdMaterials[materialName], propertyName, propertyValue)
    print("Material", materialName, "had property", propertyName, "applied at a value of", propertyValue)

def objectCreator():
    print("ENTERED OBJECT CREATOR\nObject Name:")
    objectName = getInput()
    print("Object Size X:")
    x = getInput(int)
    print("Object Size Y:")
    y = getInput(int)
    print("Object Size Z:")
    z = getInput(int)
    print("Material Name:")
    materialName = input()
    properties = createdMaterials[materialName]
    createdObjects[objectName] = scalableWorld2.createObject(objectName, (x, y, z), properties)
    print("Object", objectName, "was created with a size of", x, y, z, "with the properties of", materialName)

def instantiateObject():
    print("ENTERED OBJECT INSTANTIATOR\nObject Name:")
    objectName = getInput()
    print("Object Position X:")
    x = getInput(int)
    print("Object Position Y:")
    y = getInput(int)
    print("Object Position Z:")
    z = getInput(int)
    object = createdObjects[objectName]
    scalableWorld2.instantiateObject((x, y, z), conceptObject=object)
    print("Object", objectName, "was instantiated at", x, y, z)

def saveWorld():
    print("PREPARING TO SAVE THE WORLD\nFile Name:")
    fileName = getInput()
    scalableWorld2.saveState(fileName)
    print("World Saved")

def loadWorld():
    print("PREPARING TO LOAD THE WORLD\nFile Name:")
    fileName = getInput()
    scalableWorld2.loadState(fileName)
    print("World Loaded")

def cloneWorld():
    print("PREPARING TO CLONE THE WORLD\nFile To Clone Name:")
    fileName = getInput()
    print("New File Name:")
    newFile = getInput()
    scalableWorld2.cloneState(fileName, newFile)
    print("World Cloned")

def help():
    print("HELP:\nworld\nmaterial (create/apply)\nobject (create/insantiate)\nfile (save/load)\nrun\n...")

def run():
    global running, tepping
    print("STARTING WORLD SIMULATION\nWould you like to enable stepping?:yes/no:")
    ans = getInput()
    if (ans == "yes"):
        scalableWorld2.toggleStepping(type=True)
        stepping = True
    else:
        scalableWorld2.toggleStepping(type=False)
        stepping = False
    scalableWorld2.main()
    running = True

def step():
    input()
    scalableWorld2.callStep()

def kill():
    global running
    scalableWorld2.kill()
    running = False

while True:
    print("Enter a command to create objects (help):")
    message = input().split()
    if (running):
        if (message[0] == "step" and stepping):
            step()
        elif (message[0] == "kill"):
            kill()
    if (message[0] == "help"):
        help()
    elif (message[0] == "world"):
        worldCreator()
    elif (message[0] == "property"):
        propertyCreator()
    elif (message[0] == "material"):
        if (message[1] == "create"):
            materialCreator()
        elif (message[1] == "apply"):
            applyMaterialProperty()
    elif (message[0] == "object"):
        if (message[1] == "create"):
            objectCreator()
        elif (message[1] == "instantiate"):
            instantiateObject()
    elif (message[0] == "file"):
        if (message[1] == "save"):
            saveWorld()
        elif (message[1] == "load"):
            loadWorld()
        elif (message[1] == "clone"):
            cloneWorld()
    elif (message[0] == "run"):
        run()