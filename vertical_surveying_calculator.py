# ╭───────────────────────────────────────────────────────╮ #
# │ Program name: vertical-surveying-program.py           │ #
# │ Beta Testing Date: 2022-12-06                         │ #
# │ Alpha Release Date: 2022-12-07                        │ #
# │ Developed By: Section 61 / Group 2                    │ #
# │ Repository hosted on:                                 │ #
# │ github.com/francis-soriano/vertical-surveying-program │ #
# ╰───────────────────────────────────────────────────────╯ #

# ╭───────────────────────────────────────────────────────╮ #
# | PROGRAM STARTS HERE                                   | #
# ╰───────────────────────────────────────────────────────╯ #

# first, import modules needed for the program to run. 
import math                         # 'math' is needed to run trignometric calculations
import csv                          # '#csv' is needed to receive outputs as .csv file format
import os                           # 'os' is needed for getcwd (current working directory)
import arcpy                        # arcpy is used for spatial outputs to be used on ArcGIS

# A function to determine elevation and height of the instrument for surverying calculations
def ElevationCalculator(BS, FS, SElev):
    HeightI = SElev + BS
    Elev = HeightI - FS
    return Elev, HeightI

print("""
INSTRUCTIONS:

1) This program will first collect some metadata regarding your survey
2) Then, you will be able to enter your field data values into the calculator
3) Finally, you will have the option to export the entries and results onto a fiel (as a text csv format or other formats for GIS use)

* for "yes" and "no" responses, enter "Y" for yes and "N" for no

--------""")

# ╭───────────────────────────────────────────────────────╮ #
# | Part I. Metadata                                      | #
# ╰───────────────────────────────────────────────────────╯ #

print("""
I. Metadata 

A. Date (date information will be collected using yyyy-mm-dd format)""")

while True:                         # 'while' loop for basic data validation for year entries
    try:
        metadata_date_yyyy = int(input("Please enter the year of your traverse survey here full four numbers, i.e., 2022):\n\n "))
        if len(str(metadata_date_yyyy)) == 4:
            break
        else:
            print("You have not entered 4 characters for the year.")
    except ValueError:
        print("You have not entered a number for the year. Please try again.")
        continue

while True:                         # 'while' loop for basic data validation for month entries
    try:
        metadata_date_mm = int(input("Please enter the month of your traverse survey here full two numbers, i.e., '01' for January):\n\n "))
        if len(str(metadata_date_mm)) == 2:
            break
        else:
            print("You have not entered 2 characters for the month. For January, enter '01'.")
    except ValueError:
        print("You have not entered a number for the month. Please try again.")
        continue


while True:                         # 'while' loop for basic data validation for day entries
    try:
        metadata_date_dd = int(input("Please enter the day of your traverse survey here full two numbers, i.e., '01' for the first day of the month):\n\n "))
        if len(str(metadata_date_dd)) == 2:
            break
        else:
            print("You have not entered 2 characters for the day. For the first day of the month, enter '01'.")
    except ValueError:
        print("You have not entered a number for the day. Please try again.")
        continue

print(" B: Crew Members (crew information will be collected using first name initial, last name format)")

while True:                         # 'while' loop for basic data validation Y/N entries
    metadata_names_question1 = str(input("Would you like to enter the name of a party chief?\n\n"))
    if metadata_names_question1.upper() in ["Y", "N"]:
        break
    print("Sorry, your input is invalid. Please try again.")

if metadata_names_question1 == "Y":
    metadata_names_party_chief = str(input("Please enter the name of the survey party chief here:\n\n"))
elif metadata_names_question1 == "N":
    metadata_names_person = []      # list of names for the surveyors
    while True:
        metadata_names_person_input = str(input("Please enter the name of the survey members here: (first name, last name format)\n When done, just press 'enter' again to go to the next question.\n\n"))
        if metadata_names_person_input == "":
            break
        metadata_names_person.append(metadata_names_person_input)

print("C: Equipment")

metadata_equipment_list = []        # list of equipment items

metadata_equipment_input = str(input("Please enter the equipment item here:\n\n"))
metadata_equipment_list.append(metadata_equipment_input)

while True:                         # data validation for Y/N entries
    metadata_equipment_question1 = str(input("Would you like to enter another equipment item? (Y / N)\n\n"))
    if metadata_equipment_question1.upper() in ["Y", "N"]:
        break
    print("Sorry, your input is invalid. Please try again.")

if metadata_equipment_question1 == "Y":
    while True:
        metadata_equipment_input = str(input("Please enter the equipment item here:\n When done, just press 'enter' again to go to the next question\n\n"))
        if metadata_equipment_input == "":
            break
        metadata_equipment_list.append(metadata_equipment_input)

print("""D: Weather (weather is a choice option, 1 to 4 and the 
temperature in Celsius)

From the following choices, please enter what the 
weather conditions were during the survey:

1: Sunny/Clear
2: Cloudy
3: Precipitative event (rain/snow)
4: Fog

""")

metadata_weather = int(input("Please enter the weather here:\n\n"))

# Output metadata as csv file

### --- will fix --- ###

print("""
The program is now done collecting the metadata for your survey.
The next section of the application is the actual vertical surveying calculator.
""")

# ╭───────────────────────────────────────────────────────╮ #
# | Part II. Calculator                                   | #
# ╰───────────────────────────────────────────────────────╯ #

# Input Section

# these inputs needs to be data validated please!
UTMZone = int(input("Please enter your UTM zone: ")) # Gathers the UTM Zone which will later be used to project the data in ArcPy, important given our latitude and longitude from our test values are in UTM
StartingElevation = float(input("Pleaes enter the Starting Elevation of the Survey: ")) # Creates Starting eleveation as a reference for subsequent calculations
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

    x = float(input("The Northing of the station: ")) 
    Xlist.append(x)	# adds the latitude to the list

    y = float(input("The Easting of the station: ")) 
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
                x = float(input("The Northing of the station: ")) 
                Xlist.append(x)	# adds the latitude to the list
                y = float(input("The Easting of the station: ")) 
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
    print(PointElevationList) # Prints the calculated elevation values
    print(InstrumentHeightList) # Prints the calculated Instrument height values

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
csv_output = write_to_csv(ForesightList, BacksightList, Xlist, Ylist, PointElevationList, InstrumentHeightList)

print("Data in CSV format generated.")

#Part 4 - ArcPy

workspace_location = str(input("Please enter the folder location of the workspace here:\n"))
gdb_name = str(input("Please enter the name of a geodatabase here:\n"))
gdb_current = arcpy.CreateFileGDB_management(workspace_location, gdb_name)
print("The location of your geodatabase is:")
print(gdb_current)
print("This geodatabase will be the active environment for ArcPy.")
csv_location = workspace_location + "\\file_name2.csv"

fc_name = str(input("Please enter the name of the feature class here:\n"))
concat_sr = "NAD_1983_CSRS_UTM_Zone_" + str(UTMZone) + "N"

sr = arcpy.SpatialReference(concat_sr) 

print(gdb_current)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = str(gdb_current)

arcpy.management.XYTableToPoint(in_table=csv_location, out_feature_class=fc_name, x_field="Xlist", y_field="Ylist", z_field="", coordinate_system=sr)

print("Feature class has been created in the geodatabase you have assigned earlier. Please launch ArcGIS Pro and connect the geodatabase you have assigned earlier, or refresh the connection.")
