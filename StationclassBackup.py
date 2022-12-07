Xlist = []
Ylist = []

StationClass = str(input("Do you have Coordinates for this Station? (Y for Yes, Any Other Input Will be Assumed to be No.) : ")) # Turning points in test values don't necessarily have coordinate points, in such cases they will be hidden for intermittent calculations.
if StationClass == "Y" or StationClass == "y": # Makes lower case y inputs work

    x = float(input("The Northing of the station: ")) 
    Xlist.append(x)	# adds the latitude to the list

    y = float(input("The Easting of the station: ")) 
    Ylist.append(y)	# adds the longitude to the list

else:
    x = "<Null>"
    Xlist.append(x)
    y = "<Null>"
    Ylist.append(y)