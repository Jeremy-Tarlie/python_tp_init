def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


tab = []

y = input("Entrez un nombre: ")

while y != "":
    tab.append(int(y))
    y = input("Entrez un nombre: ")

sorted_tab = quick_sort(tab)
print(sorted_tab)