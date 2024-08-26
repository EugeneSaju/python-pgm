import os

name = os.environ.get('NAME')

if name:
    print("The secret name is", name)
else:
    print("Name is not found")