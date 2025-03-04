import csv
gearRatio = 5.0 # geared 50.0x slower
inertia = 0.1 # 10.0 kgm^2 mechanism inertia without gearbox
startVelocity = 0.0 # mechanism starts at 0.0 RPM
distanceToTravel = 305.0 # mechanism must travel 5.0 rotations (without gearbox factored in)
timeStep = 0.1 # simulate numerical approximation every 0.1 seconds

# function to access torque values from csv file
def getTorque(velocity):
    x = csv.reader(open('C:\MotorSimulation\IB Physics Internal Assessment Data - Maxwell Lee - Sheet2.csv', newline=''), delimiter=',', quotechar='|')
    for row in x:
        if float(row[1]) > velocity: # first index is velocity
            return float(row[0]) # zeroth index is torque

# initialize calculation variables
currentPosition = 0.0
currentVelocity = startVelocity
currentTime = 0.0

# main simulation loop
while (currentPosition < distanceToTravel) :
    acceleration = getTorque(currentVelocity * 60 * gearRatio) / inertia / gearRatio
    currentVelocity += acceleration * timeStep
    currentPosition += currentVelocity * timeStep
    currentTime += timeStep
    print(str(round(currentTime,1)) + "s - " + "pos: " + str(round(currentPosition,2)) + " rot - vel: " + str(round(currentVelocity,2)) + " rot/s - accel:" + str(round(acceleration,2)) + " rot/s/s")
print ("when mounted on a " + str((gearRatio)) + ":1 gearbox, the total time for a mechanism with inertia of " + str(inertia) + " kgm^2 to travel " + str(distanceToTravel) + " rotations is " + str(round(currentTime,2)) + " seconds")