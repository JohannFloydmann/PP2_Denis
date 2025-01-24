thistuple = ("apple",)
print(type(thistuple))

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


y = ("apple", "banana", "cherry")
y += thistuple
print(y)