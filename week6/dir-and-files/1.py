import os

path = os.getcwd()
print(path)
print("\nDirectories:")
for element in os.listdir(path):
    if os.path.isdir(element):
        print(element)


print("\nFiles:")
for element in os.listdir(path):
    if os.path.isfile(element):
        print(element)

print("\nAll elements:")
for element in os.listdir(path):
    print(element)