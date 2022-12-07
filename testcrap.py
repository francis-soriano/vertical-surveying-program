ForesightList = []
BacksightList = []
Xlist = []
Ylist = []

try:
    while True: # While Loop goes until the user specifies a break, allowing for traverses of all sizes.
        Foresight = float(input("The Foresight to the next station (If first station leave as 0): ")) 
        ForesightList.append(Foresight) # adds the foresight to the list
    
        Backsight = float(input("The Backsight to the previous station (If last station leave as 0): ")) 
        BacksightList.append(Backsight)	# adds the backsight to the list

        StationClass = str(input("Do you have Coordinates for this Station? (Y for Yes, Any Other Input Will be Assumed to be No.) : ")) # Turning points in test values don't necessarily have coordinate points, in such cases they will be hidden for intermittent calculations.
        if StationClass == "Y" or StationClass == "y": # Makes lower case y inputs work

            x = float(input("The Northing of the station: ")) 
            Xlist.append(x)	# adds the latitude to the list

            y = float(input("The Easting of the station: ")) 
            Ylist.append(y)	# adds the longitude to the list

        # Determine whether user needs to input another station       
        print()
        end = input("Did you have another station (Y/N)? : ")
        print()
        if  end.upper() == 'N' : # Should make it so that lower case n inputs also work
            break
except ValueError:
    print("Value Error: Please Enter Appropriate Inputs to our Specifications.")
except TypeError:
    print("Type Error: Please Enter Appropriate Inputs to our Specifications.")
except Exception as message:
    message = "A General Error has occured, Please try rerunning the program."
    print("Error:", message)