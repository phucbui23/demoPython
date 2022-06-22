# first way
class Calculator: 
    def addNumbers(x, y): 
        return x + y 
        
Calculator.addNumbers = staticmethod(Calculator.addNumbers) 
print('Product:', Calculator.addNumbers(15, 110))

# second way
class Dates:
    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB)

if(date.getDate() == dateWithDash):
    print("Equal")
print("Unequal")