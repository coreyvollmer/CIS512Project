#This class acts as a function caller, within the Main function.
#CDI from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
#BRF from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system
#cost data https://www.bls.gov/cps/tables.htm
#
# Corey Vollmer's CIS 512 Project
# Version: 0.03
# Last Updated: 11/27/2017
#
import CDIReader, BRFReader #Created classes for functions
import time

def Main():
    start = time.time() #start global execution timer

    cdiReader = CDIReader
    brfReader = BRFReader

    #This function prints row details that show a relatively easy to read view of only overall statistics about health habits
    #Many rows contain subset data which are not as valuable as overall
    #Row count, Year,State,Question,Data Value,Low Confidence Limit, High Confidence Limit, Sample Size

    print("Behavioral Risk Factor Surveillance Survey Analysis Results:")
    brfReader.printValuableLines()
    print("---")
    print("End of BRFSS")
    print("---")

    #This function prints row details on overall activity limiting conditions

    print("Chronic Disease Indicator Analysis Results:")
    cdiReader.printOverallNYRows()

    #write cleaned NY File, non null, non repeated cells from original dataset
    #cdiReader.NYfileWriter()

    #Print out each unique question
    #cdiReader.printUniqueColumnValues(6)




    #read CSV/NCAO-BRFSS.csv and print cleaned non null lines.
    #brfReader.readAndPrint()



    #brfReader.printUniqueColumnValues(10)
    #brfReader.writeCleanedCSVFile()
    #brfReader.printTopTenPercentColumns()
    # create variables for doing analysis
    #CDI = [dict() for x in range(reader.getNYLineCount())]
    #CDI.append("test")

    end = time.time() #mark end time of main execution and then report

    print("Executed in "+ str(round(end - start,3)) + " seconds.")

#This starts Main program execution
if __name__ == "__main__":
    Main()