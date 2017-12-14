#U.S. Chronic Disease Indicators CSV Reader
#This class contains functions dealing with the CSV/NPAO-BRFSS.csv and CSV/US._Chronic_Disease_Indicators_CDI_.csv files
#CDI dataset from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
#Dataset is very large, so I made a smaller file which contains all columns with NY data, CSV/CDI-NY.csv

import csv

#Full original dataset
#Source: https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
fileSelector = "CSV/U.S._Chronic_Disease_Indicators__CDI_.csv"

#small NY dataset
#fileSelector = "CSV/CDI-NY.csv"

class CDIReader:
    print("CDI Reader Initialized. Running selected functions in Main...")

#only to be used on original dataset
def getNYLineCount():
    rowLimiter = 5
    rowCount = 0
    fileCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            # fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY"):
                fileCounter = fileCounter + 1
                if rowCount < rowLimiter:
                    # print(str(rowCount + 1) + ": " + semiCleanedRow)
                    rowCount = rowCount + 1
    return fileCounter

def insertIntoCDI(cdiObject):
    cdiObject.append()

#prints the first n lines of csv
def printNLines(n):
    rowLimiter = n
    rowCount = 0
    fileCounter = 0
    with open('CSV/U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY"):
                if not semiCleanedRow.__contains__("****"): #skip lines with insufficient data
                    if rowCount < rowLimiter:
                        print("File Line: " +str(fileCounter)+", NY Data Count: "+str(rowCount + 1) + ": " + semiCleanedRow)
                        rowCount = rowCount + 1
                        #print(rowCount)

#Writes cleaned NY File
def NYfileWriter():
    with open('CSV/CDI-NY.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL, dialect='excel')
        #writer = csv.writer(csvfile, delimiter=' ', quotechar='"', quoting=csv.QUOTE_NONE, esc')
        rowCount = 0
        fileCounter = 0
        with open('CSV/U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in reader:
                fileCounter = fileCounter + 1
                semiCleanedRow = ', '.join(row)
                semiCleanedRowCells = semiCleanedRow.split(",")
                if semiCleanedRowCells[2].__contains__("NY") or fileCounter==1:
                    if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                        #print("File Line: " + str(fileCounter) + ", NY Data Count: " + str(rowCount + 1) + ": " + semiCleanedRow)
                        rowCount = rowCount + 1
                        #print(semiCleanedRowCells[1])

                        #var which holds selected rows
                        rowSelection = (semiCleanedRowCells[0]+","+ # YearStart
                                        semiCleanedRowCells[2]+","+ # State
                                        semiCleanedRowCells[5]+","+ # Topic
                                        semiCleanedRowCells[6]+","+ # Question
                                        semiCleanedRowCells[8]+","+ # DataValueUnit
                                        semiCleanedRowCells[9] + "," + # DataValueType
                                        semiCleanedRowCells[10] + "," + # DataValue
                                        semiCleanedRowCells[11] + "," + # DataValueFootnoteSymbol
                                        semiCleanedRowCells[12] + "," +  # DataValueFootnote
                                        semiCleanedRowCells[13] + "," + # LowConfidenceLimit
                                        semiCleanedRowCells[14] + "," +  # HighConfidenceLimit
                                        semiCleanedRowCells[15] + "," )  # StratificationCategory

                        writer.writerow(rowSelection)
                        print(rowCount)


#This function prints every unique value of a column
def printUniqueColumnValues(colNum):
    seenVals = []
    rowCount = 0
    fileCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY") or fileCounter == 1:
                if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                    if semiCleanedRowCells[29].__contains__("OVERALL") or fileCounter == 1:
                        if not seenVals.__contains__(semiCleanedRowCells[colNum]):
                            print(semiCleanedRowCells[colNum])
                            seenVals.append(semiCleanedRowCells[colNum])

def printOverallNYRows():
    rowCount = 0
    fileCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY") or fileCounter == 1:
                if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                    if semiCleanedRowCells[29].__contains__("OVERALL") or fileCounter == 1: #only includes rows with overall stratification
                        if semiCleanedRowCells[6].__contains__("limitation") or fileCounter == 1: #only include rows which detail conditions that cause limitations on activity
                            rowSelection = (semiCleanedRowCells[0] + "," +  # YearStart
                                        semiCleanedRowCells[2] + "," +  # State
                                        semiCleanedRowCells[5] + "," +  # Topic
                                        semiCleanedRowCells[6] + "," +  # Question
                                        semiCleanedRowCells[8] + "," +  # DataValueUnit
                                        semiCleanedRowCells[9] + "," +  # DataValueType
                                        semiCleanedRowCells[10] + "," +  # DataValue
                                    #    semiCleanedRowCells[11] + "," +  # DataValueFootnoteSymbol
                                  #      semiCleanedRowCells[12] + "," +  # DataValueFootnote
                                    #    semiCleanedRowCells[13] + "," +  # DataValueFootnote
                                        semiCleanedRowCells[14] + "," +  # LowConfidenceLimit
                                        semiCleanedRowCells[15] + "," +  # HighConfidenceLimit
                                        semiCleanedRowCells[16] + ",")  # StratificationCategory1

                            print("Row "+str(rowCount)+": "+rowSelection)
                            rowCount = rowCount + 1


#This function prints all rows with column values matching the function arguments
def printAllMatchingRows(colNum, colVal):
    fileCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
