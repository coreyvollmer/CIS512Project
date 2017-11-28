# Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System Reader
# This class contains functions dealing with the CSV/NPAO-BRFSS.csv file.
# CSV Reader and documentation from: https://docs.python.org/3/library/csv.html
# BRF dataset from https://catalog.data.gov/dataset/nutrition-physical-activity-and-obesity-behavioral-risk-factor-surveillance-system

import csv

class BRFReader:
    print("BRF Reader Initialized. Running selected functions in Main...")

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
