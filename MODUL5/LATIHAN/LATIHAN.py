#Modul5-Pengurutan

def swap(A, p, q):
    tmp = A[p]
    A[p] = A[q]
    A[q] = tmp


def cariPosisiTerkecil(A, dariSini, sampaiSini):
    posisiTerkecil = dariSini
    for i in range(dariSini + 1, sampaiSini):
        if A[i] < A[posisiTerkecil]:
            posisiTerkecil = i
    return posisiTerkecil

def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1)
    return A

worst = [99, 87, 76, 65, 53, 42, 33, 20, 11, 3]
average = [3, 20, 11, 76, 87, 99, 42, 53, 33, 65]
best = [3, 11, 20, 33, 42, 53, 65, 76, 87, 99]

hasil1 = bubbleSort(worst)
hasil2 = bubbleSort(average)
hasil3 = bubbleSort(best)

def selectionSort(A):
    n = len(A)
    for i in range(n-1):
        indexKecil = cariPosisiTerkecil(A, i, n)
        if indexKecil != i:
            swap(A, i, indexKecil)
    return A

ss1 = selectionSort(worst)
ss2 = selectionSort(average)
ss3 = selectionSort(best)

def insertionSort(A):
    n = len(A)
    for i in range(1, n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
    return A

is1 = insertionSort(worst)
is2 = insertionSort(average)
is3 = insertionSort(best)
