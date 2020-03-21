class MhsTIF(object):
    def __init__(self, nama, nim, kota, uangsaku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = uangsaku


class buatArray(object):
    internalData = 11 * [None]

    def __getitem__(self, item):
        return self.internalData[item]

    def __setitem__(self, key, value):
        self.internalData[key] = value

    def siapaTerkecil(self):
        terkecil = self[0].uangSaku
        d = []
        for i in self:
            if i.uangSaku <= terkecil:
                terkecil = i.uangSaku
        for i in self:
            if terkecil == i.uangSaku:
                d.append((i.nama, i.nim, i.kotaTinggal, i.uangSaku))
        return d


c = buatArray()
c[0] = MhsTIF('Aulia', 26, 'Wonogiri', 250000)
c[1] = MhsTIF('Tina', 51, 'Surabaya', 200000)
c[2] = MhsTIF('Tika', 2, 'Wonogiri', 245000)
c[3] = MhsTIF('Sinta', 18, 'Bandung', 240000)
c[4] = MhsTIF('Rio', 4, 'Surakarta', 235000)
c[5] = MhsTIF('Bowo', 31, 'Sragen', 260000)
c[6] = MhsTIF('Willi', 10, 'Klaten', 250000)
c[7] = MhsTIF('Putri', 5, 'Semarang', 220000)
c[8] = MhsTIF('Denis', 64, 'Klaten', 225000)
c[9] = MhsTIF('Eka', 23, 'Slogohimo', 215000)
c[10] = MhsTIF('Dina', 29, 'Purwodadi', 245000)


