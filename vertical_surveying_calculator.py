# ╭───────────────────────────────────────────────────────╮ #
# │ Program name: vertical-surveying-program.py           │ #
# │ Beta Testing Date: 2022-12-06                         │ #
# │ Alpha Release Date: 2022-12-07                        │ #
# │ Developed By: Section 61 / Group 2                    │ #
# │ Repository hosted on:                                 │ #
# │ github.com/francis-soriano/vertical-surveying-program │ #
# ╰───────────────────────────────────────────────────────╯ #

# ╭───────────────────────────────────────────────────────╮ #
# │ Developer Comments (updated: 2022-12-07)              │ #
# │ The program has undergone a somewhat intensive beta   │ #
# │ testing scheme, for which some limitations have been  │ #
# │ discovered. They are listed in the limitations section| #
# | of the program, in the INSTRUCTIONS. To check for     | #
# | BLAME, please check the GitHub Repository for code    | #
# | chunks that have corresponding commits to that section| #
# |                                             -fsoriano | #
# ╰───────────────────────────────────────────────────────╯ #

# ╭───────────────────────────────────────────────────────╮ #
# | PROGRAM STARTS HERE                                   | #
# ╰───────────────────────────────────────────────────────╯ #

# first, import modules needed for the program to run. 
import math                                 # 'math' is needed to run trignometric calculations
import csv                                  # '#csv' is needed to receive outputs as .csv file format
import os                                   # 'os' is needed for getcwd (current working directory)
import arcpy                                # arcpy is used for spatial outputs to be used on ArcGIS

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

Limitations:

1) This program only works in Canada as it uses Canadian Spatial Reference System (CSRS) for its projections.
2) This program will only work with metric measurements.
3) This program only uses Universal Transverse Mercator (UTM), so the surveyor using this program must know the Zone and coordinates must be in UTM.
4) Turning Points and Benchmarks can be specified, but coordinates for ALL points are needed to be entered.

--------""")

# ╭───────────────────────────────────────────────────────╮ #
# | Part I. Metadata                                      | #
# ╰───────────────────────────────────────────────────────╯ #

print("""
I. Metadata 

A. Date (date information will be collected using yyyy-mm-dd format)""")

while True:                                 # 'while' loop for basic data validation for year entries
    try:
        metadata_date_yyyy = int(input("Please enter the year of your traverse survey here full four numbers, i.e., 2022):\n\n "))
        if len(str(metadata_date_yyyy)) == 4:
            break
        else:
            print("You have not entered 4 characters for the year.")
    except ValueError:
        print("You have not entered a number for the year. Please try again.")
        continue

while True:                                 # 'while' loop for basic data validation for month entries
    try:
        metadata_date_mm = int(input("Please enter the month of your traverse survey here full two numbers, i.e., '01' for January):\n\n "))
        if 1 <= metadata_date_mm <= 12:     # used a range for values appropriate for number of months in a year
            break
        else:
            print("You have not entered 2 characters for the month. For January, enter '01'.")
    except ValueError:                      # exception catching, only for string entries
        print("You have made an erroneous entry for the month. Please try again. For January, enter '01'.")
        continue


while True:                                 # 'while' loop for basic data validation for day entries
    try:
        metadata_date_dd = int(input("Please enter the day of your traverse survey here full two numbers, i.e., '01' for the first day of the month):\n\n "))
        if 1 <= metadata_date_dd <= 31:     # used a range for values appropriate for days of the month
            break
        else:
            print("You have made an erroneous entry for day. For the first day of the month, enter '01'.")
    except ValueError:                      # exception catching, only for string entries
        print("You have not entered a number for the day. Please try again.")
        continue

metadata_date = str(metadata_date_yyyy) + "-" + str(metadata_date_mm) + "-" + str(metadata_date_dd)

print("B: Crew Members (crew information will be collected using first name [space] last name format)")

while True:                                 # 'while' loop for basic data validation Y/N entries
    metadata_names_question1 = str(input("Would you like to enter the name of a party chief?  (Y / N)\n\n"))
    if metadata_names_question1 in ["Y", "N", "y", "n"]:
        break                               # list above in line 92 is used instead of catching exceptions
    print("Sorry, your input is invalid. Please try again.")

if metadata_names_question1 == "Y" or metadata_names_question1 == "y":
    metadata_names_party_chief = str(input("Please enter the name of the survey party chief here:\n\n"))
elif metadata_names_question1 == "N" or metadata_names_question1 == "n":
    metadata_names_person = []              # list of names for the surveyors
    while True:
        metadata_names_person_input = str(input("Please enter the name of the survey members here:(first name [space] last name format)\n When done, just press 'enter' again to go to the next question.\n\n"))
        if metadata_names_person_input == "":
            break                           # using a NULL entry (or 'enter') to break the loop
        metadata_names_person.append(metadata_names_person_input)

print("C: Equipment")

metadata_equipment_list = []                # list of equipment items

metadata_equipment_input = str(input("Please enter the equipment item here: \n\n"))
metadata_equipment_list.append(metadata_equipment_input)

while True:                                 # data validation for Y/N entries
    metadata_equipment_question1 = str(input("Would you like to enter another equipment item? (Y / N)\n\n"))
    if metadata_equipment_question1.upper() in ["Y", "N", "y", "n"]:
        break                               # same as line 93 comment, list is used instead of catching exceptions
    print("Sorry, your input is invalid. Please try again.")

if metadata_equipment_question1 == "Y" or metadata_equipment_question1 == "y":
    while True: 
        metadata_equipment_input = str(input("Please enter the equipment item here:\n When done, just press 'enter' again to go to the next question\n\n"))
        if metadata_equipment_input == "":
            break                           # same as line 103 comment, using 'enter' to break the loop
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

while True:                                 # data validation for weather entries, had to set as 'str' rather than 'int' due to list condition below
    metadata_weather = str(input("Please enter the weather here:\n\n"))
    if metadata_weather in ["1","2","3","4"]:
        break
    else:
        print("Sorry, that is not a valid number. Please try again.")
        print("""
        From the following choices, please enter what the weather conditions were during the survey:
        1: Sunny/Clear
        2: Cloudy
        3: Precipitative event (rain/snow)
        4: Fog
        Enter only the number that corresponds to the weather.
        """)
if metadata_weather == "1":                 # if statements needed for output: it is easier to data validate numerical entries rather than full text
    metadata_weather = "Sunny/Clear"
elif metadata_weather == "2":
    metadata_weather = "Cloudy"
elif metadata_weather == "3":
    meatadata_weather = "Precipitative event (rain/snow)"
elif metadata_weather == "4":
    metadata_weather = "Fog"

print("For the metadata you have entered:") # summarizing user entries
print("Date of survey:" + str(metadata_date))
if metadata_names_question1 == "Y" or metadata_names_question1 == "y":
    print("Because you opted to name a survey chief, the program only collected their name. Their name is: " + metadata_names_party_chief)
elif metadata_names_question1 == "N" or metadata_names_question1 == "n":
    print("The names you have entered for the survey party are the following: " + str(metadata_names_person))
print("For the equipment, you have entered: " + str(metadata_equipment_list))
print("For the weather, you have entered: " + metadata_weather)
print("The program will now produce a .txt file output for the metadata.")
metadata_txt_filename = str(input("Please enter the name of the .txt file here: \n\n"))
print("The program will now create the .txt file output...")

if metadata_names_question1 == "Y" or metadata_names_question1 == "y":
    metadata_txt_body = f"""
    A. Date of survey: {metadata_date}
    B. Name of Survey Chief: {metadata_names_party_chief}
    C. List of Equipment: {metadata_equipment_list}
    D. Weather: {metadata_weather}
    """
elif metadata_names_question1 == "N" or metadata_names_question1 == "n":
    metadata_txt_body = f"""
    A. Date of survey: {metadata_date}
    B. Name of Surveyor(s): {metadata_names_person}
    C. List of Equipment: {metadata_equipment_list}
    D. Weather: {metadata_weather}
    """
# for the above if-elif statements, f-strings are used to have a simpler .txt output
metadata_txt = open (metadata_txt_filename + ".txt", "w")

metadata_txt.write(metadata_txt_body)       # creating text file for metadata entries

print("""
Text file created in your workspace, depending on where VS Code is run.



The program is now done collecting the metadata for your survey.
The next section of the application is the actual vertical surveying calculator.
""")

# ╭───────────────────────────────────────────────────────╮ #
# | Part II. Calculator                                   | #
# ╰───────────────────────────────────────────────────────╯ #

# Input Section

StartingElevation = float(input("Pleaes enter the Starting Elevation of the Survey: ")) # Creates Starting eleveation as a reference for subsequent calculations
ForesightList = [] # Creates an empty list for Foresight inputs
BacksightList = [] # Creates and empty list for Backsight inputs
Xlist = [] # Creates a list for latitude 
Ylist = [] # Creates a list for longitude
print("Please Enter the Following: ")

try:
    while True: # While Loop goes until the user specifies a break, allowing for traverses of all sizes.
        Foresight = float(input("The Foresight to the next station (If first station leave as 0): ")) 
        ForesightList.append(Foresight) # adds the foresight to the list
    
        Backsight = float(input("The Backsight to the previous station (If last station leave as 0): ")) 
        BacksightList.append(Backsight)	# adds the backsight to the list

        x = float(input("The Northing of the station: ")) 
        Xlist.append(x)	# adds the latitude to the list

        y = float(input("The Easting of the station: ")) 
        Ylist.append(y)	# adds the longitude to the list

        # StationClass = str(input("Do you have Coordinates for this Station? (Y for Yes, Any Other Input Will be Assumed to be No.) : ")) # Turning points in test values don't necessarily have coordinate points, in such cases they will be hidden for intermittent calculations.
        # if StationClass == "Y" or StationClass == "y": # Makes lower case y inputs work

        #     x = float(input("The Northing of the station: ")) 
        #     Xlist.append(x)	# adds the latitude to the list

        #     y = float(input("The Easting of the station: ")) 
        #     Ylist.append(y)	# adds the longitude to the list

        # else:
        #     x = "<Null>"
        #     Xlist.append(x)
        #     y = "<Null>"
        #     Ylist.append(y)
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

# ╭───────────────────────────────────────────────────────╮ #
# | Part III. Output Options                              | #
# ╰───────────────────────────────────────────────────────╯ #

# Exporting values to CSV file 
# Create a function that takes in six lists of values and a file name
def write_to_csv(ForesightList, BacksightList, Xlist, Ylist, PointElevationList, InstrumentHeightList):

    # Create a list of fieldnames
    fieldnames = ['Foresight', 'Backsight', 'Xlist', 'Ylist', 'Elevation', 'InstrumentHeight']

    # Open the file in write mode and create a csv writer
    with open('vertical_survey_calculations.csv', 'w') as csvfile:
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

# ╭───────────────────────────────────────────────────────╮ #
# | Part IV. ArcPy Section                                | #
# ╰───────────────────────────────────────────────────────╯ #

# Setting the workspace

UTMZone = int(input("Please enter your UTM zone: "))  # Gathers the UTM Zone which will be used to project the data in ArcPy, important given our latitude and longitude from our test values are in UTM
workspace_location = str(input("Please enter the file path to the folder location of the workspace here, for example: H:\MyDocuments\ArcGIS\Projects:\n"))
while True:                                 # data validation loop for Y/N entries
    gdb_new_question = str(input("Do you have a geodatabase already? (Y / N)\n"))
    if gdb_new_question in ["Y", "N", "y", "n"]:
        break
    print("Sorry, your input is invalid. Please try again.")

# if a geodatabase already exists, ask for the name of the geodatabase:
if gdb_new_question == "Y" or gdb_new_question == "y":
    gdb_name = str(input("Please set the name of your geodatabase here, without the '.gdb' extension here: \n"))
    gdb_current = str(workspace_location) + "\\" + str(gdb_name) + ".gdb\\"
# if a geodatabase does not exist yet, create a new one:
elif gdb_new_question == "N" or gdb_new_question == "n":
    gdb_name = str(input("Please enter the desired name of your geodatabase here:\n"))
    gdb_current = arcpy.CreateFileGDB_management(workspace_location, gdb_name)

# verify the geodatabase location, will be printed again later when code is run
print("The location of your geodatabase is:")
print(gdb_current)
print("This geodatabase will be the active environment for ArcPy.")
csv_location = workspace_location + "\\vertical_survey_calculations.csv"         # taking saved csv from the workspace location

fc_name = str(input("Please enter the name of the feature class here:\n"))
concat_sr = "NAD_1983_CSRS_UTM_Zone_" + str(UTMZone) + "N"         # specifying the coordinate system, dependent on the UTM Zone entry

sr = arcpy.SpatialReference(concat_sr) 

print(gdb_current)

arcpy.env.overwriteOutput = True
arcpy.env.workspace = str(gdb_current)

arcpy.management.XYTableToPoint(in_table=csv_location, out_feature_class=fc_name, x_field="Xlist", y_field="Ylist", z_field="", coordinate_system=sr)     # IUse XY Table to Point Tool, input is the generated .csv file 

print("Feature class has been created in the geodatabase you have assigned earlier. Please launch ArcGIS Pro and connect the geodatabase you have assigned earlier, or refresh the geodatabase connection.")
