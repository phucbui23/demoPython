class A:
    pass

    def __bool__(self):
        return False

print(bool(A()))