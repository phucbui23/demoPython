lst = [1,1.2, "Hello", True, [1,2]]


### access element
print(lst[0])
print(lst[-1])

### change list element
lst[1] = 2
print(lst)


### add element
lst.append(7)
lst.extend([7,8,9])
lst.insert(1,4)
lst[0:0] = [1,2]

### delete element
del lst[0]
lst.remove(1)
lst.pop(0)
lst[1:2] = []