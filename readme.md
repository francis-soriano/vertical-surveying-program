# Vertical Surveying Program
## PSP Group Project Section 61 / Group 2
### Jose Augustine (josaugus), Sam Pethick (sapethic), Francis Soriano (fsoriano), Suruchi Tolia (stolia)

Last Updated: November 30, 2022.

This markdown document is kept for documentation purposes as well as to provide a preface to the program being developed by the group for GEOM 67: Problem Solving and Programming at Fleming College (Fall 2022). 

#### Design Document Comments from Karen:
Requirements Comments: 
- Output section mentions a csv and on screen but not a feature class.
- Any other limitations than metric?
- What "relevant error data" will be included?
- Whtat degree of error is expected?

Specification Comments:
- Some sections are missing. The user needs to enter the starting elevation and the error information needs to be displayed.
- Will the wording of the prompt message for crew member names change after the party chief (as they can't all be party chiefs)?
- For the Station section, the height of instrument should not be entered by the user. Instead calculate it using the backsight to a station and the elevation of that station.  When the station is the starting Benchmark, only the elevation of the benchmark and the back sight are appropriate. For the last Station, only the foresight is appropriate. The program should then calculate the elevation using the height of instrument which the program would have calculated from the elevation of the previous station and the backsight to the previous station.
- Will a shapefile be used or a geodatabase feature class for the traverse export? The requirements mention a feature layer in a file geodatabase.

Algorithm Comments:
- How is the arithmetic check calculated?
- Include output to csv and feature class.

#### Program Purpose:

 -  simplify and make the vertical surveying module from survey camp 2022 more efficient by automating it
 - generate map outputs appropriate for map-communication
 - use ArcPy module to create useable file outputs for ArcGIS environments

## Relevant Information Regarding Coursework:
### Dates:

 - ~~-Design Document (Week 11, Nov 16 Wednesday)~~ *Already submitted*
 - Implementation Document (Week 14, Dec 7 Wednesday)
 - Peer Review (probably also Week 14, Dec 7 Wednesday)
 
 ### Links
 - [General project document](https://fleming.desire2learn.com/d2l/le/content/179994/viewContent/2198710/View)
 - [Design rubric document](https://fleming.desire2learn.com/d2l/le/content/179994/viewContent/2198712/View)
 - [Implementation rubric document](https://fleming.desire2learn.com/d2l/le/content/179994/viewContent/2198722/View)