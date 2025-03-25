x = []
y = int(input("Entrez un nombre : "))

while y != "":
    x.append(int(y))
    y = input("Entrez un nombre : ")
    

for i in range(len(x)):
    for j in range(len(x)):
        if x[i] < x[j]:
            x[i], x[j] = x[j], x[i]
     
print("Tableau trié :")       
print(x)