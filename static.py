# first way
class Calculator: 
    def addNumbers(x, y): 
        return x + y 
        
Calculator.addNumbers = staticmethod(Calculator.addNumbers) 
print('Product:', Calculator.addNumbers(15, 110))

# second way
class Dates:
    a = 6  

    def __init__(self, date):
        self.date = date
        
    def getDate(self):
        return self.date

    @staticmethod
    def toDashDate(date):
        return date.replace("/", "-")

    @classmethod
    def test(cls):
        print(cls.a)

date = Dates("15-12-2016")
dateFromDB = "15/12/2016"
dateWithDash = Dates.toDashDate(dateFromDB) 
# print(dateWithDash.a)   # an object created by calling static method don't have access to the class's properties
print(Dates.a)  # return property from the class

Dates.a = 19    # modify property in the class
date2 = Dates("11-09-1999")

date.a = 9      # modify property in object "date"
date.test()     # have to create an object for class method

print(date.a)   # return property from the class

# class A(metaclass=object):
#     ...

# heap: Date{a:19}
# stack: date{a:9}, date2{a:19}