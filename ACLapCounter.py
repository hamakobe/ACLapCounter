import sys
import ac
import acsys

l_lapcount=0
lapcount=0
l_speed=0
topspeed=0

def acMain(ac_version):

    global l_lapcount, l_speed, l_fuel, topspeed
    appWindow = ac.newApp("Lap Counter")
    
    ac.setSize(appWindow, 200, 200)

    ac.log("Hello, Assetto Corsa application world!")
    ac.console("Hello Assetto Corsa console!")
    
    l_speed = ac.addLabel(appWindow, "Highest Top Speed: {}".format(topspeed));
    l_lapcount = ac.addLabel(appWindow, "Laps: 0");
    ac.setPosition(l_lapcount, 3, 30)
    ac.setPosition(l_speed, 3, 60)
    
    return "Lap Counter"
    
def acUpdate(deltaT):
    global l_lapcount, l_speed, lapcount, topspeed
    laps = ac.getCarState(0, acsys.CS.LapCount)
    speed = ac.getCarState(0, acsys.CS.SpeedMPH)
    
    if speed > topspeed:
        topspeed = round(speed,2)
        ac.console("Highest Top Speed: {} MPH".format(topspeed))
        ac.setText(l_speed, "Highest Top Speed: {}".format(topspeed))
        
    if laps > lapcount:
        lapcount = laps
        ac.setText(l_lapcount, "Laps: {}".format(lapcount))