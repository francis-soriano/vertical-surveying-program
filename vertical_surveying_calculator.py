# Program name: vertical-surveying-program.py
# Date of first released version: 2022-11-XX
# Developed by: Section 61 / Group 2

# Repository location (hossted by github): github.com/francis-soriano/vertical-surveying-program

# --------------- PROGRAM STARTS HERE ---------------
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

# --------------- Part I: Metadata ---------------

print("""I. Metadata

A. Date (date information will be collected using
yyyy-mm-dd format)
""")

# fsoriano: need to run the chunk of code below inside a try statement
# that would show "data validation" in our program. honestly certain
# chunks of code should be run in try statements. i'm a little suspicious
# if Karen will try and break the code with erroneous entries lol

metadata_date_yyyy = int(input("""Please enter the year of your traverse survey here 
(full four numbers, i.e., 2022): """))
metadata_date_mm = int(input("""Please enter the month of your survey traverse here 
(numbers only, 01 for January): """))
metadata_date_dd = int(input("""Please enter the day of your survey traverse here
(numbers only, 01 for first day of the month): """))

print(""" 
B: Crew Members (crew information will be collected 
using first name initial, last name format)
""")

# fsoriano: need to loop into a tuple. 
# first tuple is last name, second tuple is first name.
# tbh idk, can be a list too.

# -------------- Design Document Specifications ---------------
# | Please enter the first name initial of the survey         |
# | party chief here: XXXXXXXXXXXX                            |
# | Please enter the last name of the survey party chief      |
# | here: XXXXXXXXXXXX                                        |
# | Did you want to add more crew members? (Y / N) X          |
# -------------------------- E N D ----------------------------

print("C: Equipment")

# fsoriano: part C also needs to get looped into a tuple/list.
# maybe we can do up a function so that we don't crowd the code? 

# -------------- Design Document Specifications ---------------
# | Please enter the equipment item here: XXXXXXXXXXXX        |
# | Did you want to enter another equipment item? (Y / N) X   |
# -------------------------- E N D ----------------------------

# fsoriano: part D *also* needs to get looped into a tuple/list.
# plz consult design document thanks (i got too lazy to copy and
# paste the design document lol)

print("""D: Weather (weather is a choice option, 1 to 4 and the 
temperature in Celsius)

From the following choices, please enter what the 
weather conditions were during the survey:

1: Sunny/Clear
2: Cloudy
3: Precipitative event (rain/snow)
4: Fog

""")


# PART II: Actual Calculator

# PART III: Output Options