# CSV Reader and documentation from: https://docs.python.org/3/library/csv.html
import CSVReader

def Main():
    reader = CSVReader
    #print(reader.getNYLineCount())
    #CDI = [dict() for x in range(reader.getNYLineCount())]
    #CDI.append("test")
    #reader.printNLines(10)
    reader.csvWriter()
if __name__ == "__main__":
    Main()
