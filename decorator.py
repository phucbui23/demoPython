### basic decorator
def testdecor(fun):
    def inner():
        print("Before")
        fun()
        print("After")
    return inner

@testdecor
def test():
    print("Test")

print("========Basic decorator===============")
test()

### argument decorator
def testdecor(fun):
    def inner(*args,**kwargs):
        print("Before")
        fun(*args,**kwargs)
        print("After")
    return inner

@testdecor
def test(name):
    print(name)

print("========argument decorator===============")
test("abcxyz")

### chaining decorator
def testdecor(fun):
    def inner():
        print("Before")
        fun()
        print("After")
    return inner

@testdecor
@testdecor
def test():
    print("Test")

print("========chaining decorator===============")
test()