x = []
y = input("Entrez un nombre: ")

while y != "":
    x.append(int(y))
    y = input("Entrez un nombre: ")

for i in range(len(x)):
    min_index = i
    for j in range(i + 1, len(x)):
        if x[j] < x[min_index]:
            min_index = j
    x[i], x[min_index] = x[min_index], x[i]

print(x)
