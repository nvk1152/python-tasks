from os import walk

for (_, _, filenames) in walk('.'):
    for name in filenames:
        if name.endswith(".py"):
            print(name, end=", ")