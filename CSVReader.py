import csv

class CSVReader:
    print("inited")

def getNYLineCount():
    rowLimiter = 5
    rowCount = 0
    fileCounter = 0
    with open('CSV/U.S._Chronic_Disease_Indicators__CDI_.csv', newline='') as csvfile:
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
def csvWriter():
    with open('output.csv', 'w', newline='') as csvfile:
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
                        # 0 : yearstart
                        # 1 : yearend
                        # 2 : location
                        # 4 : data sourde
                        # 5 : topic
                        # 6 : question

                        writer.writerow(semiCleanedRow)
                        #selectedColumns = semiCleanedRowCells[0,2]
                        #writer.writerow(selectedColumns)
                        # print(rowCount)