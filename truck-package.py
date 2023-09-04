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
        ids = []
        for pk in self.packages:
            ids.append(pk.id)
        return ids

#truck = Truch("123", 10, "office")
#pk1 = Package("1")
#pk1.office = "office"
#pk2.address = "address"

#print(truck.getpackageIds())
