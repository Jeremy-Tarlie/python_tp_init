tab1 = []
tab2 = []

x = input("Entrez un nombre: ")
while x != "":
    tab1.append(int(x))
    x = input("Entrez un nombre: ")

for i in range(len(tab1)):
    tab2.append(tab1[i])
    for j in range(len(tab2)):
        if tab2[j] > tab2[i]:
            tab2[i], tab2[j] = tab2[j], tab2[i]
            
print(tab2)