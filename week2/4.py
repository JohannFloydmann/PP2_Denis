thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
[print(x) for x in thislist]

#comperhension
#1 way
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#2 way
newlist = [x for x in fruits if "a" in x]

print(newlist)