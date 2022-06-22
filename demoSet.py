example1 = {"one", 1, 2,3, "six",4,5,6,7,8}
print("Demo unordered:")
print(example1)

print("Demo Change item")
example1.add("new")
print(example1)

example2 = ["item1", "item2"]
example1.update(example2)
print(example1)

print("Demo remove item")
example1.remove("one")
print(example1)
example1.discard("item2")
print(example1)
example1.pop()
print(example1)

print("Demo join sets")
example3 = {"1", "6", "13"}
print(example1.union(example3))

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)
print(x)

z = {"apple", "banana", "cherry"}
k = {"google", "microsoft", "apple"}

z.symmetric_difference_update(k)
print(z)


a = {1,1}
print(a)




