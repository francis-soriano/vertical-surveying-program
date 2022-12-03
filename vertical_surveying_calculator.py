# Program name: vertical-surveying-program.py
# Date of first released version: 2022-11-XX
# Developed by: Section 61 / Group 2

# Repository location (hossted by github): github.com/francis-soriano/vertical-surveying-program

# --------------- PROGRAM STARTS HERE ---------------
import math
import csv
#import arcpy

# Defines a function to determine elevation and height of the instrument for surverying calculations

def ElevationCalculator(BS, FS, SElev):
    HeightI = SElev + BS
    Elev = HeightI - FS
    return Elev, HeightI


# DO NOT TOUCH THIS SECTION ---------- FSORIANO WILL FIX

print("""
INSTRUCTIONS:

1) This program will first collect some
metadata regarding your survey

2) Then, you will be able to enter your field data
values into the calculator

3) Finally, you will have the option to export the
entries and results onto a fiel (as a text csv format
or other formats for GIS use)

* for "yes" and "no" responses, enter "Y" for yes and
"N" for no

--------""")

# # --------------- Part I: Metadata ---------------

print("""I. Metadata

A. Date (date information will be collected using
yyyy-mm-dd format)
""")

# # fsoriano: need to run the chunk of code below inside a try statement
# # that would show "data validation" in our program. honestly certain
# # chunks of code should be run in try statements. i'm a little suspicious
# # if Karen will try and break the code with erroneous entries lol

while True:
    try:
        metadata_date_yyyy = int(input("""Please enter the year of your traverse survey here full four numbers, i.e., 2022):\n """))
    except ValueError:
        print("You have not entered a number for the year. Please try again.")
        continue
    else:
        break

while True:
    try:
        metadata_date_mm = int(input("""Please enter the month of your survey traverse here (numbers only, 01 for January):\n """))
    except ValueError:
        print("You have not entered a number for the month. Please try again.")
        continue
    else:
        break

while True:
    try:
        metadata_date_dd = int(input("""Please enter the day of your survey traverse here (numbers only, 01 for first day):\n """))
    except ValueError:
        print("You have not entered a number for the day. Please try again.")
        continue
    else:
        break

print(""" 
B: Crew Members (crew information will be collected 
using first name initial, last name format)
""")

# # fsoriano: need to loop into a tuple. 
# # first tuple is last name, second tuple is first name.
# # tbh idk, can be a list too.

# # -------------- Design Document Specifications ---------------
# # | Please enter the first name initial of the survey         |
# # | party chief here: XXXXXXXXXXXX                            |
# # | Please enter the last name of the survey party chief      |
# # | here: XXXXXXXXXXXX                                        |
# # | Did you want to add more crew members? (Y / N) X          |
# # -------------------------- E N D ----------------------------

while True:
    try:
       crew_members_party_chief = str(input("Please enter the first name initial of the survey party chief here:\n"))
    except ValueError:
       print("You have not entered a letter for the first name initial. Please try again.")
    else:
       break

while True:
    try:
       crew_members_more = str(input("Did you want to add more crew members? (Y / N)\n"))
    except ValueError:
       print("You need to answer 'Y' for YES and 'N' for NO. Please try again.")
    else:
       break

# print("C: Equipment")

# # fsoriano: part C also needs to get looped into a tuple/list.
# # maybe we can do up a function so that we don't crowd the code? 

# # -------------- Design Document Specifications ---------------
# # | Please enter the equipment item here: XXXXXXXXXXXX        |
# # | Did you want to enter another equipment item? (Y / N) X   |
# # -------------------------- E N D ----------------------------

# # fsoriano: part D *also* needs to get looped into a tuple/list.
# # plz consult design document thanks (i got too lazy to copy and
# # paste the design document lol)

print("""D: Weather (weather is a choice option, 1 to 4 and the 
temperature in Celsius)

From the following choices, please enter what the 
weather conditions were during the survey:

1: Sunny/Clear
2: Cloudy
3: Precipitative event (rain/snow)
4: Fog

""")

# YOU CAN TOUCH ANYTHING BELOW THIS SECTION ----- FSORIANO WILL DO PART I (METADATA COLLECTION)


# PART II: Actual Calculator

# Input Section

StartingElevation = float(input("Pleaes enter the Starting Elevation of the Survey: ")) # Creates Starting eleveation as a reference for subsequent calculatiions
ForesightList = [] # Creates an empty list for Foresight inputs
BacksightList = [] # Creates and empty list for Backsight inputs
Xlist = [] # Creates a list for latitude 
Ylist = [] # Creates a list for longitude
print("Please Enter the Following: ")

while True:
    Foresight = float(input("The Foresight to the next station (If first station leave as 0): ")) 
    ForesightList.append(Foresight) # adds the foresight to the list
    
    Backsight = float(input("The Backsight to the previous station (If last station leave as 0): ")) 
    BacksightList.append(Backsight)	# adds the backsight to the list

    x = float(input("The Latitude of the station: ")) 
    Xlist.append(x)	# adds the latitude to the list

    y = float(input("The Longitude of the station: ")) 
    Ylist.append(y)	# adds the longitude to the list

    # determine whether user needs to input another station 
    print()
    end = input("Did you have another station (Y/N)? : ")
    print()
    if  end.upper() == 'N' : #Should make it so that lower case n inputs also work
        break
    else:
        try: 
            StationClass = str(input("The Station is a Benchmark rather than a Turning Point? (Y/N): ")) #Turning points in test values don't have coordinate points, in such cases they will be hidden for intermittent calculations.
            if StationClass.upper == "Y": # Makes lower case y inputs work
                x = float(input("The Latitude of the station: ")) 
                Xlist.append(x)	# adds the latitude to the list
                y = float(input("The Longitude of the station: ")) 
                Ylist.append(y)	# adds the longitude to the list
    
            else: 
                print("Coordinates not required for a Turning Point. ")
        except ValueError:
            print("Please Enter an approrpriate Value, Y or N for the Station Class, and a number for Latitude and Longitude. ") # Should refrain from causing a program crash when inputs are mismatched.
                    
# End of Inputs

# Calculations

PointElevationList = [] # Creates an empty list to append calculated elevation into
InstrumentHeightList = [] # Creates an empty list to append calculated height of instrument into

for index in range(0,(len(ForesightList))): # Creates an index within the range of the above inputs
    Foresight = ForesightList[index] # retrieves the Foresight from the list for calculations 
    Backsight = BacksightList[index] # retrives the Backsight from the list for calculations
    Elevation, InstrumentHeight = ElevationCalculator(Backsight, Foresight, StartingElevation) # calls the elevation calculations function to return elevation and Instrument Height
    PointElevationList.append(Elevation) # appends calculated elevation into the Point elevation list
    InstrumentHeightList.append(InstrumentHeight) # appends calculated Instrument Height into the list
    print("test")
    print(PointElevationList)
    print(InstrumentHeightList)

# PART III: Output Options

# Exporting values to CSV file 
# Create a function that takes in six lists of values and a file name
def write_to_csv(ForesightList, BacksightList, Xlist, Ylist, PointElevationList, InstrumentHeightList):

    # Create a list of fieldnames
    fieldnames = ['Foresight', 'Backsight', 'Xlist', 'Ylist', 'Elevation', 'InstrumentHeight']

    # Open the file in write mode and create a csv writer
    with open('file_name2.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Iterate over the lists of values and write each row
        for i in range(len(ForesightList)):
            # Create a dictionary for the current row
            rowdict = {
                'Foresight': ForesightList[i],
                'Backsight': BacksightList[i],
                'Xlist': Xlist[i],
                'Ylist': Ylist[i],
                'Elevation': PointElevationList[i],
                'InstrumentHeight': InstrumentHeightList[i],
            }
            # Write the row to the CSV file
            writer.writerow(rowdict)

    # Print a message indicating that the file was written successfully
    # Call the function to write the lists of values to a CSV file
write_to_csv(ForesightList, BacksightList, Xlist, Ylist, PointElevationList, InstrumentHeightList)

print("Data in CSV format generated.")