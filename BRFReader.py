# Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System Reader
# This class contains functions dealing with the CSV/NPAO-BRFSS.csv file.
# CSV Reader and documentation from: https://docs.python.org/3/library/csv.html
# BRF dataset from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system

import csv, re

#Original dataset from web
dataSetPath="CSV/NPAO-BRFSS.csv"

#Cleaned dataset path
cleanDataSetPath="CSV/BRFSS-Clean.csv"

class BRFReader:
    print("BRF Reader Initialized. Running selected functions in Main...")


def writeCleanedCSVFile():
    with open(cleanDataSetPath, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL, dialect='excel')
        #writer = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_NONE, esc')
        rowCount = 0
        fileCounter = 0
        with open(dataSetPath, newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                fileCounter = fileCounter + 1
                semiCleanedRow = ', '.join(row)
                semiCleanedRowCells = semiCleanedRow.split(",")
                if semiCleanedRowCells[2].__contains__("NY") or fileCounter==1:
                    if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                        rowCount = rowCount + 1
                        print(semiCleanedRowCells[1].strip)
                        #var which holds selected rows
                        rowSelection = (semiCleanedRowCells[1].strip()+","+ # YearEnd
                                        semiCleanedRowCells[2].strip()+","+ # LocationAbbr
                                        semiCleanedRowCells[5]+","+ # Class
                                        semiCleanedRowCells[6]+","+ # Topic
                                        semiCleanedRowCells[7]+","+ # Question
                                        semiCleanedRowCells[8] + "," + # Data_Value_Unit
                                        semiCleanedRowCells[9] + "," + # Data_Value_Type
                                        semiCleanedRowCells[11] + "," + #
                                        semiCleanedRowCells[12] + "," +  #
                                        semiCleanedRowCells[13] + "," + #
                                        semiCleanedRowCells[14] + "," +  #
                                        semiCleanedRowCells[15] + "," +  #
                                        semiCleanedRowCells[16] + ",")  #
                        writer.
                        print(rowCount)



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


def printValuableLines():
    rowLimiter=10
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

                    selectedColumns=semiCleanedRowCells[1] +" |_| "+ semiCleanedRowCells[2] +" |_| "+ semiCleanedRowCells[5] +" |_| "+ semiCleanedRowCells[6] +" |_| "+ semiCleanedRowCells[7]  +" |_| "+ semiCleanedRowCells[9] +" |_| "+ semiCleanedRowCells[10] + " |_| "
                    if(rowLimiter>rowCount):
                        print(selectedColumns)
                        rowCount = rowCount + 1

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


