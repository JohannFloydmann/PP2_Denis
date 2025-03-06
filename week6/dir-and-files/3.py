import os

path = input("Enter the path: ")
path.strip()

exists = os.access(path, os.F_OK)
if exists:
        print("Directory exists")
        if os.path.isfile(path):
            directory = os.path.dirname(path)
            filename = os.path.basename(path)
        else:
              directory = path
              filename = "NO FILE"
        print(f"Directory portion: '{directory}'")
        print(f"Filename portion: '{filename}'")
else:
      print("Directory doesn't exist")