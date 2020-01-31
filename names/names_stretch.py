import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()
names_1 = sorted(names_1)
f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

def binary_search(name):
    global names_1
    top = len(names_1) -1
    bottom = 0
    while top >= bottom:
        middle = (top + bottom)//2
        middleName = names_1[middle]
        if middleName == name:
            return True
        elif middleName < name:
            bottom = middle + 1
        elif middleName > name:
            top = middle - 1
    return False

for name_2 in names_2:
    if binary_search(name_2):
        duplicates.append(name_2)




end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

