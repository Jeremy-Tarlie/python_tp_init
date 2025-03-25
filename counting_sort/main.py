tab1 = []

x = input("Entrez un nombre: ")

while x != "":
    tab1.append(int(x))
    x = input("Entrez un nombre: ")

max_value = max(tab1)
count = [0] * (max_value + 1)

while len(tab1) > 0:
    num = tab1.pop(0)
    count[num] += 1

for i in range(len(count)):
    while count[i] > 0:
        tab1.append(i)
        count[i] -= 1

print(tab1)