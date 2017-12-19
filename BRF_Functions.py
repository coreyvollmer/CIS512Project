# Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System Reader
# This class contains functions dealing with the CSV/NPAO-BRFSS.csv file.
# CSV Reader and documentation from: https://docs.python.org/3/library/csv.html
# BRF dataset from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system

import csv, pandas, matplotlib.pyplot as plt

#Original dataset from web
dataSetPath="CSV/NPAO-BRFSS.csv"

#Cleaned dataset path
cleanDataSetPath="CSV/BRFSS-Clean.csv"

class BRFReader:
    print("BRF Reader Initialized. Running selected functions in Main...")

#Depreciated
def writeCleanedCSVFile():
    with open(cleanDataSetPath, 'w', newline='') as writecsvfile:
        writer = csv.writer(writecsvfile, delimiter=' ', quotechar="'", quoting=csv.QUOTE_NONE, escapechar=' ')
        #writer = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_NONE, esc')
        rowCount = 0
        fileCounter = 0
        with open(dataSetPath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                fileCounter = fileCounter + 1
                semiCleanedRow = ','.join(row)
                semiCleanedRowCells = semiCleanedRow.split(",")
                #print(semiCleanedRowCells)
                if semiCleanedRowCells[2].__contains__("NY") or fileCounter==1:
                    if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data

                        rowCount = rowCount + 1
                        #var which holds selected rows
                        rowSelection = (semiCleanedRowCells[1].strip()+" "+ # YearEnd
                                        semiCleanedRowCells[2].strip()+" "+ # LocationAbbr
                                        semiCleanedRowCells[5].strip()+","+ # Class
                                        semiCleanedRowCells[6].strip()+","+ # Topic
                                        semiCleanedRowCells[7].strip()+","+ # Question
                                        semiCleanedRowCells[8].strip()+ "," + # Data_Value_Unit
                                        semiCleanedRowCells[9].strip()+ "," + # Data_Value_Type
                                        semiCleanedRowCells[11].strip()+ "," + #
                                        semiCleanedRowCells[12].strip()+ "," +  #
                                        semiCleanedRowCells[13].strip()+ "," + #
                                        semiCleanedRowCells[14].strip()+ "," +  #
                                        semiCleanedRowCells[15].strip()+ "," +  #
                                        semiCleanedRowCells[16].strip()+ ",")  #
                        print(rowSelection)
                        #writer.writerow(rowSelection)
                        #print(rowCount)

#prints out non null NY columns
def readAndPrint():
    rowLimiter = 53840 #more than file lines
    rowCount = 0
    fileCounter = 0
    with open('CSV/NPAO-BRFSS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            fileCounter = fileCounter + 1
            if semiCleanedRowCells[2].__contains__("NY") or fileCounter == 1:
                if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                    fileCounter = fileCounter + 1
                    if rowCount < rowLimiter:
                        print(semiCleanedRow)
                        #print(fileCounter) # 53835 file lines
                        #print(rowCount) # 1009 NY Lines
                        rowCount = rowCount + 1

# This function prints row details that show a relatively easy to read view of only overall statistics about health habits
#  Many rows contain subset data which are not as valuable as overall
# Row count, Year,State,Question,Data Value,Low Confidence Limit, High Confidence Limit, Sample Size
def printValuableLines():
    rowLimiter=100
    rowCount = 0
    fileCounter = 0
    with open('CSV/NPAO-BRFSS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            fileCounter = fileCounter + 1
            if semiCleanedRowCells[2].__contains__("NY") or fileCounter == 1:
                if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                    if (semiCleanedRowCells[32].__contains__("OVR") or fileCounter == 1): # Only consider lines with overall statistics
                        rowSelection = (semiCleanedRowCells[1].strip() + "," +  # YearEnd
                                    semiCleanedRowCells[2].strip() + "," +  # LocationAbbr
                                  # semiCleanedRowCells[5].strip() + "," +  # Class
                                  # semiCleanedRowCells[6].strip() + "," +  # Topic
                                    semiCleanedRowCells[7].strip() + "," +  # Question
                                  # semiCleanedRowCells[8].strip() + "," +  # Data_Value_Unit
                                  # semiCleanedRowCells[9].strip() + "," +  # Data_Value_Type
                                    semiCleanedRowCells[10].strip() + "," +  # data_value
                                    semiCleanedRowCells[14].strip() + "," +  # low confidence limit
                                    semiCleanedRowCells[15].strip() + "," +  # High confidence limit
                                    semiCleanedRowCells[16].strip()) # Sample Size
                        if(rowLimiter>rowCount):
                           # print(rowSelection)
                            print("Row "+str(rowCount)+": "+rowSelection)
                            rowCount = rowCount + 1

# This function will print rows that have not been repeated for the specified column argument
def printUniqueColumnValues(colNum):
    seenVals = []
    rowCount = 0
    fileCounter = 0
    with open('CSV/NPAO-BRFSS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY"):
                if not semiCleanedRow.__contains__("****"): #skip lines with insufficient data
                    if not seenVals.__contains__(semiCleanedRowCells[colNum]):
                        print(semiCleanedRowCells[colNum])
                        seenVals.append(semiCleanedRowCells[colNum])

# This function is supposed to get a list of rows with the top percentages.
# Does not work work correctly and has been depreciated
def printTopTenPercentColumns():
    fileLineCounter = 0
    topColumns = []
    topPercentages = []
    i = 0
    with open('CSV/NPAO-BRFSS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY"):
                if not semiCleanedRow.__contains__("****"): #skip lines with insufficient data
                    if not(semiCleanedRowCells[10]):
                        #this section finds top percentages
                        if len(topPercentages)<10:
                            topPercentages.append(semiCleanedRowCells[10])
                            print("adding:"+semiCleanedRowCells[10])
                        else:
                            print("list is sufficiently big. testing:"+ semiCleanedRowCells[10])
                            for p in topPercentages:
                                if p > semiCleanedRowCells[10]:
                                    print("replacing: "+topPercentages[0]+" with: "+semiCleanedRowCells[10])
                                    topPercentages[0] = semiCleanedRowCells[10]
                                    topPercentages.sort()
        fileLineCounter = fileLineCounter + 1
        topPercentages = topPercentages.sort()
        for top in topPercentages:
            print(top)