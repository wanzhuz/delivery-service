# Delivery Service
<strong>Overview: </strong>Simulate a delivery truck service

### Task
The task is to simulate a delivery truck. Each truck starts out empty but with a map with the addresses of the post service offices and the possible places it might need to deliver to. 
The truck is supposed to pick up all packages from the post service offices and deliver all the packages (but not necessarily in that order). The truck also knows what packages there are in each post service office.
Each package has an address and a name to which the package should be delivered. The goal is to pick up and deliver all packages.

#### Package
The Package class has only one method, the constructor. Each package is initialized with a unique identifier id and has four attributes:
- id (a string with only numeric characters) for the package’s unique identifier.
- address (a string) for the address to which the package is supposed to be delivered.
- office (a string) for the address of a post-service office: if a package is not collected, then the
attribute refers to the office where the package is; otherwise, it refers to from which office the
package is collected.
- ownerName (a string) for the name to which the package is supposed to be delivered, and
- delivered (a Boolean) for indicating if the package is delivered or not.
- collected (a Boolean) for indicating if the package is collected by a truck or not.

#### Truck
A truck has the following attributes:
- id (a string with only numeric characters): the unique identifier of a truck.
- size (a non-negative integer): the size of the truck, i.e., the maximum number of packages can be
stored in a truck (assuming all packages are of the same volume).
- location (a string): the current location of a truck.
- packages: the packages that have been loaded in a truck.
- mileage: the mileage of a truck.

#### Methods
The methods you need to define include the followings.
- __init__(self, id, n, loc): Each truck is initialized with a unique identifier id, a size n and a location
loc. No matter what type you choose for the collection of packages in a truck, it should be initalized
to be empty.
- collectPackage(self, pk): collect a package pk (an instance of Package), i.e., add to pk to self.packages.
The truck and pk must be at the same post service office for the truck to be able to collect the
package.
- deliverPackage(self, pk): deliver the pckage pk.
The truck has to be at the address specified by pk.address to be able to deliver the package.
- deliverPackages(self): deliver all packages that are supposed to be delivered to truck’s current
location.
- removePackage(self, pk): remove the package pk from the truck and put it back to a post service office
without delivering it. The truck must be at a post-service office for this to work and the removed
package will be at the post-service office afterwards.
- driveTo(self, loc, dist): drive from current location to location loc. The distance from the cur-
rent location to loc is also provided in the parameter: dist and it needs to be added to the truck’s
mileage attribute for record keeping.
- getPackagesIds(self): return a Python list of the ids of the packages in self.packages.
