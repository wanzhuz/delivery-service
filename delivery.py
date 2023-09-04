"""
deliveryService
"""

class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False

class Truck:
    def __init__(self, id, n, loc):
        self.id = id # unique identifier of a truck
        self.size = n # maximum number of packages that can be stored on the truck
        self.location = loc # current location of truck
        self.packages = [] # packages that have been loaded on truck
        self.mileage = 0 # the mileage of a truck


    def collectPackage(self, pk):
        # we can only collect a package if
            # (1) len(self.packages) < self.size
            # (2) self.location = pk.office
        if pk == None:
            return

        if len(self.packages) < self.size and self.location == pk.office:
            if pk.id not in self.getPackagesIds():
                pk.collected = True
                self.packages.append(pk)
        return pk.collected


    def deliverPackage(self, pk):
        # we can only deliver a package if
            # (1) self.location = pk.address
            # (2) the id on the package is the same as pk.id
        # loop through all our packages to deliver them
        if pk == None:
            return

        for i, package in enumerate(self.packages):
            if self.location == pk.address and package.id == pk.id:
                self.packages.pop(i)
                pk.delivered = True
                break
        return pk.delivered


    def deliverPackages(self):
        #To leave the designated parcel at the address
        x = [] #makes a new list to refer to a new variable
        for pk in self.packages:
            x.append(pk)
        for pk in x:
            if pk.address == self.location:
                self.deliverPackage(pk)
        return 
       
    # Don't worry about checking whether the truck is at a post-service office. 
    # The test cases will make sure of that.
    def removePackage(self, pk):
        if pk == None:
            return

        pk.delivered = False
        pk.collected = False
        for i, package in enumerate(self.packages):
            if package.id == pk.id:
                self.packages.pop(i)
        return
        

    def driveTo(self, loc, dist):
        self.mileage += dist
        self.location = loc
        return


    def getPackagesIds(self):
        id = []
        for pk in self.packages:
            id.append(pk.id)
        return id


#returns a list of connections of a location
def createAdjacencyList(map,loc):
    connections = []
    for connection in map:
        if connection[0] == loc:
            connections.append(connection[1])
        elif connection[1] == loc:
            connections.append(connection[0])
    return connections

#returns distance between two locations
def getDistance(map,source,dest):
    for connection in map:
        if connection[0] == source or connection[1]==dest:
            return int(connection[2])
        elif connection[1] == dest or connection[0] == source:
            return int(connection[2])
    return 0

#returns path from source to destination
def findPath(map,source,dest): 
    path = []
    visited=[]
    stack = [(source, [source])]
    while stack:
        loc,path = stack.pop()
        if loc == dest:
            return path
        visited.append(loc)
        adjacencyList = createAdjacencyList(map,loc)
        adjacencyList.sort()
        for item in adjacencyList:
            if item == dest:
                path.append(item)
                return path
            else:
                if item not in visited:
                    stack.append((item, path + [item]))
    return None

def getDistanceOfPath(map,path):
    dist = 0
    for loc in range(1,len(path)):
        dist += getDistance(map,path[loc-1],path[loc])
    return dist


#collects all packages present at current location of truck
def collectPackages(truck,packages):
    for package in packages:
        if not package.collected and not package.delivered:
            truck.collectPackage(package)

def getCollectionOffices(packages):
    offices = []
    for package in packages:
        if package.office not in offices:
            offices.append(package.office)
    return offices

def allPackagesCollected(packages):
    for package in packages:
        if package.collected == False:
            return False
    return True

def allPackagesDelivered(packages):
    for package in packages:
        if package.delivered == False:
            return False
    return True

def getOfficePackages(packages):
    offices = getCollectionOffices(packages)
    officePackages = dict()
    for office in offices:
        collectables = []
        for package in packages:
            if package.office == office:
                collectables.append(package)
        officePackages[office] = collectables
    return officePackages
        
def goToLocation(map,truck,dest,stops):
    path = findPath(map,truck.location,dest)
    if path is not None and not truck.location == dest:
        for loc in path:
            truck.driveTo(dest,getDistance(map,truck.location,loc))
            stops.append(loc)


def deliveryService(map, truck:Truck, packages):
    
    # write your code here
    deliveredTo = dict()
    stops = []
    visitedOffices = []
    
    officePackages = getOfficePackages(packages)
    offices = getCollectionOffices(packages)
    curr_office = truck.location
    while not allPackagesDelivered(packages):
        if curr_office in offices and not allPackagesCollected(officePackages[curr_office]):
            goToLocation(map,truck,curr_office,stops)
            collectPackages(truck,packages)
        else:
            visitedOffices.append(curr_office)
            for office in offices:
                if office not in visitedOffices and office != curr_office:
                    goToLocation(map,truck,office,stops)
                    curr_office = office
                    break
            
        for package in truck.packages:
            loc = truck.location
            dest = package.address
            path = findPath(map,loc,dest)
            for office in path:
                truck.driveTo(office,getDistance(map,loc,office))
                #collect all packages at current location
                collectPackages(truck,packages)
                #Deliver all packages which are to be delivered on current location
                for pack in packages:
                    if pack.address == office:
                        deliveredTo[pack.id] = office
                        truck.deliverPackage(pack)
                            
                            
                
    return (deliveredTo, stops)
