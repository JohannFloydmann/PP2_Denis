thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist)
print(len(thislist))

thislist[1:3] = ["blackcurrant", "watermelon"]
thislist.insert(2, "watermelon")
thislist.append("orange")
thislist.remove("watermelon")
print(thislist[-4:-1])
thislist.pop(1)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

thislist2 = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist2)

tropical = ("mango", "pineapple", "papaya")
thislist2.extend(tropical)
print(thislist2)
del tropical
thislist2.clear()