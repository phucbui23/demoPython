#### basic function
def test1(fname):
    print(fname)

print("Test for basic function")
test1("abcxyz")


#### return function
def test2(fname):
    return fname

print("Test for function have return")
print(test2("ancxyz"))


### arbitrary arguments
def test3(*args):
    for x in args:
        print(x)

print("Test for arbitrary arguments")
test3(1,2,3)
test3(1,2,3,4,5)


### keyword arguments
def test4(fname, lname):
    print(fname, lname)

print("Test for keyword arguments")
test4(fname="abc", lname="xyz")

### arbitrary keyword argument
def test5(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

print("Test for arbitrary keyword arguments")
test5(fname="abc", lname="xyz")
test5(fname="abc", lname="xyz", name="qaz")


### default param value
def test6(fname="abc"):
    print(fname)

print("Test for default value")
test6()

