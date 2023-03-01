import random
import os
def tambah(a):
    for i in range(12):
        input('ketuk enter untuk tambah angka acak')
        a.append(random.randint(1,30))
        os.system('cls')
        print(a)
        if len(a) == 12:
            print('angka akan di sort')
            

def partition(l, bwh, atas): 
    pivot = l[atas]
    index = bwh
    current = bwh
    while (current < atas) :
        if l[current] <= pivot:
            l[index],l[current]=l[current],l[index] 
            index += 1
        current += 1
    l[index],l[atas] = l[atas],l[index] 
    return index

def quicksort(l, bwh, atas): 
  if bwh < atas:
    index = partition(l, bwh, atas)
    quicksort(l, bwh, index-1) 
    quicksort(l, index+1, atas) 
    return l

list = []
tambah(list)

akhir = quicksort(list,0,len(list)-1)
print("Setelah disort : ",akhir)


        
    
    