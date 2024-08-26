import os

name = os.environ.get('NAME')

print(f"Hello, {name}!")

if name:
    print("The secret name is", name)
else:
    print("Name is not found")