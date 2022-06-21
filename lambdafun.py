from tokenize import Double


### basic lambda
double = lambda x: x*2

add = lambda x,y: x+y

### map
x = list(map(lambda x: x*2, [1,2,3,4]))
print(x)

### filter
lst = [1,2,3,4,5]
new_lst = list(filter(lambda x: x%2==0, lst))

print(new_lst)