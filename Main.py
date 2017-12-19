#This class acts as a function caller, within the Main function.
#CDI from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
#BRF from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
#cost data https://www.bls.gov/cps/tables.htm
#
# Corey Vollmer's CIS 512 Project
# Version: 0.03
# Last Updated: 11/27/2017
#
import CDI_Functions, BRF_Functions, CPS_Functions #Created classes for functions
import time

cdiObject = CDI_Functions
brfObject = BRF_Functions
cpsObject = CPS_Functions

cpsObjectList = []
cdiObjectList = []

def Main():
    start = time.time() #start global execution timer

    #insert calls into call list, use key
    # "brfpvl" =  Prints row details that show a relatively easy to read view of only overall statistics about health habits
    # "cdiponyr" = prints row details on overall activity limiting conditions
    # "cpsriv" = reads cps csv file and creates a list of class objects

    #callList = ("brfpvl","cdiponyr");
    callList = ("cpsriv","");

    functionCallListHandler(callList);

    #print(cpsObjectList[0].name)
    #cpsObject.reportTopIndustries(cpsObjectList)
    #cpsObject.reportAllVariables(cpsObjectList)

    # create variables for doing analysis
    #CDI = [dict() for x in range(reader.getNYLineCount())]
    #CDI.append("test")

    end = time.time() #mark end time of main execution and then report

    print("Executed in "+ str(round(end - start,3)) + " seconds.")


#This is the controller for handling runtime calls. This enables this program to have modular functionality
def functionCallListHandler(callList):
    for call in callList:
        if(call=="brfpvl"):
            print("Behavioral Risk Factor Surveillance Survey Overall Analysis Results:")
            brfObject.printValuableLines()
            print("---")
            print("End of 'brfpvl' call")
            print("---")

        if(call=="cdiponyr"):
            print("Chronic Disease Indicator Analysis Results:")
            cdiObject.printOverallNYRows()
            print("---")
            print("End of 'cdiponyr' call.")
            print("---")

        if (call == "cdirivl"):
            print("---")
            print("Reading CDI and populating a list of class objects")
            cpsObjectList = cdiObject.readIntoVarList()
            print("End of 'cdiril' call.")
            print("---")

        if(call=="cpsrivl"):
            print("---")
            print("Reading CPS and populating a list of class objects")
            cpsObjectList = cpsObject.readIntoVarList()
            print("End of 'cpsriv' call.")
            print("---")

#This starts Main program execution
if __name__ == "__main__":
    Main()
