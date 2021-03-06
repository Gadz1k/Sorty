### Bubble Sort
print("Bubble Sort")

liczby = [5,6,3,9,10,14,18,2,73,54,21,19]

def bubble(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

print(liczby)
bubble(liczby)
print(liczby)

### Merge Sort
print("Merge Sort")

liczby = [5,6,3,9,10,14,18,2,73,54,21,19]

def merge(lista):
    if len(lista) > 1:
        m = len(lista)//2
        l = lista[:m]
        r = lista[m:]

        merge(l)
        merge(r)
  
        i = j = k = 0
  
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                lista[k] = l[i]
                i += 1
            else:
                lista[k] = r[j]
                j += 1
            k += 1
  
        while i < len(l):
            lista[k] = l[i]
            i += 1
            k += 1
  
        while j < len(r):
            lista[k] = r[j]
            j += 1
            k += 1

print(liczby)
merge(liczby)
print(liczby)

### QuickSort
print("QuickSort")

liczby = [5,6,3,9,10,14,18,2,73,54,21,19]

def partition(lista, left, right):
    i = (left - 1)
    pivot = lista[right]
    for j in range(left, right):
        if lista[j] <= pivot:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]
    lista[i + 1], lista[right] = lista[right], lista[i + 1]
    return (i + 1)



def quick(lista, left, right):
    if left < right:
        pi = partition(lista, left, right)
        quick(lista, left, pi - 1)
        quick(lista, pi + 1, right)

print(liczby)
quick(liczby,0,len(liczby)-1)
print(liczby)
