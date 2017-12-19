#This class acts as a function caller, within the Main function.

#CDI from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
#MUST DOWNLOAD THIS FROM WEBSITE AND PLACE IN FOLDER

#BRF from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
#cost data https://www.bls.gov/cps/tables.htm
#
# Corey Vollmer's CIS 512 Project
# Last Updated: 12/19/2017
#
import CDI_Functions, BRF_Functions, CPS_Functions #Created classes for functions
import time, pandas, matplotlib.pyplot as plt


cdiObject = CDI_Functions
brfObject = BRF_Functions
cpsObject = CPS_Functions

cpsObjectList = []
cdiObjectList = []
brfObjectList = []

def Main():
    start = time.time() #start global execution timer
    #
    # insert calls into call list, use this dictionary below
#   #   #
    # "brfpvl" =  prints row details that show a relatively easy to read view of only overall statistics about health habits
#   #   #
    # "cdiponyr" = prints row details on overall activity limiting conditions
    # "cdirivl" = read cdi csv file and creates a list of class objects
    # "cdippala" = makes a scatter plot for crude prevalence of arthritis over time
    # "cdippalphd" = makes a scatter plot for crude prevalence of COPD over time
    # "cdipral" = makes a bar graph showing mean percentage of recent activity limitations by year
#   #   #
    # "cpsrivl" = reads cps csv file and creates a list of class objects
    # "cpsrip" = reads into pandas
    #   #
    #callList = ("brfpvl","cdiponyr");
    #callList = ("cdirivl","cpsrivl","cdipi");
    callList = ["brfpvl","cdiponyr","cdippala","cdippalphd","cdipral","cpsrivl"]

    #Fix error if list is of size  1.
    if(len(callList) == 1):
        callList.append("")

    #This function runs list of functions declared above.
    functionCallListHandler(callList)

    end = time.time() #mark end time of main execution and then report

    print("Executed in "+ str(round(end - start,3)) + " seconds.")


#This is the controller for handling runtime calls. This enables this program to have modular functionality
def functionCallListHandler(callList):
    for call in callList:
        print("---")
        if(call=="brfpvl"):
            print("Behavioral Risk Factor Surveillance Survey Overall Analysis Results:")
            brfObject.printValuableLines()
            print("End of 'brfpvl' call")

        if (call == "brfpsvl"):
            print("Behavioral Risk Factor Surveillance Survey Overall Analysis Results:")
            brfObject.printSimplifiedValuableLines()
            print("End of 'brfpsvl' call")

        if(call=="cdiponyr"):
            print("Chronic Disease Indicator Analysis Results:")
            cdiObject.printOverallNYRows()
            print("End of 'cdiponyr' call.")

        if (call == "cdirivl"):
            print("Reading CDI and populating a list of class objects")
            cdiObjectList = cdiObject.readIntoVarList()
            print("End of 'cdiril' call.")

        if (call == "cdippala"):
            print("")
            cdiObject.pandasPlotActLimArthritis()
            print("End of 'cdippala' call.")

        if (call == "cdippalphd"):
            print("")
            cdiObject.pandasPlotActLimPHD()
            print("End of 'cdippalphd' call.")

        if (call == "cdipral"):
            print("")
            cdiObject.pandasPlotRecActLim()
            print("End of 'cdipral' call.")

        if(call=="cpsrivl"):
            print("Reading CPS and populating a list of class objects")
            cpsObjectList = cpsObject.readIntoVarList()
            print("End of 'cpsrivl' call.")

        if (call == "cpsrip"):
            print("Reading CPS and populating a list of class objects")
            print("End of 'cpsrip' call.")
        print("---")

#This starts Main program execution
if __name__ == "__main__":
    Main()
