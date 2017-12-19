#U.S. Chronic Disease Indicators CSV Reader
#This class contains functions dealing with the CSV/NPAO-BRFSS.csv and CSV/US._Chronic_Disease_Indicators_CDI_.csv files
#CDI dataset from https://catalog.data.gov/dataset/u-s-chronic-disease-indicators-cdi-e50c9
#Dataset is very large, so I made a smaller file which contains all columns with NY data, CSV/CDI-NY.csv

import csv, pandas, matplotlib.pyplot as plt

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
                    if semiCleanedRowCells[29].__contains__("OVERALL") or fileCounter == 1: #only includes rows with overall stratification (not by race or gender)
                        if semiCleanedRowCells[6].__contains__("limitation") or fileCounter == 1: #only include rows which detail conditions that cause limitations on activity
                            rowSelection = (semiCleanedRowCells[0] + "," +  # YearStart
                                        semiCleanedRowCells[2] + "," +  # State
                                        semiCleanedRowCells[5] + "," +  # Topic
                                        semiCleanedRowCells[6] + "," +  # Question
                                        semiCleanedRowCells[8] + "," +  # DataValueUnit
                                        semiCleanedRowCells[9] + "," +  # DataValueType
                                        semiCleanedRowCells[10] + "," +  # DataValue
                                      # semiCleanedRowCells[11] + "," +  # DataValueAlt (this is the same as DataValue, what a waste of space)
                                      # semiCleanedRowCells[12] + "," +  # DataValueFootnoteSymbol
                                      # semiCleanedRowCells[13] + "," +  # DataValueFootnote
                                        semiCleanedRowCells[14] + "," +  # LowConfidenceLimit
                                        semiCleanedRowCells[15] + "," +  # HighConfidenceLimit
                                        semiCleanedRowCells[16])  # StratificationCategory1
                            print(rowSelection)
                            #print("Row "+str(rowCount)+": "+rowSelection)
                            rowCount = rowCount + 1

def readIntoVarList():
    rowCount = 0
    objectList = []
    fileCounter = 0
    outputObjectIndexCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            if semiCleanedRowCells[2].__contains__("NY") or fileCounter == 1:
                if not semiCleanedRow.__contains__("****"):  # skip lines with insufficient data
                    if semiCleanedRowCells[29].__contains__("OVERALL") or fileCounter == 1: #only includes rows with overall stratification (not by race or gender)
                        if semiCleanedRowCells[6].__contains__("limitation") or fileCounter == 1: #only include rows which detail conditions that cause limitations on activity
                            rowSelection = (semiCleanedRowCells[0] + "," +  # YearStart
                                        semiCleanedRowCells[2] + "," +  # State
                                        semiCleanedRowCells[5] + "," +  # Topic
                                        semiCleanedRowCells[6] + "," +  # Question
                                        semiCleanedRowCells[8] + "," +  # DataValueUnit
                                        semiCleanedRowCells[9] + "," +  # DataValueType
                                        semiCleanedRowCells[10] + "," +  # DataValue
                                      # semiCleanedRowCells[11] + "," +  # DataValueAlt (this is the same as DataValue, what a waste of space)
                                      # semiCleanedRowCells[12] + "," +  # DataValueFootnoteSymbol
                                      # semiCleanedRowCells[13] + "," +  # DataValueFootnote
                                        semiCleanedRowCells[14] + "," +  # LowConfidenceLimit
                                        semiCleanedRowCells[15] + "," +  # HighConfidenceLimit
                                        semiCleanedRowCells[16])  # StratificationCategory1

                            objectList.append(cdiDatum(semiCleanedRowCells[0],semiCleanedRowCells[5],semiCleanedRowCells[6],
                                                       semiCleanedRowCells[8],semiCleanedRowCells[9],semiCleanedRowCells[10],
                                                       semiCleanedRowCells[14],semiCleanedRowCells[15]))
                            #print("Row "+str(rowCount)+": "+rowSelection)
                            rowCount = rowCount + 1
    return objectList


#This is a basic class with instance property variables for a row of data
class cdiDatum():
    def __init__(self,YearStart, Topic, Question, DataValueUnit, DataValueType, DataValue, LowConfidenceLimit, HighConfidenceLimit):
        self.yearStart = YearStart
        self.topic = Topic
        self.question = Question
        self.dataValueUnit = DataValueUnit
        self.dataValueType = DataValueType
        self.dataValue = DataValue
        self.lowConfidenceLimit = LowConfidenceLimit
        self.highConfidenceLimit = HighConfidenceLimit

#This function prints all rows with column values matching the function arguments
def printAllMatchingRows(colNum, colVal):
    fileCounter = 0
    with open(fileSelector, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            fileCounter = fileCounter + 1
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")


def pandasPlotActLimArthritis():
    data = pandas.read_csv("CSV/CDI-Cleaned_Subset.csv")
    data = data[data[' Topic'] == " Arthritis"]
    data = data[data[' DataValueType'] == " Crude Prevalence"]

    plt.xlabel("Survey Year")
    plt.ylabel("Crude Prevalence")
    plt.title("Prevalence of Activity Limiting Arthritis")

    #print(data.axes) #this row shows data column names, found missing leading spaces here
    plt.scatter(data['YearStart'],data[' DataValue'])

    plt.show()

def pandasPlotActLimPHD():
    data = pandas.read_csv("CSV/CDI-Cleaned_Subset.csv")
    data = data[data[' Topic'] == " Chronic Obstructive Pulmonary Disease"]
    data = data[data[' DataValueType'] == " Crude Prevalence"]

    plt.xlabel("Survey Year")
    plt.ylabel("Crude Prevalence")
    plt.title("Prevalence of Activity Limiting Chronic Obstructive Pulmonary Disease")

    # print(data.axes) #this row shows data column names, found missing leading spaces here
    plt.scatter(data['YearStart'], data[' DataValue'])

    plt.show()

def pandasPlotRecActLim():
    data = pandas.read_csv("CSV/CDI-Cleaned_Subset.csv")
    data = data[data[' Topic'] == " Overarching Conditions"]
    data = data[data[' DataValueType'] == " Mean"]

    plt.xlabel("Survey Year")
    plt.ylabel("Mean Percentage")
    plt.title("Recent Activity Limitation Among Adults")

    # print(data.axes) #this row shows data column names, found missing leading spaces here
    plt.bar(data['YearStart'], data[' DataValue'])

    plt.show()