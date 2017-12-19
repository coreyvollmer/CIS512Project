import Main
import csv, pandas

def readAndPrint():
    rowCount = 0
    fileCounter = 0
    with open('CSV/BLS-CPS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in reader:
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            fileCounter = fileCounter + 1
            print(semiCleanedRow)

def readIntoPandas():
    data = pandas.read_csv("CSV/BLS-CPS.csv", error_bad_lines=False)
    print(data.axes)
    print(data)

def readIntoVarList():
    fileCounter = 0
    objectList = []
    with open('CSV/BLS-CPS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            semiCleanedRow = ', '.join(row)
            semiCleanedRowCells = semiCleanedRow.split(",")
            fileCounter = fileCounter + 1
            if(fileCounter>=38):
                objectList.append(
                    annualAvgIndustry(
                    semiCleanedRowCells[0],
                    semiCleanedRowCells[1],
                    semiCleanedRowCells[2],
                    semiCleanedRowCells[3],
                    semiCleanedRowCells[4],
                    semiCleanedRowCells[5],
                    semiCleanedRowCells[6],
                    semiCleanedRowCells[7]
                ))
    return objectList

def reportAllVariables(objectList):
    for annualAvgIndustry in objectList:
        annualAvgIndustry.printAll()

def reportTopIndustries(industryList):
    print("top industries:")
    topFiveIndustries = []
    topFiveRates = []
    for industry in industryList:
        if(len(topFiveIndustries)<5):
            topFiveIndustries.append(industry)
            print("populating industry list")
        if(len(topFiveIndustries)>=5):
            i = 0
            lowestIndex = 6
            lowestSoFar = 5
            for topIndustry in topFiveIndustries:
                print("testing: "+topIndustry.name)
                print("testing: "+ str(float(topIndustry.lostWorkIlnInj)))
                print()
                if (float(topIndustry.lostWorkIlnInj) < float(lowestSoFar)):
                    lowestSoFar = topIndustry.lostWorkIlnInj
                    lowestIndex = i
                    print("Lowest so far: " + str(lowestSoFar) + "| lowest index: " + str(i))
                i = i + 1
            print("removing: " +str(i))
            topFiveIndustries.pop(lowestIndex)
            topFiveIndustries.append(industry)
            print(topFiveIndustries[0].name)
            print(topFiveIndustries[1].name)
            print(topFiveIndustries[2].name)
            print(topFiveIndustries[3].name)
            print(topFiveIndustries[4].name)






class annualAvgIndustry():
    def __init__(self,name,sampleSize,absRateTotal,absRateIlnInj,absRateOther,lostWorkTotal,lostWorkIlnInj,lostWorkOther):
        self.name = name
        self.sampleSize = sampleSize
        self.absRateTotal = absRateTotal
        self.absRateIlnInj = absRateIlnInj
        self.absRateOther = absRateOther
        self.lostWorkTotal = lostWorkTotal
        self.lostWorkIlnInj = lostWorkIlnInj
        self.lostWorkOther = lostWorkOther

    def printAll(self):
        print(self.name)
        print(self.sampleSize)
        print(self.absRateTotal)
        print(self.absRateIlnInj)
        print(self.absRateOther)
        print(self.lostWorkTotal)
        print(self.lostWorkIlnInj)
        print(self.lostWorkOther)
