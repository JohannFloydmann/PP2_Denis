thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset.add("orange")
print(thisset)


tropical = ["pineapple", "mango", "papaya"]
thisset.update(tropical)
print(thisset)


thisset.remove("banana")
thisset.discard("banana")
print(thisset)


#The union() and update() methods joins all items from both sets.

#The intersection() method keeps ONLY the duplicates.

#The difference() method keeps the items from the first set that are not in the other set(s).

#The symmetric_difference() method keeps all items EXCEPT the duplicates.