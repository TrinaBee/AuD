import time
#bubble sort
def bubble_sort(liste):
    laenge = len(liste)
    swapped = True
    while swapped:
        swapped = False
        for i in range(laenge-1):
            if liste[i] > liste[i+1]:
                liste[i], liste[i+1] = liste[i+1], liste[i]
                swapped = True
            # if i == laenge-1:
            #     laenge -= 1



test_liste = [6,5,3,1,8,7,2,4]
print(test_liste)
start = time.time()
bubble_sort(test_liste)
print(test_liste)
print(time.time()-start)