import glob

myfiles = glob.glob("../projects/*.py")

for file in myfiles:
    print(file)

"""READ ALL FILE CONTENT IN GIVEN DIRECTORY IN UPPERCASE"""
for file in myfiles:
    with open(file, 'r') as f:
        print(f.read().upper())