example = {
    "brand": "ford",
    "model": "mustang",
    "year": 1964,
    "year": 2022,
    "colors": ["red", "white"]
}

print("Demo access item")
print(example["colors"])
print(example.get("year"))
print(example.keys())
print(example.values())
print(example.items())

print("Demo change item")
example.update({"year": 2001})
print(example["year"])

print("Demo add item")
example.update({"name": "ford2001"})
print(example)

print("Demo remove item")
example.pop("colors")
print(example)
example.popitem()
print(example)

print("Demo copy")
copy1 = example.copy()
copy2 = dict(example)

print(copy1)
print(copy2)


