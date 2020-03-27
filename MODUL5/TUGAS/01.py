class MhsTIF(object):
    def __init__(self, nama, nim, asal, us):
        self.nama = nama
        self.nim = nim
        self.asal = asal
        self.uangsaku = us

def swap(A, p, q):
    temp = A[p]
    A[p] = A[q]
    A[q] = temp

def nimurut(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if A[j].nim > A[j + 1].nim:
                swap(A, j, j + 1)
    listUrut = []
    for k in A:
        listUrut.append((k.nim, k.nama, k.asal, k.uangsaku))
    return listUrut

daftar = [ (MhsTIF('Aulia', 26, 'Wonogiri', 250000)),
            (MhsTIF('Tina', 51, 'Surabaya', 200000)),
            (MhsTIF('Tika', 2, 'Wonogiri', 245000)),
            (MhsTIF('Sinta', 18, 'Bandung', 240000)),
            (MhsTIF('Rio', 4, 'Surakarta', 235000)),
            (MhsTIF('Bowo', 31, 'Sragen', 260000)),
            (MhsTIF('Willi', 10, 'Klaten', 250000)),
            (MhsTIF('Putri', 5, 'Semarang', 220000)),
            (MhsTIF('Denis', 64, 'Klaten', 225000)),
            (MhsTIF('Eka', 23, 'Slogohimo', 215000)),
            (MhsTIF('Dina', 29, 'Purwodadi', 245000))]

