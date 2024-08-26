import sys

name = sys.argv[1]

print(f"Hello, {name}!")

if name:
    print("The secret name is", name)
else:
    print("Name is not found")