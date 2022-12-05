

# arcpy.env.overwriteOutput = True
# workspace_location = str(input("Please enter the folder location of the workspace here:\n"))
# concat_workspace_location = workspace_location + "\surveyingcalculator.gdb"

# SurveyCalculator = concat_workspace_location

import arcpy

def Model():  # Model

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True
    
    workspace_location = str(input("Please enter the folder location of the workspace here:\n"))

    locations_csv = "H:\ProblemSolvingProject\groupproject\\file_name2.csv"

    SurveyCalculator = workspace_location + "\surveyingcalculator.gdb" # "H:\ProblemSolvingProject\groupproject\grpproj_PSP\grpproj_PSP.gdb"

    # Process: XY Table To Point (XY Table To Point) (management)
    locations_XYTableToPoint = "H:\ProblemSolvingProject\groupproject\grpproj_PSP\grpproj_PSP.gdb\\locations_XYTableToPoint"
    with arcpy.EnvManager():
        arcpy.management.XYTableToPoint(in_table=locations_csv, out_feature_class=locations_XYTableToPoint, x_field="Xlist", y_field="Ylist", z_field="", coordinate_system="GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

    # Process: Table To Geodatabase (Table To Geodatabase) (conversion)
    SurveyCalculator_gdb = arcpy.conversion.TableToGeodatabase(Input_Table=[locations_csv], Output_Geodatabase=SurveyCalculator)[0]

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"H:\ProblemSolvingProject\groupproject\grpproj_PSP\grpproj_PSP.gdb", workspace=r"H:\ProblemSolvingProject\groupproject\grpproj_PSP\grpproj_PSP.gdb"):
        Model()
