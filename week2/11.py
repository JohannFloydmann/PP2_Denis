thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

x = thisdict.get("model")
x = thisdict.keys()
x = thisdict.values()
x = thisdict.items()

thisdict.update({"year": 2020})

thisdict.pop("model")
thisdict.popitem()
del thisdict["model"]

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])